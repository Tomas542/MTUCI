import typing as tp
import warnings

import chex
import jax
import matplotlib.pyplot as plt
import numpy as np
from flax import nnx
from jax import numpy as jnp


class MLP(nnx.Module):
    """Simple MLP with variable hidden layers' size

    Args:
        - input_dim (int) - num of input features. Default: 60
        - hidden (tuple[int]) - optional sizes of hidden layers. Default: None
        - output_dim (int) - num of output features. Default: 10
        - rngs (nnx.Rngs) - random generator.

    Example:
    >>> import jax.numpy as jnp
    >>> from flax import nnx
    >>> model = MLP(input_dim=60, hidden=(5,), output_dim=10, rngs=nnx.Rngs(42))
    >>> y = jnp.ones(60)
    >>> model(y)
    Array([0.1900208], dtype=float32)
    """

    def __init__(
        self,
        input_dim: int = 60,
        hidden: tp.Optional[tuple[int]] = None,
        output_dim: int = 10,
        rngs: tp.Optional[nnx.Rngs] = None,
    ) -> None:
        # init random generator for Jax
        if rngs is None:
            rngs = nnx.Rngs(42)

        # layers = [nnx.RMSNorm(60, rngs=rngs)] # store all layers
        layers = []  # store all layers

        # without hidden
        if hidden is None:
            layers.append(nnx.Linear(input_dim, output_dim, rngs=rngs))

        # init hidden layers with ReLU
        else:
            last_layer = input_dim  # out_featuers of the last layer
            for hidden_layer in hidden:
                layers.append(
                    nnx.Linear(
                        in_features=last_layer, out_features=hidden_layer, rngs=rngs
                    )
                )
                layers.append(nnx.swish)
                # layers.append(nnx.Dropout(0.05, rngs=rngs))
                last_layer = hidden_layer
            layers.append(nnx.Linear(last_layer, output_dim, rngs=rngs))

        # unpack all layers to call them later
        self.nn = nnx.Sequential(*layers)
        del layers

    def __call__(self, x: chex.Array) -> chex.Array:
        x = self.nn(x)
        return x


class MAE(nnx.metrics.Average):
    """Mean-absolute Error metric. This metric subclasses :class:`Average`,
    and so they share the same ``reset`` and ``compute`` method
    implementations. Unlike :class:`Average`, no string needs to
    be passed to ``MAE`` during construction.

    Example usage::

    >>> from flax import nnx
    >>> import jax, jax.numpy as jnp

    >>> logits = jax.random.normal(jax.random.key(0), (5, 2))
    >>> targets = jnp.array([1, 1, 0, 1, 0])
    >>> logits2 = jax.random.normal(jax.random.key(1), (5, 2))
    >>> targets2 = jnp.array([0, 1, 1, 1, 1])

    >>> metrics = nnx.metrics.MAE()
    >>> metrics.compute()
    Array(nan, dtype=float32)
    >>> metrics.update(logits=logits, targets=targets)
    >>> metrics.compute()
    Array(0.6, dtype=float32)
    >>> metrics.update(logits=logits2, targets=targets2)
    >>> metrics.compute()
    Array(0.7, dtype=float32)
    >>> metrics.reset()
    >>> metrics.compute()
    Array(nan, dtype=float32)
    """

    def update(
        self, *, logits: chex.ArrayBatched, targets: chex.ArrayBatched, **_
    ) -> None:
        """In-place update this ``Metric``.

        Args:
        logits: the outputted predicted activations. These values are
        argmax-ed (on the trailing dimension), before comparing them
        to the targets.
        targets: the ground truth integer targets.
        """
        if logits.ndim != targets.ndim + 1:
            raise ValueError(
                f"Expected logits.ndim==targets.ndim+1, got {logits.ndim} and {targets.ndim}"
            )
        elif targets.dtype in (jnp.int64, np.int32, np.int64, jnp.int32):
            targets = jnp.astype(targets, jnp.float32)
        elif targets.dtype != jnp.float32:
            raise ValueError(
                f"Expected targets.dtype==jnp.float32, got {targets.dtype}"
            )

        super().update(values=(jnp.abs(logits - targets)))


