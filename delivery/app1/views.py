from django.http import JsonResponse
from .models import Pricing
# Create your views here.
def calculate_price(request):
    data = request.data
    zone = data.get('zone')
    organization_id = data.get('organization_id')
    total_distance = data.get('total_distance')
    item_type = data.get('item_type')


    try:
        pricing =  Pricing.objects.get(organization_id=organization_id,zone=zone)
    except Pricing.DoesNotExist:
        return  JsonResponse({'error':'Pricing details not found'})

    total_price = pricing.base_price
    if total_price>pricing.base_distance_in_km:
        additional_distance = total_distance-pricing.base_distance_in_km
        per_km_price =  pricing.km_price_perishable if item_type == 'perishable' else pricing.km_price_non_perishable
        total_price += additional_distance*per_km_price

        total_price *=100

        return JsonResponse({'total_price':total_price})
    else:
        return JsonResponse({'error':'HTTP_400_BAD_REQUEST'})


