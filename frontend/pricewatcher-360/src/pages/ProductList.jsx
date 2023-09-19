import React from "react";
import { BiFilter } from "react-icons/bi";
import { FiSearch } from "react-icons/fi";
import Card from "../components/Card";

const ProductList = () => {
  return (
    <>
      <div className="main-container p-4">
        <div className="border border-gray-300 rounded-lg p-4 mb-4">
          <div className="flex justify-between items-center mb-4">
            <div className="text-gray-400">
              Found 40 items for "Search Term"
            </div>
            <div className="flex justify-between items-center mb-4">
              <div className="flex items-center mr-4">
                <div className="relative">
                  <input
                    type="text"
                    name="search-product"
                    id="search-product"
                    className="block w-80 p-2 pl-10 text-sm text-gray-400 border border-gray-300 rounded-lg placeholder-gray-400"
                    placeholder="Search for a product"
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
          <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
            <Card />
            <Card />
            <Card />
            <Card />
            <Card />
          </div>
        </div>
      </div>
    </>
  );
};

export default ProductList;
