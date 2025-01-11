import styles from './Button.module.css';

interface ButtonProps {
  label: string;
  onClick: () => void;
  color?: 'blue' | 'red' | 'orange' | 'dark-orange';
  size?: 'small' | 'medium' | 'large';
}
export const Button = ({ label, onClick, color = 'orange', size = 'medium' }: ButtonProps) => {
  return (
    <button
    className={`${styles.btn} ${styles[`btn-${color}`]}
    ${styles[`btn-${size}`]}`}
    onClick={onClick}
    >
    {label}
    </button>
  );
};