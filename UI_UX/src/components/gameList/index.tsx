import { MenuCell } from "../menuCell"
import styles from './Table.module.css';

interface TableTopsProps {
  game_class: "classic" | "mafia" | "imagination" | "thinking"
}

export const TableTops = ({game_class}: TableTopsProps) => {
  switch (game_class) {
    case "classic":
      return (
        <div className={styles.TableCellBorder}>
          <ul role='list' className={styles.activitiesContainer}>
            <MenuCell 
              img_src="https://www.toyway.ru/upload/iblock/17a/HASBRO%20B7512121.jpg3.jpg"
              name="Монополия"
              description="Игра, которая не нуждается в представление. Может как сплачить, так и разобщить вашу компанию."
            />
            <MenuCell 
              img_src="https://www.mosigra.ru/image/data/mosigra.product.main/559/218/DSC_7432.jpg"
              name="Мафия"
              description="Игра с огромным множеством ролей, где всё зависит от ваших наблюдательности и красноречия."
            />
          </ul>
        </div>
      );
    case "mafia":
      return (
        <div className={styles.TableCellBorder}>
          <ul role='list' className={styles.activitiesContainer}>
            <MenuCell 
              img_src="https://c.dns-shop.ru/thumb/st4/fit/760/600/aff760c323ab06ba4a0dde2cd10cce63/q93_2aed44b57bedc87a32aeea41be298da341488ec64120fce3ce6947fe448ad0d1.jpg"
              name="Гномы-вредители"
              description="Игроки делятся на две команды, и пока обычные гномы пытаются докопать до золота, вредители стараются им помешать."
            />
            <MenuCell 
              img_src="https://www.igroved.ru/db/games/images/39/2239/igroved_bang-the-duel_03.jpg"
              name="Бэнг"
              description="Бандиты стараются убить шерифа, пока он его помощники стараются помещать бандитам."
            />
          </ul>
        </div>
      );
    case "imagination":
      return (
        <div className={styles.TableCellBorder}>
          <ul role='list' className={styles.activitiesContainer}>
            <MenuCell 
              img_src="https://static.insales-cdn.com/files/1/3195/5737595/original/imaginarium-2.jpg"
              name="Имаджинариум"
              description="Игроки по очереди загадвают ассоциации на свои карточки и стараются отгадать их."
            />
            <MenuCell 
              img_src="https://www.researchgate.net/publication/332350197/figure/fig1/AS:746491564027914@1554988866561/Codenames-The-game-kit-and-Grid-arrangement.jpg"
              name="Codenames"
              description="Пока два капитана загадывают ассоциации, члены их команд пытаются понять, что вообще капитан имел в виду."
            />
          </ul>
        </div>
      );
    case "thinking":
      return (
        <div className={styles.TableCellBorder}>
          <ul role='list' className={styles.activitiesContainer}>
            <MenuCell 
              img_src="https://pronastolki.wordpress.com/wp-content/uploads/2019/03/dsc08868.jpg?w=656"
              name="Элементарно"
              description="Серия детективных историй, где ваша цель понять мотивы и восстановить ход преступления."
            />
            <MenuCell 
              img_src="https://www.mosigra.ru/image/cache/data/mosigra.product.main/549/230/DSC_3315-1024x1024-wm.webp"
              name="Cluedo"
              description="Кто-то где-то чем-то совершил преступление. Цель игрока - выяснить детали раньше других."
            />
          </ul>
        </div>
      );
  }
  
}