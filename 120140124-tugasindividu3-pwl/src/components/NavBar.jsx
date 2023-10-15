import React, { useContext } from "react";
import * as FiIcon from "react-icons/fi";
import { NavLink } from "react-router-dom";
import { ThemeContext } from "../context/themeContext";

const NavBar = () => {
  const { theme, themeHandle } = useContext(ThemeContext);
  return (
    <>
      <nav>
        <div className="icon-container">          
        </div>
        <ul>
          <li>
            <NavLink to={"/"}>Beranda</NavLink>
          </li>
          <li>
            <NavLink to={"about"}>Tentang</NavLink>
          </li>
          <li>
            <NavLink to={"contact"}>Kontak</NavLink>
          </li>
          <li>
            <NavLink to={"result"}>Pesan</NavLink>
          </li>
         
        </ul>
      </nav>
    </>
  );
};

export default NavBar;
