
import styles from './InfoSection.module.css';

export const InfoSection = () => {
  return (
    <div className={styles.infoContainer}>
      <p>
        Пополнить здоровье и манну? А может просто вкусно покушать? Для любой компании у нас есть бесплатные кофе, чай, печенье, хлопья и прочие снеки.
      </p>
      <p>
        Также отдельно работает кухня, где вы можете заказать блюдо поесть или пенное попить.
      </p>
    </div>
  );
}
