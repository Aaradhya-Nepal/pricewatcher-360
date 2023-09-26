# scraper_project/scraper_app/management/commands/scrapy_crawl.py

import os
from django.core.management.base import BaseCommand
import subprocess

# os.environ['DJANGO_SETTINGS_MODULE'] = 'scraper_project.settings'

class Command(BaseCommand):
    help = 'Run a Scrapy spider'

    def add_arguments(self, parser):
        parser.add_argument('spider_name', type=str)
        parser.add_argument('--search_term', type=str, required=True)
        parser.add_argument('--max_pages', type=int, required=True)

    def handle(self, *args, **options):
        spider_name = options['spider_name']
        search_term = options['search_term']
        max_pages = options['max_pages']

        # Adjust the path to your Scrapy project's spider directory
        spider_directory = 'C:\\Users\\Aaradhya\\Documents\\Projects\\pricewatcher-360\\backend\\scraper_project\\scraper\\scraper\\spiders'

        # Run the Scrapy spider using subprocess
        subprocess.run([
            'scrapy',
            'crawl',
            'daraz',
            '-a',
            f'search_term={search_term}',
            '-a',
            f'max_pages={max_pages}'
        ], cwd=spider_directory)
