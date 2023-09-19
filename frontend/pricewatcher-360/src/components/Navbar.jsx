import React from "react";
import { FiSearch } from "react-icons/fi";

const Navbar = () => {
  return (
    <>
      <nav className="flex flex-row py-4 px-10 justify-between items-center shadow-md">
        <div className="text-2xl font-montserrat font-semibold">
          PriceWatcher-360
        </div>
        <div className="flex items-center">
          <div className="relative">
            <input
              type="text"
              name="search-product"
              id="search-product"
              className="block w-[600px] p-3 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 placeholder-gray-400"
              placeholder="Search for a product"
            />
            <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
              <FiSearch className="w-4 h-4 text-gray-500" />
            </div>
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
