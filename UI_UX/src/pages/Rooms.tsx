import { Header } from "../components/header";
import { Slogan } from "../components/slogan";
import { InfoSection } from "../components/roomInfo";
import { RoomImages } from "../components/roomImages";
import { Footer } from "../components/footer";

import styles from "./Pages.module.css"

function Rooms() {
  return (
    <div className={styles.main}>
      <Header />
      <div className={styles.slogan}>
        <div style={{display: "flex", justifyContent: "center"}}>
          <Slogan 
            fontSize={"60px"} 
            text="просторные и уютные залы"
          />
        </div>
        <div>
          <Slogan 
            fontSize={"40px"}
            text="для больших и маленьких компаний"
          />
        </div>
      </div>
      <div className={styles.text}>
        <InfoSection />
        <h2>Залы</h2>
        <RoomImages 
          room="base"
        />
        <RoomImages 
          room="playing"
        />
        <RoomImages 
          room="cinema"
        />
      </div>
      <Footer />
    </div>
  );
}

export default Rooms;
