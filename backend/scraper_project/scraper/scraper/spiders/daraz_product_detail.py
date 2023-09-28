import scrapy
from scrapy.selector import Selector
from selenium import webdriver
import json
import sys
import os
import asyncio
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from asgiref.sync import sync_to_async

# Assuming 'scraper_project' is the name of your Django project directory.
django_project_path = 'C:\\Users\\Aaradhya\\Documents\\Projects\\pricewatcher-360\\backend\\scraper_project'
sys.path.append(django_project_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'scraper_project.settings'
import django
django.setup()
from scraper_app.models import ProductDetail, ScrapedProduct

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

    @sync_to_async
    def save_to_database(self, product_data, scraped_link):
        scraped_product = ScrapedProduct.objects.get(link=scraped_link)
        product = ProductDetail(
            title=product_data['title'],
            brand=product_data['brand'],
            price=product_data['price'],
            delivery_info=product_data['delivery_info'],
            sold_by=product_data['sold_by'],
            positive_seller_ratings=product_data['positive_seller_ratings'],
            ship_on_time=product_data['ship_on_time'],
            chat_response_rate=product_data['chat_response_rate'],
            highlights=product_data['highlights'],
            brand_spec=product_data['brand_spec'],
            sku_spec=product_data['sku_spec'],
            image_links=product_data['image_links'],
            scraped_product_link=scraped_product,
        )
        product.save()

    async def parse(self, response):
        # Use Selenium to load the dynamic content
        driver = webdriver.Chrome()
        driver.get(response.url)

        # Wait for the page to load
        driver.implicitly_wait(5)

        # Use Scrapy Selector on the Selenium driver page source
        sel = Selector(text=driver.page_source)

        # Extract details from the product images block
        image_links = sel.css('.item-gallery__thumbnail-image::attr(src)').getall()

        # Extract other details with conditions
        title = sel.css('span.pdp-mod-product-badge-title::text').get() or 'NA'
        brand = sel.css('a.pdp-product-brand__brand-link::text').get() or 'NA'
        price = sel.css('span.pdp-price_type_normal::text').get() or 'NA'
        delivery_info = sel.css('.delivery-option-item_type_standard .delivery-option-item__title::text').get() or 'NA'
        sold_by = sel.css('.seller-name__detail-name::text').get() or 'NA'
        positive_seller_ratings = sel.css('.seller-info-value.rating-positive::text').get() or 'NA'
        ship_on_time = sel.css('.seller-info-value::text').get() or 'NA'
        chat_response_rate = sel.css('.seller-info-value::text').get() or 'NA'

        # Extract details from the product highlights section
        highlights = sel.css('.html-content.pdp-product-highlights ul li::text').getall() or ['NA']

        # Extract details from the specifications section
        brand_spec = sel.css('.specification-keys li:contains("Brand") .key-value::text').get() or 'NA'
        sku_spec = sel.css('.specification-keys li:contains("SKU") .key-value::text').get() or 'NA'

        # Close the Selenium driver
        driver.quit()

        # Create an instance of the Django model and save the data
        product_data = {
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

        await self.save_to_database(product_data, response.url)

if __name__ == '__main__':
    # Pass the URL as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <url>")
        sys.exit(1)

    url_to_scrape = sys.argv[1]

    # Create an asyncio event loop
    loop = asyncio.get_event_loop()

    # Use the loop to run the crawl process
    process = CrawlerProcess(settings=get_project_settings(), install_root_handler=False)

    # Run the crawl in the event loop
    asyncio.ensure_future(process.crawl(DarazSpider, start_urls=[url_to_scrape]))
    loop.run_until_complete(process.crawl(DarazSpider, start_urls=[url_to_scrape]))

    # This will also close the loop
    loop.close()
