import random as r
import math as m


def gen_dots(
    x_min: int, x_max: int, y_min: int, y_max: int, num_exps: int
) -> tuple[list[float], list[float]]:
    x_r = [(x_max - x_min) * r.random() + x_min for _ in range(num_exps)]
    y_r = [(y_max - y_min) * r.random() + y_min for _ in range(num_exps)]
    dots = [(x_i, y_i) for x_i, y_i in zip(x_r, y_r)]
    return dots


def compute_delta(res: list[float]) -> list[float]:
    return [abs(res_i - res_i_1) / res_i for res_i, res_i_1 in zip(res, res[1:])]


def monte_carlo(num_exps: int, x0: int, y0: int, r0: int) -> tuple[float, float]:
    dots = gen_dots(x0 - r0, x0 + r0, y0 - r0, y0 + r0, num_exps)

    in_circle, in_square = compute_distance(dots, x0, y0, r0)
    pi = 4 * (in_circle / in_square)

    return pi


def compute_distance(
    dots: list[tuple[float]], x0: int, y0: int, r0: int
) -> tuple[int, int]:
    in_circle = 0

    for dot in dots:
        x, y = dot
        r = m.sqrt(m.pow(x - x0, 2) + m.pow(y - y0, 2))
        if r <= r0:
            in_circle += 1

    return in_circle, len(dots)


def integral(start: int = 0, end: int = 2, num_exps: int = 10_000) -> float:
    x_min, x_max = min(start, end), max(start, end)
    func = lambda x: m.pow(x, 3) + 1  # noqa: E731
    y_min, y_max = 0, func(x_max)

    dots = gen_dots(x_min, x_max, y_min, y_max, num_exps)
    under_integral = 0
    for dot in dots:
        x, y = dot
        if y < func(x):
            under_integral += 1

    total_dots = len(dots)

    s_square = (x_max - x_min) * (y_max - y_min)
    s_int = (under_integral / total_dots) * s_square
    return s_int


def main(x0: int = 0, y0: int = 2, r0: int = 5) -> None:
    num_exps = 8
    num_dots = [10**i for i in range(1, num_exps)]
    pi1 = [0] * (num_exps - 1)
    # вообще list лучше так не спаунить из-за ссылочной натуры
    # [0 for _ in range(num_exps)] # не тестил

    # 1-2 tasks
    for i, experiment in enumerate(num_dots):
        pi1[i] = monte_carlo(experiment, x0, y0, r0)

    delta1 = compute_delta(pi1)

    print(f"{pi1=}, {delta1=}")

    num_repeats = 5
    pi2 = [0] * (num_exps - 1)
    for i, experiment in enumerate(num_dots):
        pi_i = [0] * num_repeats
        for j in range(num_repeats):
            pi_i[j] = monte_carlo(experiment, x0, y0, r0)

        pi2[i] = sum(pi_i) / num_repeats

    delta2 = compute_delta(pi2)

    print(f"{pi2=}, {delta2=}")

    num_dots = [10**i for i in range(4, 8)]
    num_repeats = 3
    integrals = [0] * len(num_dots)
    for i, experiment in enumerate(num_dots):
        integral_i = [0] * num_repeats
        for j in range(num_repeats):
            integral_i[j] = integral(num_exps=experiment)
        integrals[i] = sum(integral_i) / num_repeats
    print(integrals)

    delta3 = compute_delta(integrals)
    print(f"{integrals=}, {delta3=}")

    return pi1, delta1, pi2, delta2, integrals, delta3


if __name__ == "__main__":
    main()
