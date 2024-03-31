from django.http import JsonResponse
from .models import Pricing
from rest_framework.decorators import api_view

@api_view(['POST'])
def calculate_price(request):

    organization_id = 1
    total_distance = 12
    zone = request.data.get('zone')
    organization_id = request.data.get('organization_id')
    total_distance = float(request.data.get('total_distance'))  # Convert to float
    item_type = request.data.get('item_type')


    try:
        pricing = Pricing.objects.get(pk=organization_id)
    except Pricing.DoesNotExist:
        return JsonResponse({'error': 'Pricing details not found'}, status=400)

    total_price = pricing.base_price
    if total_distance > pricing.base_distance_in_km:
        additional_distance = total_distance - pricing.base_distance_in_km
        if pricing.item.type == 'perishable':
            per_km_price = pricing.km_price_perishable
        else:
            per_km_price = pricing.km_price_non_perishable
        total_price=float(additional_distance)*float(per_km_price)
        total_price+=float(pricing.base_price)

    return JsonResponse({'total_price': total_price})
