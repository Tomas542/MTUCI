import { Activity } from "../homeActivity"
import styles from './Activities.module.css';

export const Activities = () => {
  return (
    <div className={styles.activityBorder}>
      <ul role='list' className={styles.activitiesContainer}>
        <Activity 
          img_src="https://optim.tildacdn.com/tild3162-3761-4831-a630-636661326136/-/resize/90x/-/format/webp/icons8---100.png"
          header_text="Веселитесь"
          main_text="Проведите уютный день или вечер в компании друзей за партией в любимую игру."
        />
        <Activity 
          img_src="https://optim.tildacdn.com/tild3535-3332-4737-a261-613130656436/-/resize/90x/-/format/webp/icons8--100.png"
          header_text="Читайте"
          main_text="Огромная коллекция книг и комиксов. Разнообразные сюжеты, качественная печать и широкий выбор."
        />
        <Activity 
          img_src="https://optim.tildacdn.com/tild6666-3765-4531-b737-346566666461/-/resize/90x/-/format/webp/icons8----100.png"
          header_text="Работайте"
          main_text="Наше кафе также подходит для работы. Розетки, высокоскоростной интернет и не только."
        />
        <Activity 
          img_src="https://optim.tildacdn.com/tild6635-6163-4732-b361-333734623264/-/resize/90x/-/format/webp/icons8--100.png"
          header_text="Смотрите"
          main_text="Насладитесь вместе с друзьями кино или играйте в свои любимые игры на проекторе."
        />
      </ul>
    </div>
  );
}