from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import AllServices, Services, AllProjects, Project, get_oil_price

urlpatterns = [
    path('AllServices/', AllServices.as_view()),
    path('Services/<int:pk>', Services.as_view()),

    path('AllProjects/', AllProjects.as_view()),
    path('Project/<int:pk>', Project.as_view()),
    
    path('api/oil-price/', get_oil_price, name='get_oil_price'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
