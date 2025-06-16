
from django.http import JsonResponse

def products(request):
    return JsonResponse({
        "shoes": [{"name": "Running Shoes", "price": 50}, {"name": "Formal Shoes", "price": 80}],
        "watches": [{"name": "Smart Watch", "price": 120}, {"name": "Classic Watch", "price": 90}],
        "paintings": [{"name": "Landscape", "price": 200}, {"name": "Abstract", "price": 180}]
    })
