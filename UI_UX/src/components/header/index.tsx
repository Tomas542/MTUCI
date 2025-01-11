import styles from './HeaderSection.module.css';
import { Button } from '../headerButton';
import { useNavigate } from 'react-router-dom';


export const Header = () => {
  const navigate = useNavigate();
  
  const handleClickMain = () => {
    navigate('/');
  };

  const handleClickRooms = () => {
    navigate('/rooms');
  };
  
  const handleClickMenu = () => {
    navigate('/menu');
  };
  
  const handleClickGames = () => {
    navigate('/games');
  };

  return (
    <header className={styles.headerContainer}>
      <Button
        label="Главная"
        onClick={handleClickMain}
        color="dark-orange"
        size="medium"
      />
      <Button
        label="Залы"
        onClick={handleClickRooms}
        color="dark-orange"
        size="medium"
      />
      <Button
        label="Меню"
        onClick={handleClickMenu}
        color="dark-orange"
        size="medium"
      />
      <Button
        label="Настолки"
        onClick={handleClickGames}
        color="dark-orange"
        size="medium"
      />
    </header>
  );
}
