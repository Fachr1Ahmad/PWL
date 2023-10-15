import { Outlet } from "react-router-dom";
import NavBar from "../components/NavBar";
import Footer from "../components/Footer";
import { ThemeProvider } from "../provider/themeProvider";
import { ScreenProvider } from "../provider/screenProvider";

const RootElement = () => {
  return (
    <ScreenProvider>
      <ThemeProvider>
        <NavBar />
        <Outlet />
        <Footer />
      </ThemeProvider>
    </ScreenProvider>
  );
};

export default RootElement;
