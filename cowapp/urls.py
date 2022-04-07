from django.urls import path
from .views import *
# from ilpapi import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path("donate_user/", Donation.as_view(), name='donation'),
    path("payment/", Order_payment.as_view(), name="payment"),
    path("paymenthandler/", Paymenthandler.as_view(), name="paymenthandler")   
    ]        
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 