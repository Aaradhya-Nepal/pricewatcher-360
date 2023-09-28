import React, { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";

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
        setScrapedData(scrapedData);
      } catch (error) {
        console.error("Error fetching scraped data:", error);
      }
    };

    fetchData();
  }, [productId]);

  return (
    <>
      <div className=""> Product Id: {productId}</div>
      <div>Hello this is product detail page</div>
    </>
  );
};

export default ProductDetail;
