from django.shortcuts import render, HttpResponse
from cowapp.models import *
from cowapp.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
import sys
import razorpay
from goshala import settings
import requests
import json

# Create your views here.

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))



class Order_payment(APIView):
    def get(self, request,format = None):
        user = User.objects.all()
        srializer1 = UserSerializer(user, many = True)
        return Response(srializer1.data)

    def post (self, request, formate = None):
        data = request.data
        name = data.get("name",None)
        contact = data.get("contact",None)
        if contact is None:
            return Response({"success": False,"message":"contact sould be nessery"},status=status.HTTP_204_NO_CONTENT)
        email = data.get("email",None)
        address = data.get("address",None)
        amount = data.get("amount",None)
        if amount is None:
            return Response({"success": False,"message":"amount sould be nessery"},status=status.HTTP_204_NO_CONTENT)
        
        try:            
            user = User.objects.get(contact=contact)
            razorpay_order = client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"})
            order_ID = razorpay_order['id']
            order_data = Order.objects.create(user=user, amount=amount,provider_order_id=[order_ID])
            order_data.save()
            return_data = {"name":name, "contact":contact, "order_id":order_ID}
            return Response(return_data, status=status.HTTP_201_CREATED)
            
        except:
            U = User.objects.create(name = name, contact = contact, email = email, address = address, )
            razorpay_order = client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"})
            order_ID = razorpay_order['id']
            order_data = Order.objects.create(user=U, amount=amount,provider_order_id=[order_ID])
            order_data.save()
            return_data1 = {"name":name, "contact":contact, "order_id":order_ID}
            return Response(return_data1, status=status.HTTP_201_CREATED)
    
        
        # user = User.objects.get(contact=contact)
        # amountfield = Amount_info.objects.create(user=user, amount=amount)
        # return Response({"success":True, "message":"add amount"}, status=status.HTTP_201_CREATED)
            
        
            





# def order_payment(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         amount = request.POST.get("amount")
        # client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        # razorpay_order = client.order.create(
        #     {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
        # )
#         print(razorpay_order)
#         order = Order.objects.create(
#             name=name, amount=amount, provider_order_id=payment_order["id"]
#         



# class Order_payment(APIView):
#     def post(self, request,formate = None):
#         data = request.data
#         name = data['name']
#         amount = data['amount']
#         client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
#         razorpay_order = client.order.create(
#             {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
#         )
#         id = razorpay_order["id"]
#         order = Order.objects.create(
#             name=name, amount=amount, provider_order_id=[id]
#         )
#         order.save()
#         data_order_id={"order_ID":id}
#         print(data_order_id)
#         return Response(data_order_id)

        

        