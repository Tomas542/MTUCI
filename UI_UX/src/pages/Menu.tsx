import { Header } from "../components/header";
import { Slogan } from "../components/slogan";
import { InfoSection } from "../components/menuInfo";
import DropdownMenu from "../components/menuDropdown";
import { Footer } from "../components/footer";

import styles from "./Pages.module.css"

function Menu() {
  return (
    <div className={styles.main}>
      <Header />
      <div className={styles.slogan}>
        <div style={{display: "flex", justifyContent: "center"}}>
          <Slogan 
            fontSize={"60px"} 
            text="приятные мелочи жизни"
          />
        </div>
        <div>
          <Slogan 
            fontSize={"40px"}
            text="которыми так просто наслаждаться"
          />
        </div>
      </div>
      <div className={styles.text}>
        <InfoSection />
        <DropdownMenu 
          label="Чаи и кофе"
          default_open={true}
          food_class="tea"
        />
        <DropdownMenu
          label="Снеки"
          default_open={true}
          food_class="snacks"
        />
        <DropdownMenu
          label="Пенное"
          default_open={true}
          food_class="beer"
        />
      </div>
      <Footer />
    </div>
  );
}

export default Menu;
