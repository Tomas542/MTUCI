import { useState } from 'react';
import styles from './Room.module.css';

// const base = [
//   "https://static.tildacdn.com/tild6562-3235-4661-a365-343162313539/IMG_7662_enfuse.jpg",
//   "https://static.tildacdn.com/tild6133-6564-4733-b764-356334626565/IMG_7683_enfuse.jpg",
//   "https://static.tildacdn.com/tild3665-3230-4434-b935-633637393264/IMG_7689_enfuse.jpg",
//   "https://static.tildacdn.com/tild3566-6663-4433-b566-306264376630/IMG_7668_enfuse.jpg",  
// ];

const img = {
  "base": [
    "https://static.tildacdn.com/tild6562-3235-4661-a365-343162313539/IMG_7662_enfuse.jpg",
    "https://static.tildacdn.com/tild6133-6564-4733-b764-356334626565/IMG_7683_enfuse.jpg",
    "https://static.tildacdn.com/tild3665-3230-4434-b935-633637393264/IMG_7689_enfuse.jpg",
    "https://static.tildacdn.com/tild3566-6663-4433-b566-306264376630/IMG_7668_enfuse.jpg",
  ],
  "cinema": [
    "https://static.tildacdn.com/tild3563-3665-4530-b366-323561643833/IMG_4536_enfuse.jpg",
    "https://static.tildacdn.com/tild3532-6466-4663-a365-306262323135/IMG_4542_enfuse.jpg",
    "https://static.tildacdn.com/tild3236-3030-4337-b134-353938346431/IMG_4548_enfuse.jpg",
    "https://static.tildacdn.com/tild3737-3830-4539-b337-656638366639/IMG_4554_enfuse.jpg",
  ],
  "playing": [
    "https://static.tildacdn.com/tild3132-3161-4333-b231-333762633966/IMG_7572_enfuse.jpg",
    "https://static.tildacdn.com/tild3565-6665-4265-b432-613235636139/IMG_7581_enfuse.jpg",
    "https://static.tildacdn.com/tild3765-6563-4861-a664-363535643364/IMG_7587_enfuse.jpg",
    "https://static.tildacdn.com/tild3061-3564-4364-a265-376235653838/IMG_7575_enfuse.jpg",
  ]
};

const name = {
  "base": "База",
  "cinema": "Кинозал",
  "playing": "Игровая"
}

interface RoomImageProps {
  room: "base" | "cinema" | "playing"
}

export const RoomImages = ({room}: RoomImageProps) => {
  const [currentIndex, setCurrentIndex] = useState(0);

  const handlePrev = () => {
    setCurrentIndex((prevIndex) => (prevIndex === 0 ? img[room].length - 1 : prevIndex - 1));
    setCurrentIndex((prevIndex) => (prevIndex === 0 ? img[room].length - 1 : prevIndex - 1));
  };

  const handleNext = () => {
    setCurrentIndex((prevIndex) => (prevIndex === img[room].length - 1 ? 0 : prevIndex + 1));
  };

  return (
    <div className={styles.reviewsContainer}>
      <button className={`${styles.arrow} ${styles.left}`} onClick={handlePrev}>‹</button>
      <div className={styles.reviewCard}>
        <img src={img[room][currentIndex]} width={650} height={350}></img>
        <p>{name[room]}</p>
      </div>
      <button className={`${styles.arrow} ${styles.right}`} onClick={handleNext}>›</button>
    </div>
  );
}

