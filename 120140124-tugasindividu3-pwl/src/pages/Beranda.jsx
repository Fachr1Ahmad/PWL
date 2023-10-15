import React, { useContext, useState } from "react";
import Header from "../components/Header";
import { Curious } from "../components/Assets";
import { ThemeContext } from "../context/themeContext";
import { AddButton, MinButton, ResetButton } from "../components/Button";
import { ScreenContext } from "../context/screenContenxt";

const Beranda = () => {
  const { theme } = useContext(ThemeContext);
  const { screenSize } = useContext(ScreenContext);
  const [number, setNumber] = useState(0);

  const increment = () => {
    setNumber(number + 1);
  };

  const decrement = () => {
    number > 0
      ? setNumber(number - 1)
      : alert(`Number already ${number}`);
  };

  const resetNumber = () => {
    number === 0 ? alert(`Number already ${number}`) : setNumber(0);
  };

  return (
    <>
      <Header />
      <main className={theme}>
        <div className="container row item-center" style={{ justifyContent: "center" }}>
          <div className="container column" style={{ textAlign: "center" }}>
            <Curious width={150} height={150} style={{ margin: '0 auto' }} />
            <h1>Itera Forest Campus</h1>
            <p>
              Institut Teknologi Sumatera, disingkat ITERA, adalah sebuah
              perguruan tinggi negeri yang terdapat di Provinsi Lampung di
              Pulau Sumatra. Lokasinya berada di antara wilayah Kabupaten
              Lampung Selatan dengan Kota Bandar Lampung.
            </p>
          </div>
        </div>
        <div className="container column full-width item-center minimal-gap">
          <h3 style={{ textAlign: "center" }}>
            Gunakan tombol di bawah untuk menambah atau mengurangi jumlah sesuai kebutuhan Anda. Tombol tambah akan menambah jumlah, tombol kurang akan menguranginya, dan tombol reset akan mengembalikan jumlah ke nol.
          </h3>
          <div className={`container row item-auto-space ${screenSize > 600 ? "half-width" : "full-width"}`}>
            <AddButton actions={increment} />
            <MinButton actions={decrement} />
          </div>
          <h1 style={{ marginBottom: 20 }}>{number}</h1>
          <ResetButton actions={resetNumber} />
        </div>

      </main>
    </>
  );
};

export default Beranda;
