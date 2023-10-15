import React, { useContext, useEffect, useState } from "react";
import * as AiIcon from "react-icons/ai";
import { ThemeContext } from "../context/themeContext";

const InputName = ({ placeholder, textColor, onChange, value }) => {
  return (
    <>
      <div className="input-field with-icons">
        <AiIcon.AiOutlineUser size={16} />
        <input
          onChange={onChange}
          style={{
            color: textColor,
          }}
          type="text"
          name="nama"
          id="nama"
          value={value}
          placeholder={placeholder}
          required
        />
      </div>
    </>
  );
};

const InputEmail = ({ placeholder, textColor, onChange, value }) => {
  return (
    <>
      <div className="input-field with-icons">
        <AiIcon.AiOutlineMail size={16} />
        <input
          onChange={onChange}
          style={{
            color: textColor,
          }}
          type="text"
          name="email"
          id="email"
          value={value}
          placeholder={placeholder}
          required
        />
      </div>
    </>
  );
};

const InputMsg = ({ textColor, onChange, value }) => {
  return (
    <>
      <div className="container full-height">
        <textarea
          onChange={onChange}
          style={{
            color: textColor,
          }}
          id="messages"
          name="messages"
          value={value}
          required
        ></textarea>
      </div>
    </>
  );
};

const InputComponent = ({ type, placeholder, onChange, value }) => {
  const { theme } = useContext(ThemeContext);
  const [textColor, setTextColor] = useState("#222831");
  useEffect(() => {
    theme === "light" ? setTextColor("#222831") : setTextColor("#EEE2DE");
  }, [theme]);
  return (
    <>
      {type === "name" ? (
        <InputName
          onChange={onChange}
          placeholder={placeholder}
          textColor={textColor}
          value={value}
        />
      ) : type === "email" ? (
        <InputEmail
          onChange={onChange}
          placeholder={placeholder}
          textColor={textColor}
          value={value}
        />
      ) : type === "messages" ? (
        <InputMsg onChange={onChange} textColor={textColor} value={value} />
      ) : (
        "Input type unspecified"
      )}
    </>
  );
};

export default InputComponent;
