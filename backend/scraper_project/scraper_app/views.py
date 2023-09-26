import subprocess
from django.http import JsonResponse
from scraper_app.models import ScrapedProduct
from django.views.decorators.csrf import csrf_exempt
import subprocess
import json
import requests

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
        # Check if 'search_term' exists in the POST data
        if 'search_term' in request.POST:
            # Retrieve the search term from the POST data
            search_term = request.POST['search_term']

            # Trigger the Scrapy spider with the search term as a command-line argument
            spider_name = 'daraz'  # Replace with your actual spider name
            max_pages = 2  # Replace with your desired max pages

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