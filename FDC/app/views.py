from django.core.cache import cache
from django.http import JsonResponse
from yahoo_fin import stock_info
from rest_framework import generics
from .models import Service,Project
from .serializer import ServiceSerializer, ProjectSerializer


class AllServices(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class Services(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class AllProjects(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class Project(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


def get_oil_price(request):
    # Try to get the oil price from the cache
    oil_price = cache.get('oil_price')

    if oil_price is None:
        try:
            # Fetch the current price of WTI crude oil
            price = stock_info.get_live_price("CL=F")
            # Format the price to two decimal places
            formatted_price = f"${round(price, 2):.2f}" #to add $
            # formatted_price = round(price, 2)  # or you can use f"{price:.2f}"

            oil_price = {
                "oil_price": formatted_price,
                "currency": "USD",
            }
            # Cache the result for 10 minutes (600 seconds)
            cache.set('oil_price', oil_price, timeout=600)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse(oil_price)
