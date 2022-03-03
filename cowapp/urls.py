from django.urls import path
from .views import *
# from ilpapi import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("donate_user/", Donation.as_view(),name='donation'),
    path("donate/", Donation_api.as_view(),name='donation_api'),
    
    ]        
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 