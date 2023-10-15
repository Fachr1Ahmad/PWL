import React, { useState } from "react";
import { ThemeContext } from "../context/themeContext";
export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState("light");

  const themeHandle = () => {
    setTheme((prevTheme) => (prevTheme === "light" ? "dark" : "light"));
  };
  return (
    <ThemeContext.Provider value={{ theme, themeHandle }}>
      {children}
    </ThemeContext.Provider>
  );
};
