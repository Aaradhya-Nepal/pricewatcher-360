import scrapy
from scrapy.selector import Selector
from selenium import webdriver
import json

class DarazSpider(scrapy.Spider):
    name = 'detail_spider'
    start_urls = ['https://www.daraz.com.np/products/xiaomi-redmi-note-11-pro-5g-xiaomi-11i-hypercharge-5g-armor-ring-cover-shockproof-silicon-bumper-case-i127991597-s1035032825.html?search=1']

    def parse(self, response):
        # Use Selenium to load the dynamic content
        driver = webdriver.Chrome()
        driver.get(response.url)

        # Wait for the page to load
        driver.implicitly_wait(5)

        # Use Scrapy Selector on the Selenium driver page source
        sel = Selector(text=driver.page_source)

        # Extract the title using the provided class
        title = sel.css('span.pdp-mod-product-badge-title::text').get()

        # Close the Selenium driver
        driver.quit()

        # Save the data as a JSON file
        output_file = 'output.json'
        with open(output_file, 'w', encoding='utf-8') as json_file:
            data = {'title': title}
            json.dump(data, json_file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess

    process = CrawlerProcess()
    process.crawl(DarazSpider)
    process.start()
