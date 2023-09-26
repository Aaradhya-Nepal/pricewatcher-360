from django.http import JsonResponse
from scraper_app.models import ScrapedProduct
from django.views.decorators.csrf import csrf_exempt

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
            
            # Perform the search and prepare the response data
            # You can use the search_term variable here
            # For example, you can use it to search your database or scrape data
            # For now, let's create a sample response data
            data = {
                'results': [
                    {'title': 'Product 1', 'price': 10.99},
                    {'title': 'Product 2', 'price': 15.99},
                    # Add more results as needed
                ]
            }
            
            # Return the response data as JSON
            return JsonResponse(data)
        else:
            # If 'search_term' is not found in the POST data, return an error response
            return JsonResponse({'error': 'Missing search_term in POST data'})
    else:
        # Handle other HTTP methods or return an error response
        return JsonResponse({'error': 'Invalid request method'})
