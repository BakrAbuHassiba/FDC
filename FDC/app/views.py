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


def contact_form_submission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        company = request.POST.get('company')
        message = request.POST.get('message')

        send_mail(
            subject=f"New Contact Form Submission from {name}",
            message=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nCompany: {company}\nMessage: {message}",
            from_email='daw@fdenergies.com',  # Replace with your sender email
            # Email where the message will be sent
            recipient_list=['daw@fdenergies.com'],
            fail_silently=False,
        )
        return JsonResponse({'status': 'success', 'message': 'Email sent successfully!'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)
