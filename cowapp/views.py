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

# Create your views here.

class Donation(APIView):
    def get(self, request,format = None):
        user = User.objects.all()
        srializer1 = UserSerializer(user, many = True)
        return Response(srializer1.data)

    def post (self, request, formate = None):
        data = request.data
        name = data["name"]
        contact = data["contact"]
        email = data["email"]
        address = data["address"]
        comment = data["comment"]
        amount = data["amount"]
        try:
            
            user = User.objects.get(contact=contact)
            amountfield = Amount_info.objects.create(user=user, amount=amount)
            return Response({"success":True, "message":"add amount"}, status=status.HTTP_201_CREATED)
            
        except:
            U = User.objects.create(name = name, contact = contact, email = email, address = address, comment = comment)
            amountfield = Amount_info.objects.create(user=U, amount=amount)
            return Response({"success":True}, status=status.HTTP_201_CREATED)
    
        
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



class Order_payment(APIView):
    def post(self, request,formate = None):
        data = request.data
        name = data['name']
        amount = data['amount']
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        razorpay_order = client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
        )
        id = razorpay_order["id"]
        order = Order.objects.create(
            name=name, amount=amount, provider_order_id=[id]
        )
        order.save()
        data_order_id={"order_ID":id}
        return Response(data_order_id)