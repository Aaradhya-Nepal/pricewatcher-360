# scraper_project/scraper_app/management/commands/scrapy_crawl_another_spider.py

import os
from django.core.management.base import BaseCommand
import subprocess

class Command(BaseCommand):
    help = 'Run another Scrapy spider'

    def add_arguments(self, parser):
        # Add any custom arguments needed for your spider
        parser.add_argument('spider_name', type=str)
        parser.add_argument('--custom_argument', type=str, required=True)

    def handle(self, *args, **options):
        spider_name = options['spider_name']  # Corrected this line
        custom_argument = options['custom_argument']

        # Adjust the path to your Scrapy project's spider directory
        spider_directory = 'C:\\Users\\Aaradhya\\Documents\\Projects\\pricewatcher-360\\backend\\scraper_project\\scraper\\scraper\\spiders'

        # Run the Scrapy spider using subprocess
        subprocess.run([
            'scrapy',
            'crawl',
            spider_name,  # Use the provided spider_name argument
            '-a',
            f'custom_argument={custom_argument}',
        ], cwd=spider_directory)
