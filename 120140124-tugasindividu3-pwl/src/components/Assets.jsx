import React from "react";
import Itera from "../assets/Logo_ITERA.png";
import layoutofberanda from "../assets/Layout of beranda.png";
import layoutoftentangandkontak from "../assets/Layout of tentang and kontak.png";

export const Curious = ({ width }) => {
  return (
    <>
      <a href="https://www.itera.ac.id/"target="_blank"rel="noreferrer">
      <img 
        width={width == null ? 300 : width}
        height={width == null ? 300 : width}
        src={Itera}
        alt="Logo_ITERA.png"
        style={{
          borderRadius: "50%",  
          border: "2px solid #000",  
        }}
      />

      </a>
    </>
  );
};
export const LayoutOFBeranda = () => {
  return (
    <>
      <img
        className="full-width"
        src={layoutofberanda}
        alt="Layout of beranda.png"
      />
    </>
  );
};
export const LayoutOFTK = () => {
  return (
    <>
      <img
        className="full-width"
        src={layoutoftentangandkontak}
        alt="Layout of tentang and kontak.png"
      />
    </>
  );
};