class Accuracy(nnx.metrics.Average):
    """Accuracy metric. This metric subclasses :class:`Average`,
    and so they share the same ``reset`` and ``compute`` method
    implementations. Unlike :class:`Average`, no string needs to
    be passed to ``Accuracy`` during construction.

    Example usage::

        >>> from flax import nnx
        >>> import jax, jax.numpy as jnp

        >>> logits = jax.random.normal(jax.random.key(0), (5, 2))
        >>> labels = jnp.array([1, 1, 0, 1, 0])
        >>> logits2 = jax.random.normal(jax.random.key(1), (5, 2))
        >>> labels2 = jnp.array([0, 1, 1, 1, 1])

        >>> metrics = nnx.metrics.Accuracy()
        >>> metrics.compute()
        Array(nan, dtype=float32)
        >>> metrics.update(logits=logits, labels=labels)
        >>> metrics.compute()
        Array(0.6, dtype=float32)
        >>> metrics.update(logits=logits2, labels=labels2)
        >>> metrics.compute()
        Array(0.7, dtype=float32)
        >>> metrics.reset()
        >>> metrics.compute()
        Array(nan, dtype=float32)
    """

    def update(
        self, *, logits: chex.ArrayBatched, labels: chex.ArrayBatched, **_
    ) -> None:  # type: ignore[override]
        """In-place update this ``Metric``.

        Args:
        logits: the outputted predicted activations. These values are
            argmax-ed (on the trailing dimension), before comparing them
            to the labels.
        labels: the ground truth integer labels.
        """
        if logits.ndim != labels.ndim + 1:
            raise ValueError(
                f"Expected labels.dtype==jnp.int32 and logits.ndim={logits.ndim}=="
                f"labels.ndim+1={labels.ndim + 1}"
            )
        super().update(values=(logits.argmax(axis=-1) == labels))


def _init_model(
    input_dim: int = 60,
    hidden: tp.Optional[tuple[int]] = None,
    output_dim: int = 10,
    rngs: tp.Optional[nnx.Rngs] = None,
) -> tuple[tp.Union[MLP, nnx.State]]:
    """Inits MLP model with hidden layers.

    Args:
        - input_dim (int) - num of input features. Default: 60
        - hidden (tuple[int]) - optional sizes of hidden layers. Default: None
        - output_dim (int) - num of output features. Default: 10
        - rngs (nnx.Rngs) - random generator.

    Example:
    >>> model = _init_model(input_dim=60,
                            hidden=(5,),
                            output_dim=10,
                            rngs=nnx.Rngs(42))
    """
    model = MLP(input_dim=input_dim, hidden=hidden, output_dim=output_dim, rngs=rngs)
    default_weights = nnx.state(model)
    return model, default_weights


def _init_metrics_hisory() -> dict[str, list[chex.Array]]:
    """Creates metrics_history
    Example:
    >>> metrics = _init_metrics_hisory()
    >>> metrics
    {'train_loss': [], 'train_accuracy': [], 'test_loss': [], 'test_accuracy': []}
    """
    metrics_history = {
        "train_loss": [],
        "train_accuracy": [0],
        "test_loss": [],
        "test_accuracy": [0],
    }
    return metrics_history


def plot_metrics(metrics_history: dict[str, list[chex.Array]]) -> None:
    """Plot metrics for train and test loss and accuracy"""
    labels = set()
    metrics = set()
    for k in metrics_history:
        label, metric = k.split("_")
        labels.add(label)
        metrics.add(metric)

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
    fig.tight_layout(pad=3.5)
    i = 0

    for metric in metrics:
        for label in labels:
            ax[i].plot(metrics_history[f"{label}_{metric}"], label=label.capitalize())

        ax[i].set_title(f"Train and Test {metric.capitalize()}", fontsize=14)
        ax[i].set_xlabel("Epoch", fontsize=11.5)
        ax[i].set_ylabel(f"{metric.capitalize()}", fontsize=11.5)

        ax[i].legend()
        i += 1
        print(metric)


def batch(
    X: chex.Array,  # noqa: N803
    y: chex.Array,
    batch_size: int,
    key: chex.PRNGKey,
    train: bool = False,
) -> tp.Generator[tuple[chex.ArrayBatched], None, None]:
    assert X.shape[0] == y.shape[0], (
        f"Features and labels must have same dimensions, but got {X.shape[0]} and {y.shape[0]} respectively"
    )
    if X.shape[0] % batch_size:
        warnings.warn(
            f"Can't split X with {X.shape[0]} examples in equal batches with {batch_size=}. Last batch will be droped",
            category=UserWarning,
        )
    if train:
        permutation_order = jax.random.permutation(key=key, x=X.shape[0])
        for batch_ in range(X.shape[0] // batch_size):
            yield (
                X[permutation_order[batch_ * batch_size : (batch_ + 1) * batch_size]],
                y[permutation_order[batch_ * batch_size : (batch_ + 1) * batch_size]],
            )
    else:
        for batch_ in range(X.shape[0] // batch_size):
            yield (
                X[batch_ * batch_size : (batch_ + 1) * batch_size],
                y[batch_ * batch_size : (batch_ + 1) * batch_size],
            )
