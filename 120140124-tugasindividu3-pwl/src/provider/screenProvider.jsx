import { useEffect, useState } from "react";
import { ScreenContext } from "../context/screenContenxt";

export const ScreenProvider = ({ children }) => {
  const [screenSize, setScreenSize] = useState(window.innerWidth);

  useEffect(() => {
    const widthHandle = () => {
      setScreenSize(window.innerWidth);
    };
    window.addEventListener("resize", widthHandle);
    return () => {
      window.removeEventListener("resize", widthHandle);
    };
  }, []);
  return (
    <ScreenContext.Provider value={{ screenSize }}>
      {children}
    </ScreenContext.Provider>
  );
};
