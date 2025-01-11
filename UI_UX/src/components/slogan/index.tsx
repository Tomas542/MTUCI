import styles from './Slogan.module.css'

interface SloganProps {
  text:string;
  fontSize:number | string;
}

export const Slogan = ({ text, fontSize }:SloganProps) => {
  return (
    <p className={styles.slgn} style={{ fontSize , display:"inline"}} >
      {text}
    </p>
  );
}