import styles from './Why.module.css';


export const WhySection = () => {
  return (
      <div className={styles.main}>
      <ul>
        <li>
          Близкое расположение к метро
        </li>
        <li>
          Возможность играть и выпивать
        </li>
        <li>
          Популярное место (сбор через carpet)
        </li>
        <li>
          Более 100 настольных игр
        </li>
        <li>
          <b>Программа лояльности</b>
        </li>
      </ul>
    </div>
  );
}
