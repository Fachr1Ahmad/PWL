import React, { useContext, useEffect, useState } from "react";
import { DirectButton, ScrollTop } from "../components/Button";
import { ThemeContext } from "../context/themeContext";
import {
  LayoutOFBeranda,
  LayoutOFTK,
  
} from "../components/Assets";


const Tentang = () => {
  const { theme } = useContext(ThemeContext);
  const [showScrollButton, setShowScrollButton] = useState(false);
  useEffect(() => {
    window.addEventListener("scroll", () => {
      window.scrollY > 300
        ? setShowScrollButton(true)
        : setShowScrollButton(false);
    });
  }, []);
  return (
    <>
      <main className={theme}>
        {showScrollButton && (
          <ScrollTop
            actions={() => {
              window.scrollTo({
                top: 0,
                behavior: "smooth",
              });
            }}
          />
        )}
       <div className="container column half-width minimal-gap content-container">

          <div className="container column half-width minimal-gap">
            <h2 id="komponenhalaman"> Tentang Itera</h2>
              <p>
                Institut Teknologi Sumatera, disingkat ITERA, adalah sebuah
                perguruan tinggi negeri yang terdapat di Provinsi Lampung di
                Pulau Sumatra. Lokasinya berada di antara wilayah Kabupaten
                Lampung Selatan dengan Kota Bandar Lampung.
              </p>

            <section>
              <h2>Sejarah</h2>
              <p>
                ITERA didirikan berdasarkan Peraturan Presiden Nomor 124 Tahun
                2014 tentang Pendirian Institut Teknologi Sumatera (Lembaran
                Negara Republik Indonesia Tahun 2014 Nomor 253) yang ditetapkan
                Presiden Republik Indonesia Dr. H. Susilo Bambang Yudhoyono pada
                tanggal 6 Oktober 2014 dan diundangkan tanggal 9 Oktober 2014.
                Walaupun peresmiannya dilaksanakan pada tahun 2014, tetapi ITERA
                sudah memulai kegiatan akademik dengan menerima mahasiswa baru
                sejak tahun 2012-2013. Selain ITB dan ITS, dengan dibukanya ITERA
                dan ITK, maka pemerintah Indonesia memiliki empat institut
                teknologi.
              </p>
              <div>
                <LayoutOFBeranda />
              </div>
            </section>
            <section>
              <h2>Strategi</h2>
              <p>
                Dalam konteks strategi utama pelaksanaan Masterplan Percepatan
                dan Perluasan Pembangunan Ekonom Indonesia (MP3EI), peran
                sumberdaya manusia yang berpendidikan menjadi kunci utama dalam
                mendukung pertumbuhan ekonomi yang berkesinambungan. Oleh karena
                itu, tujuan utama di dalam sistem pendidikan dan pelatihan untuk
                mendukung hal tersebut di atas haruslah bisa menciptakan
                sumberdaya manusia yang mampu beradaptasi dengan cepat terhadap
                perkembangan sains dan teknologi. Upaya percepatan pembangunan
                nasional, khususnya dalam bidang sains, teknologi dan seni,
                memerlukan kesiapan penyediaan sumberdaya manusia yang unggul.
                Untuk itu, Kementerian Pendidikan dan Kebudayaan memiliki program
                pendirian institut teknologi negeri di Pulau Sumatra.
              </p>
              <div>
                <LayoutOFTK />
              </div>
            </section>
          </div>
          <div className="container column half-width minimal-gap">
            <section>
            <div className="container row minimal-gap item-center" style={{ marginTop: 10, }}></div>
            </section>
          </div>
        </div>
      </main>
    </>
  );
};

export default Tentang;
