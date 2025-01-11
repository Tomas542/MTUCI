import { Header } from "../components/header";
import { Slogan } from "../components/slogan";
import { InfoSection } from "../components/roomInfo";
import DropdownGames from "../components/gameDropdown";
import { Footer } from "../components/footer";

import styles from "./Pages.module.css"

function Games() {
  return (
    <div className={styles.main}>
      <Header />
      <div className={styles.slogan}>
        <div style={{display: "flex", justifyContent: "center"}}>
          <Slogan 
            fontSize={"60px"} 
            text="на любой вкус и цвет"
          />
        </div>
        <div>
          <Slogan 
            fontSize={"40px"}
            text="более 100 игр в нашей коллекци"
          />
        </div>
      </div>
      <div className={styles.text}>
        <InfoSection />
        <DropdownGames 
          label="Классические игры"
          default_open={false}
          game_class="classic"
        />
        <DropdownGames 
          label="Похожие на мафию"
          default_open={false}
          game_class="mafia"
        />
        <DropdownGames 
          label="Требующие воображения"
          default_open={false}
          game_class="imagination"
        />
        <DropdownGames
          label="На подумать"
          default_open={false}
          game_class="thinking"
        />
        <h2>И много много ещё...</h2>
      </div>
      <Footer />
    </div>
  );
}

export default Games;
