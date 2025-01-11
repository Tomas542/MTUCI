import { useState } from "react";
import { Food } from "../menuFood";

import styles from "./Dropdown.module.css";


interface DropdownButtonProps {
  label: string
  default_open: boolean
  food_class: "tea" | "snacks" | "beer"
}

export default function DropdownMenu({food_class, label = "Click me!", default_open = false}: DropdownButtonProps) {
  const [dropdownState, setDropdownState] = useState({ open: default_open});

  const handleDropdownClick = () => {
    setDropdownState({ open: !dropdownState.open});
  }

return (
  <div className={styles.container}>
    <button
      type="button"
      className={styles.button}
      onClick={handleDropdownClick}
      >
      {label} {dropdownState.open ? "🡣" : "🡢"}
    </button>
  {dropdownState.open && (
    <div className={styles.dropdown}>
      <Food food_class={food_class}/>
    </div>
  )}
  </div>
  );
}
