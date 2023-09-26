import "./App.css";
import Navbar from "./components/Navbar";
import ProductList from "./pages/ProductList";
import { useState } from "react";

function App() {
  return (
    <div>
      <Navbar />
      <ProductList />
    </div>
  );
}

export default App;
