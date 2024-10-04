from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import AllServices, Services, AllProjects, Project, get_commodity_prices, AllNews, News, contact_form_submission

urlpatterns = [
    path('AllServices/', AllServices.as_view()),
    path('Services/<int:pk>', Services.as_view()),

    path('AllProjects/', AllProjects.as_view()),
    path('Project/<int:pk>', Project.as_view()),

    path('AllNews/', AllNews.as_view()),
    path('News/<int:pk>', News.as_view()),

    path('oil-price/', get_commodity_prices, name='get_oil_price'),

    path('submit-contact-form/', contact_form_submission,
         name='submit-contact-form'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
