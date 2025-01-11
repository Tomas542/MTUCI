// unworking API-like call to JSON
import styles from './Reviews.module.css';

import React, { useEffect, useState } from 'react'; 

interface JSONReviews { 
  text: string; 
  reviewer: string; 
  date: string
}

export const Reviews2: React.FC = () => {
  const [reviews, setReviews] = useState<JSONReviews[]>([]); 
  const [reviewsLength, setReviewsLength] = useState<number>(0); 
  useEffect(() => { 
    const fetchReviews = async () => { 
      const response = await fetch('../../../src/assets/reviews.json'); 
      const data: JSONReviews[] = await response.json(); 
      setReviews(data); 
      setReviewsLength(data.length);
    }; 
    fetchReviews(); 
  }, []);

  const [currentIndex, setCurrentIndex] = useState(0);

  const handlePrev = () => {
    setCurrentIndex((prevIndex) => (prevIndex === 0 ? reviewsLength - 1 : prevIndex - 1));
  };

  const handleNext = () => {
    setCurrentIndex((prevIndex) => (prevIndex === reviewsLength - 1 ? 0 : prevIndex + 1));
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
