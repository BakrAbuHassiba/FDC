from django.core.mail import send_mail
from django.core.cache import cache
from django.http import JsonResponse
from yahoo_fin import stock_info
from rest_framework import generics
from .models import Service, Project, News
from .serializer import ServiceSerializer, ProjectSerializer, NewsSerializer


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


class AllNews(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class News(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


def get_commodity_prices(request):
    # Try to get the prices from the cache to avoid too many API calls
    prices = cache.get('commodity_prices')

    if prices is None:
        try:
            # Fetch the live prices for WTI Crude, Brent Crude, and Natural Gas
            wti_price = stock_info.get_live_price("CL=F")
            brent_price = stock_info.get_live_price("BZ=F")
            natural_gas_price = stock_info.get_live_price("NG=F")

            # Format the prices with two decimal places
            prices = {
                "WTI_Crude": f"${round(wti_price, 2):.2f}",
                "Brent_Crude": f"${round(brent_price, 2):.2f}",
                "Natural_Gas": f"${round(natural_gas_price, 2):.2f}"
            }

            # Cache the result for 10 minutes (600 seconds)
            cache.set('commodity_prices', prices, timeout=600)
        except Exception as e:
            return JsonResponse
    return JsonResponse(prices)




import json
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def contact_form_submission(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data
            data = json.loads(request.body.decode('utf-8'))
            name = data.get('name')
            email = data.get('email')
            phone = data.get('phone')
            company = data.get('company')
            message = data.get('message')

            # Send email with the received data
            send_mail(
                subject=f"New Contact Form Submission from {name}",
                message=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nCompany: {company}\nMessage: {message}",
                from_email='daw@fdenergies.com',
                recipient_list=['daw@fdenergies.com'],
                fail_silently=False,
            )
            return JsonResponse({'status': 'success', 'message': 'Email sent successfully!'})
        
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data.'}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)


