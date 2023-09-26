import React from "react";

const Card = ({ imageUrl, title, currentPrice, originalPrice, discount }) => {
  return (
    <div className="max-w-xs bg-white border border-gray-300 rounded-lg">
      <div className="p-2">
        <div
          className="aspect-w-2 aspect-h-3 relative"
          style={{
            height: "200px",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          {imageUrl ? (
            <img
              className="rounded-lg object-cover h-full"
              src={imageUrl}
              alt="Card Image"
            />
          ) : (
            <div className="bg-gray-200 h-full flex items-center justify-center">
              No image available
            </div>
          )}
        </div>
        <div className="p-3">
          <h5
            className="mb-2 text-xl font-semibold tracking-tight text-gray-900"
            style={{
              display: "-webkit-box",
              WebkitLineClamp: 2,
              WebkitBoxOrient: "vertical",
              overflow: "hidden",
              textOverflow: "ellipsis",
            }}
          >
            {title}
          </h5>
          <div className="flex items-center gap-2">
            <p className="text-green-600 font-semibold">{currentPrice}</p>
            <p className="text-gray-500 line-through">{originalPrice}</p>
            <p className="text-xs text-gray-600">{discount}</p>
          </div>
        </div>
        <a href="#">
          <button className="w-full bg-white hover:bg-primary-color hover:text-white text-black border border-gray-300 hover:border-primary-color px-3 py-2 rounded-md transition-all duration-200">
            View
          </button>
        </a>
      </div>
    </div>
  );
};

export default Card;
