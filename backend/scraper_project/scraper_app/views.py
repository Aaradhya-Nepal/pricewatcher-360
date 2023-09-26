from django.http import JsonResponse
from .models import ScrapedProduct

def get_data(request):
    data = ScrapedProduct.objects.all()
    serialized_data = serialize_data(data)
    return JsonResponse(serialized_data, safe=False)

def serialize_data(data):
    # Serialize your data into a format like JSON
    serialized_data = [{'field1': item.field1, 'field2': item.field2} for item in data]
    return serialized_data
