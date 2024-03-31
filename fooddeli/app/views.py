from django.http import JsonResponse
from .models import Pricing

def calculate_price(request):
    total_distance = 12
    try:
        pricing = Pricing.objects.get(pk=1)
    except Pricing.DoesNotExist:
        return JsonResponse({'error': 'Pricing details not found'}, status=400)

    total_price = pricing.base_price
    if total_distance > pricing.base_distance_in_km:
        additional_distance = total_distance - pricing.base_distance_in_km
        if pricing.item.type == 'perishable':  # Access 'item' attribute of pricing object
            per_km_price = pricing.km_price_perishable
        else:
            per_km_price = pricing.km_price_non_perishable  # Corrected the assignment here
        total_price += additional_distance * per_km_price

    print(total_price)
    return JsonResponse({'total_price': total_price})
