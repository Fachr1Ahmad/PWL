import { NavLink } from "react-router-dom";

export const NavigateButton = ({ text, target }) => {
  return (
    <div className="button-no-fill">
      <NavLink to={target}>{text}</NavLink>
    </div>
  );
};
