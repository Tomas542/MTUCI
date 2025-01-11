import { MenuCell } from "../menuCell"
import styles from './Table.module.css';

interface FoodProps {
  food_class: "tea" | "snacks" | "beer"
}

export const Food = ({food_class}: FoodProps) => {
  switch (food_class) {
    case "tea":
      return (
        <div className={styles.TableCellBorder}>
          <ul role='list' className={styles.activitiesContainer}>
            <MenuCell 
              img_src="https://img.shop.rusteaco.ru/files/1/4274/27357362/original/romashkoviy-chay.jpg"
              name="Ромашковый чай"
              description="Расслабьтесь с приятным ромашковым чаем."
            />
            <MenuCell 
              img_src="https://teatrading.ru/wa-data/public/blog/img/strawberry_leaf_tea3-2.png"
              name="Клубничный чай"
              description="Почувствуйте вкус спелых ягод."
            />
            <MenuCell 
              img_src="https://img.shop.rusteaco.ru/files/1/7626/35757514/original/chay-s-chabrecom-1721814361762.jpg"
              name="Чай с чабрецом"
              description="Классический и такой знакомый для многих чай с чабрецом"
            />
          </ul>
        </div>
      );
    case "snacks":
      return (
        <div className={styles.TableCellBorder}>
          <ul role='list' className={styles.activitiesContainer}>
            <MenuCell 
              img_src="https://e2.edimdoma.ru/data/ingredients/0000/8259/8259-ed4_wide.jpg?1502378254"
              name="Кукурузные хлопья"
              description="Вкусный сухой завтрак, который вы можете съесть с молоком."
            />
            <MenuCell 
              img_src="https://dessert.ru/upload/iblock/bee/l6u5tuszxiwau0dxskl8gpxudvdi3ytv.jpg"
              name="Печенье американо"
              description="Вкуснейшнее шоколадное печенье."
            />
          </ul>
        </div>
      );
    case "beer":
      return (
        <div className={styles.TableCellBorder}>
          <ul role='list' className={styles.activitiesContainer}>
            <MenuCell 
              img_src="https://ivandamaria.rest/images/articles/082.webp"
              name="Светлое пиво"
              description="Без ярко выраженного вкуса солода."
            />
            <MenuCell 
              img_src="https://pivoug.ru/d/55073772_2.jpg"
              name="Тёмное пиво"
              description="Следка сладковатое с приятным послевкусием."
            />
          </ul>
        </div>
      );
  }
}