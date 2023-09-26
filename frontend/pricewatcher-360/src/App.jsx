import "./App.css";
import Navbar from "./components/Navbar";
import ProductList from "./pages/ProductList";
import { useState } from "react";

function App() {
  const [searchTerm, setSearchTerm] = useState("");

  return (
    <div>
      <Navbar onSearch={(searchQuery) => setSearchTerm(searchQuery)} />
      <ProductList searchTerm={searchTerm} />
    </div>
  );
}

export default App;
