import { Header } from "../components/header";
import { Slogan } from "../components/slogan";
import { InfoSection } from "../components/homeInfoCaffe";
import { Activities } from "../components/homeActivities";
import { Reviews } from "../components/homeReviews";
import { WhySection } from "../components/homeWhy";
import { Footer } from "../components/footer";
// import mySVG from "../../public/logo.svg"

import styles from "./Pages.module.css"

function Home() {
  return (
    <div className={styles.main}>
      <Header />
      <div className={styles.slogan}>
        <div style={{display: "flex", justifyContent: "center"}}>
          <Slogan 
            fontSize={"60px"} 
            text="вдвоём ещё по одной"
          />
        </div>
        <div>
          <Slogan 
            fontSize={"40px"}
            text="совмещаем приятное с приятным 🍻🃏"
          />
        </div>
      </div>
      <div className={styles.text}>
        <InfoSection />
        <h2>Время препровождение</h2>
        <Activities />
        <h2>Отзывы</h2>
        <Reviews />
        <h2>Почему именно мы?</h2>
        <WhySection />
      </div>
      <Footer />
    </div>
  );
}

export default Home;
