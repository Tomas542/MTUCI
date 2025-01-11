import { useState } from 'react';
import styles from './Reviews.module.css';

const reviews = [
  {
    text: "Отличное место! Очень уютно и вкусно.",
    reviewer: "Анна Иванова",
    date: "10 октября 2024"
  },
  {
    text: "Пиииво!.",
    reviewer: "Иван Петров",
    date: "15 октября 2024"
  },
  {
    text: "ПиВо 🍻.",
    reviewer: "Мария Смирнова",
    date: "20 октября 2024"
  },
  {
    text: "Место хорошее, светлое и нефильтрованное.",
    reviewer: "Алексей Кузнецов",
    date: "22 октября 2024"
  }
];

export const Reviews = () => {
  const [currentIndex, setCurrentIndex] = useState(0);

  const handlePrev = () => {
    setCurrentIndex((prevIndex) => (prevIndex === 0 ? reviews.length - 1 : prevIndex - 1));
  };

  const handleNext = () => {
    setCurrentIndex((prevIndex) => (prevIndex === reviews.length - 1 ? 0 : prevIndex + 1));
  };

  return (
    <div className={styles.reviewsContainer}>
      <button className={`${styles.arrow} ${styles.left}`} onClick={handlePrev}>‹</button>
      <div className={styles.reviewCard}>
        <p>{reviews[currentIndex].text}</p>
        <p className={styles.reviewer}>{reviews[currentIndex].reviewer}</p>
        <p>{reviews[currentIndex].date}</p>
      </div>
      <button className={`${styles.arrow} ${styles.right}`} onClick={handleNext}>›</button>
    </div>
  );
}

