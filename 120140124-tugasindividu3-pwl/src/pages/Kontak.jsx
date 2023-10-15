import { useContext, useEffect, useState } from "react";
import { ThemeContext } from "../context/themeContext";
import { SendButton } from "../components/Button";
import InputComponent from "../components/Input";
import dataDump from "../dump/data.dump";

const Kontak = () => {
  const { theme } = useContext(ThemeContext);
  const [date, setDate] = useState(new Date());

  const [input, setInput] = useState({
    nama: "",
    email: "",
    messages: "",
    sendAt: "",
  });

  useEffect(() => {
    setDate(new Date());
  }, []);

  useEffect(() => {
    setInput({
      nama: "",
      email: "",
      messages: "",
      sendAt: `${date.toLocaleTimeString("en-US", {
        formatMatcher: "best fit",
        hour: "2-digit",
        minute: "2-digit",
      })} | ${date.toLocaleString("id-ID", {
        dateStyle: "full",
      })}`,
    });
  }, [date]);

  const handleInput = (e) => {
    setInput({ ...input, [e.target.name]: e.target.value });
  };

  const handleSubmit = () => {
    try {
      dataDump.push(input);
    } catch (error) {
      console.log(error);
    } finally {
      alert("Berhasil mengirim pesan");
      setInput({
        nama: "",
        email: "",
        messages: "",
        sendAt: "",
      });
    }
  };

  return (
    <>
      <main className={theme}>
        <center><h1>Ada Pertanyaan? </h1></center>
        <div className="container item-center column full-width minimal-gap flex-full">
          <div className="container column half-width minimal-gap">
            <InputComponent
              type={"messages"}
              onChange={handleInput}
              value={input?.messages}
            />
             <div className="container column minimal-gap full-width">
              <InputComponent
                type={"name"}
                placeholder={"Nama Lengkap"}
                onChange={handleInput}
                value={input?.nama}
              />
              <InputComponent
                type={"email"}
                placeholder={"Email"}
                onChange={handleInput}
                value={input?.email}
              />
            </div>
          </div>
          <div className="container half-width">
            <SendButton actions={handleSubmit} />
          </div>
        </div>
      </main>
    </>
  );
};

export default Kontak;
