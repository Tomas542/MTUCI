import styles from './Activity.module.css';

interface ActivityProps {
  header_text: string;
  main_text: string;
  img_src: string;
}

export const Activity = ({ header_text, main_text, img_src }: ActivityProps) => {
  return (
    <li className={styles.activityContainer}>
      <div style={{
        display: "block"
      }}>
        <div style={{
          display: "table-cell",
          height: "100%",
          marginLeft: "0px",
          marginRight: "0px",
          boxSizing: "content-box"
        }}>
          <img src={img_src} alt=""></img>
        </div>
        <div style={{
          paddingLeft: "20px",
          display: "table-cell",
          width: "100%",
          height: "100%",
          verticalAlign: "top",
        }}>
          <div style={{
            display: "block",
            fontSize: "20px",
            fontWeight: 600,
          }}>
            {header_text}
          </div>
          <div style={{
            display: "block"
          }}>
            {main_text}
          </div>
        </div>
      </div>
    </li>
  );
};
