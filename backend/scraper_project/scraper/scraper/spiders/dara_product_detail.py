import scrapy
from scrapy.selector import Selector
from selenium import webdriver
import json

class DarazSpider(scrapy.Spider):
    name = 'detail_spider'
    
    def __init__(self, *args, **kwargs):
        super(DarazSpider, self).__init__(*args, **kwargs)
        start_urls = kwargs.get('start_urls')
        if start_urls:
            # Add 'http://' if scheme is missing
            if not start_urls.startswith('http://') and not start_urls.startswith('https://'):
                start_urls = 'http://' + start_urls
            self.start_urls = [start_urls]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Use Selenium to load the dynamic content
        driver = webdriver.Chrome()
        driver.get(response.url)

        # Wait for the page to load
        driver.implicitly_wait(5)

        # Use Scrapy Selector on the Selenium driver page source
        sel = Selector(text=driver.page_source)

        # Extract details from the product images block
        image_links = sel.css('.item-gallery__thumbnail-image::attr(src)').getall()

        # Extract other details
        title = sel.css('span.pdp-mod-product-badge-title::text').get()
        brand = sel.css('a.pdp-product-brand__brand-link::text').get()
        price = sel.css('span.pdp-price_type_normal::text').get()
        delivery_info = sel.css('.delivery-option-item_type_standard .delivery-option-item__title::text').get()
        sold_by = sel.css('.seller-name__detail-name::text').get()
        positive_seller_ratings = sel.css('.seller-info-value.rating-positive::text').get()
        ship_on_time = sel.css('.seller-info-value::text').get()
        chat_response_rate = sel.css('.seller-info-value::text').get()

        # Extract details from the product highlights section
        highlights = sel.css('.html-content.pdp-product-highlights ul li::text').getall()

        # Extract details from the specifications section
        brand_spec = sel.css('.specification-keys li:contains("Brand") .key-value::text').get()
        sku_spec = sel.css('.specification-keys li:contains("SKU") .key-value::text').get()

        # Close the Selenium driver
        driver.quit()

        # Save the data as a JSON file
        output_file = 'output.json'
        with open(output_file, 'w', encoding='utf-8') as json_file:
            data = {
                'title': title,
                'brand': brand,
                'price': price,
                'delivery_info': delivery_info,
                'sold_by': sold_by,
                'positive_seller_ratings': positive_seller_ratings,
                'ship_on_time': ship_on_time,
                'chat_response_rate': chat_response_rate,
                'highlights': highlights,
                'brand_spec': brand_spec,
                'sku_spec': sku_spec,
                'image_links': image_links,
            }
            json.dump(data, json_file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    import sys

    # Pass the URL as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <url>")
        sys.exit(1)

    url_to_scrape = sys.argv[1]

    from scrapy.crawler import CrawlerProcess

    process = CrawlerProcess()
    process.crawl(DarazSpider, start_urls=[url_to_scrape])
    process.start()
