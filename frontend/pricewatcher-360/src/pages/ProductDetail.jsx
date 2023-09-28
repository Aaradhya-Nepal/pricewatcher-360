import React, { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";
import { Line } from "react-chartjs-2";

const ProductDetail = () => {
  const { productId } = useParams();
  const [scrapedData, setScrapedData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/api/scrape_data/${productId}/`
        );
        const scrapedData = response.data.data;
        console.log(scrapedData);
        setScrapedData(scrapedData);
      } catch (error) {
        console.error("Error fetching scraped data:", error);
      }
    };

    fetchData();
  }, [productId]);

  if (!scrapedData) {
    // Data is still loading
    return <div>Loading...</div>;
  }

  const { title, brand, price, delivery_info, image_links, highlights } =
    scrapedData;

  const chartData = {
    labels: ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"],
    datasets: [
      {
        label: "Price Fluctuation",
        data: [20, 25, 18, 30, 22], // Example data, replace with your actual data
        fill: false,
        borderColor: "rgba(75,192,192,1)",
        tension: 0.1,
      },
    ],
  };

  return (
    <>
      <section className="text-gray-700 body-font overflow-hidden bg-white">
        <div className="container px-5 py-24 mx-auto">
          <div className="lg:w-4/5 mx-auto flex flex-wrap">
            <img
              key={0}
              alt={`product-0`}
              src={image_links[0]}
              className="w-80 h-full object-cover object-center rounded border border-gray-200"
            />
            <div className="lg:w-1/2 w-full lg:pl-10 lg:py-6 mt-6 lg:mt-0">
              <h2 className="text-sm title-font text-gray-500 tracking-widest">
                {scrapedData.brand}
              </h2>
              <h1 className="text-gray-900 text-3xl title-font font-medium mb-1">
                {scrapedData.title}
              </h1>
              <p className="leading-relaxed">
                {Array.isArray(highlights)
                  ? highlights.map((highlight, index) => (
                      <span key={index}>{highlight}</span>
                    ))
                  : "No highlights available"}
              </p>
              <div className="flex">
                <span className="title-font font-medium text-2xl text-gray-900">
                  {scrapedData.price}
                </span>
                <a
                  href={scrapedData.scraped_product_link}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex ml-auto"
                >
                  <button className="flex ml-auto text-white bg-primary-color border-0 py-2 px-6 focus:outline-none hover:bg-secondary-color rounded">
                    Go to product page
                  </button>
                </a>
                <button className="rounded-full w-10 h-10 bg-gray-200 p-0 border-0 inline-flex items-center justify-center text-gray-500 ml-4">
                  <svg
                    fill="currentColor"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    className="w-5 h-5"
                    viewBox="0 0 24 24"
                  >
                    <path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"></path>
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
        {/* <Line data={chartData} /> */}
      </section>
    </>
  );
};

export default ProductDetail;
