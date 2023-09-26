import React from "react";
import { FiSearch } from "react-icons/fi";
import { useState } from "react";
import axios from "axios";

const Navbar = () => {
  const [inputValue, setInputValue] = useState("");

  const handleSearch = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/search/", {
        search_term: inputValue, // Assuming inputValue contains your search term
      });

      // Check if the response status indicates success (e.g., 200 OK)
      if (response.status === 200) {
        // Handle the response data as needed
        const responseData = response.data.search_term;
        console.log(responseData);
        return responseData;
      } else {
        // Handle other response status codes (e.g., 4xx or 5xx errors)
        console.error("Request failed with status:", response.status);
        return null; // or throw an error
      }
    } catch (error) {
      // Handle network errors or other issues
      console.error("Error searching:", error);
      throw error; // You can re-throw the error or handle it differently
    }
  };

  return (
    <>
      <nav className="flex flex-row py-4 px-10 justify-between items-center shadow-md">
        <div className="text-2xl font-montserrat font-semibold">
          PriceWatcher-360
        </div>
        <div className="relative">
          <input
            type="text"
            name="search-product"
            id="search-product"
            className="block w-[600px] p-3 pl-10 pr-12 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 placeholder-gray-400"
            placeholder="Search for a product"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
          />
          <button
            onClick={handleSearch}
            className="absolute inset-y-0 right-0 px-3 py-2 bg-primary-color text-white rounded-r-lg hover:bg-secondary-color focus:outline-none"
          >
            Search
          </button>
          <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
            <FiSearch className="w-4 h-4 text-gray-500" />
          </div>
        </div>
        <div className="flex flex-row gap-3">
          <div className="login-button">
            <button
              type="button"
              className="bg-white text-black font-medium text-base border px-6 py-3 transition-all hover:bg-primary-color hover:text-white"
            >
              Log In
            </button>
          </div>
          <div className="signup-button">
            <button
              type="button"
              className="bg-primary-color text-white font-medium text-base border px-6 py-3 transition-all hover:bg-secondary-color"
            >
              Sign Up
            </button>
          </div>
        </div>
      </nav>
    </>
  );
};

export default Navbar;
