import time
import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import argparse


class DarazSpider(scrapy.Spider):
    name = "daraz"
    start_urls = ["https://www.daraz.com.np"]

    def __init__(self, search_term=None, max_pages=1, *args, **kwargs):
        super(DarazSpider, self).__init__(*args, **kwargs)
        self.search_term = search_term
        self.max_pages = int(max_pages)

    def parse(self, response):
        search_term = getattr(self, "search_term", None)
        if not search_term:
            self.logger.error(
                "Please provide a search term using '-a search_term=your_search_query'."
            )
            return

        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)

        try:
            driver.get(self.start_urls[0])
            time.sleep(5)

            # Find and interact with the search bar
            search_bar = driver.find_element(
                By.CSS_SELECTOR, ".search-box__input--O34g"
            )
            search_bar.send_keys(search_term)
            search_bar.send_keys(Keys.RETURN)

            product_data = []  # Store product data for this page

            # Function to scroll and load more products
            def load_more_products():
                while True:
                    products_count = len(
                        driver.find_elements(By.CSS_SELECTOR, ".gridItem--Yd0sa")
                    )
                    driver.execute_script("window.scrollBy(0, window.innerHeight);")
                    time.sleep(2)  # Adjust the delay as needed

                    new_products_count = len(
                        driver.find_elements(By.CSS_SELECTOR, ".gridItem--Yd0sa")
                    )
                    if new_products_count == products_count:
                        break

            # Function to scrape a single page of products
            def scrape_page():
                page_number = 1  # Track the current page number

                while page_number <= self.max_pages:
                    # Wait for the search results to load
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, ".gridItem--Yd0sa")
                        )
                    )

                    # Scroll and load all products
                    load_more_products()

                    # Extract data from the grid directly using Selenium
                    product_elements = driver.find_elements(
                        By.CSS_SELECTOR, ".gridItem--Yd0sa"
                    )

                    for product_element in product_elements:
                        title_element = product_element.find_element(
                            By.CSS_SELECTOR, ".title--wFj93"
                        )
                        title = title_element.text

                        try:
                            current_price_element = product_element.find_element(
                                By.CSS_SELECTOR, ".price--NVB62 .currency--GVKjl"
                            )
                            current_price = current_price_element.text
                        except Exception as e:
                            # Handle the case when no data is found
                            current_price = "N/A"
                        try:
                            original_price_element = product_element.find_element(
                                By.CSS_SELECTOR, ".origPrice--AJxRs .currency--GVKjl"
                            )
                            original_price = original_price_element.text
                        except Exception as e:
                            # Handle the case when no data is found
                            original_price = "N/A"
                        try:
                            discount_element = product_element.find_element(
                                By.CSS_SELECTOR, ".discount--HADrg"
                            )
                            discount = discount_element.text
                        except Exception as e:
                            # Handle the case when no data is found
                            discount = "N/A"

                        anchor_element = product_element.find_element(
                            By.CSS_SELECTOR, "a"
                        )
                        link = anchor_element.get_attribute("href")

                        image_element = anchor_element.find_element(
                            By.CSS_SELECTOR, ".image--WOyuZ"
                        )
                        image = image_element.get_attribute("src")
                        alt_text = image_element.get_attribute("alt")

                        location_element = product_element.find_element(
                            By.CSS_SELECTOR, ".location--eh0Ro"
                        )
                        location = location_element.text

                        try:
                            rating_element = product_element.find_element(
                                By.CSS_SELECTOR, ".rating--ZI3Ol.rate--DCc4j"
                            )
                            number_of_reviews_element = rating_element.find_element(
                                By.CSS_SELECTOR, ".rating__review--ygkUy"
                            )
                            number_of_reviews = number_of_reviews_element.text.replace(
                                "(", ""
                            ).replace(")", "")
                        except:
                            number_of_reviews = "NA"

                        product_data.append(
                            {
                                "title": title,
                                "current_price": current_price,
                                "original_price": original_price,
                                "discount": discount,
                                "image": image,
                                "link": link,
                                "alt_text": alt_text,
                                "location": location,
                                "number_of_reviews": number_of_reviews,
                            }
                        )

                    # Go to the next page if available
                    if page_number < self.max_pages:
                        try:
                            next_page_button = driver.find_element(
                                By.CSS_SELECTOR, ".ant-pagination-next"
                            )
                            if (
                                "ant-pagination-disabled"
                                in next_page_button.get_attribute("class")
                            ):
                                return False  # No more pages to scrape
                            next_page_button.click()
                            page_number += 1

                            # Wait for the new page to load
                            WebDriverWait(driver, 20).until(
                                EC.staleness_of(product_elements[0])
                            )
                            WebDriverWait(driver, 20).until(
                                EC.presence_of_element_located(
                                    (By.CSS_SELECTOR, ".gridItem--Yd0sa")
                                )
                            )
                            time.sleep(
                                5
                            )  # Adjust the delay as needed to ensure the next page loads
                        except Exception as e:
                            return False  # No more pages to scrape or an error occurred
                    else:
                        return False  # Reached the maximum number of pages

                return True

            # Scrape products from all pages
            scrape_page()

            # Save the data as a JSON file
            with open("daraz_products.json", "w", encoding="utf-8") as json_file:
                json.dump(product_data, json_file, ensure_ascii=False, indent=4)

        except Exception as e:
            self.logger.error(f"An error occurred: {str(e)}")

        finally:
            driver.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Daraz Scraper")
    parser.add_argument(
        "-s", "--search_term", type=str, required=True, help="Search term for products"
    )
    parser.add_argument(
        "-p", "--max_pages", type=int, required=True, help="Number of pages to scrape"
    )
    args = parser.parse_args()

    scrapy_args = [
        "crawl",
        "daraz",
        "-a",
        f"search_term={args.search_term}",
        "-a",
        f"max_pages={args.max_pages}",
    ]

    scrapy.cmdline.execute(scrapy_args)
