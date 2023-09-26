import React, { useState, useEffect } from "react";
import axios from "axios"; // Import Axios
import { BiFilter } from "react-icons/bi";
import { FiSearch } from "react-icons/fi";
import Card from "../components/Card";

const ProductList = () => {
  const [products, setProducts] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");

  const fetchData = async () => {
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/api/get_data/?search=${searchTerm}`
      );
      const responseData = response.data.data;
      setProducts(responseData);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="main-container p-4">
      <div className="border border-gray-300 rounded-lg p-4 mb-4">
        <div className="flex justify-between items-center mb-4">
          <div className="text-gray-400">
            Found {products.length} items for "{searchTerm}"
          </div>
          <div className="flex justify-between items-center mb-4">
            <div className="flex items-center mr-4">
              <div className="relative">
                <input
                  type="text"
                  name="search-product"
                  id="search-product"
                  className="block w-80 p-2 pl-10 text-sm text-gray-400 border border-gray-300 rounded-lg placeholder-gray-400"
                  placeholder="Search for a product from the list"
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                />
                <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                  <FiSearch className="w-4 h-4 text-gray-400" />
                </div>
              </div>
            </div>
            <button className="text-gray-500 border border-gray-300 px-12 py-1.5 rounded-md flex items-center gap-2 hover:bg-primary-color hover:text-white">
              <BiFilter size={20} />
              <span>Filter</span>
            </button>
          </div>
        </div>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {products.map((product) => (
            <Card
              key={product.pk}
              imageUrl={product.image}
              title={product.title}
              currentPrice={product.current_price}
              originalPrice={product.original_price}
              discount={product.discount}
            />
          ))}
        </div>
      </div>
    </div>
  );
};

export default ProductList;
