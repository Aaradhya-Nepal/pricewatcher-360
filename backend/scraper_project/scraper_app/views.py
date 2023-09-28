import subprocess
from django.http import JsonResponse
from scraper_app.models import ProductDetail, ScrapedProduct
from django.views.decorators.csrf import csrf_exempt
import subprocess
import json
import requests
from django.shortcuts import get_object_or_404
from django.core.serializers import serialize
from django.forms.models import model_to_dict

def get_data(request):
    data = ScrapedProduct.objects.all()
    serialized_data = serialize_data(data)
    response_data = {"data": serialized_data}
    return JsonResponse(response_data, safe=False)

def serialize_data(data):
    # Serialize your data into a list of dictionaries
    serialized_data = [
        {
            "pk": item.pk,
            "title": item.title,
            "current_price": item.current_price,
            "original_price": item.original_price,
            "discount": item.discount,
            "image": item.image,
            "link": item.link,
            "alt_text": item.alt_text,
            "location": item.location,
            "number_of_reviews": item.number_of_reviews,
        }
        for item in data
    ]
    return serialized_data

@csrf_exempt
def search_view(request):
    if request.method == 'POST':

        data = json.loads(request.body.decode('utf-8'))
        # Check if 'search_term' exists in the POST data
        search_term = data.get('search_term', '')

        if search_term:
            # Retrieve the search term from the POST data
            search_term = data['search_term']

            # Trigger the Scrapy spider with the search term as a command-line argument
            spider_name = 'daraz'
            max_pages = 2 

            spider_directory = 'C:\\Users\\Aaradhya\\Documents\\Projects\\pricewatcher-360\\backend\\scraper_project\\scraper\\scraper\\spiders'

            try:
                # Run the Scrapy spider using subprocess
                subprocess.run([
                    'scrapy',
                    'crawl',
                    spider_name,
                    '-a',
                    f'search_term={search_term}',
                    '-a',
                    f'max_pages={max_pages}'
                ], cwd=spider_directory)

                # You can customize the response based on the result of the spider if needed
                response_data = {
                    'message': 'Spider started successfully',
                    'search_term': search_term
                }

                # Return the response data as JSON
                return JsonResponse(response_data)
            except Exception as e:
                # Handle any errors that occur when running the spider
                return JsonResponse({'error': str(e)}, status=500)

        else:
            # If 'search_term' is not found in the POST data, return an error response
            return JsonResponse({'error': 'Missing search_term in POST data'})
    else:
        # Handle other HTTP methods or return an error response
        return JsonResponse({'error': 'Invalid request method'})

def scrape_product_data(request, product_id):
    try:
        # Retrieve the ScrapedProduct instance based on the product ID
        scraped_product = get_object_or_404(ScrapedProduct, pk=product_id)

        # Retrieve the product URL from the instance
        product_url = scraped_product.link

        # Check if data already exists in ProductDetail for the given link
        if not ProductDetail.objects.filter(scraped_product_link=scraped_product).exists():
            # Run the Scrapy spider using subprocess
            spider_directory = 'C:\\Users\\Aaradhya\\Documents\\Projects\\pricewatcher-360\\backend\\scraper_project\\scraper\\scraper\\spiders'
            subprocess.run([
                'scrapy',
                'crawl',
                'detail_spider',
                '-a',
                f'start_urls={product_url}'
            ], cwd=spider_directory, check=True)

        # Fetch the data from ProductDetail
        product_detail_instance = ProductDetail.objects.get(scraped_product_link=scraped_product)

        # Convert the model instance to a dictionary
        product_detail_data = model_to_dict(product_detail_instance)

        # Return the serialized data as JSON
        return JsonResponse({'status': 'success', 'data': product_detail_data})

    except ScrapedProduct.DoesNotExist:
        # Handle the case where the product ID is not found
        return JsonResponse({'error': 'Product not found'}, status=404)
    except ProductDetail.DoesNotExist:
        # Handle the case where the product detail data is not found
        return JsonResponse({'error': 'Product detail not found'}, status=404)
    except Exception as e:
        # Handle other exceptions
        return JsonResponse({'error': str(e)}, status=500)