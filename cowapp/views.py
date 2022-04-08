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
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

# Create your views here.

razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))



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
            razorpay_order = razorpay_client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"})
            order_ID = razorpay_order['id']
            order_data = Order.objects.create(user=user, amount=amount,provider_order_id=[order_ID])
            order_data.save()
            return_data = {"name":name, "contact":contact, "order_id":order_ID}
            return Response(return_data, status=status.HTTP_201_CREATED)
            
        except:
            U = User.objects.create(name = name, contact = contact, email = email, address = address, )
            razorpay_order = razorpay_client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"})
            order_ID = razorpay_order['id']
            order_data = Order.objects.create(user=U, amount=amount,provider_order_id=[order_ID])
            order_data.save()
            return_data1 = {"name":name, "contact":contact, "order_id":order_ID}
            return Response(return_data1, status=status.HTTP_201_CREATED)
    
        
        # user = User.objects.get(contact=contact)
        # amountfield = Amount_info.objects.create(user=user, amount=amount)
        # return Response({"success":True, "message":"add amount"}, status=status.HTTP_201_CREATED)


# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
# @csrf_exempt
# def paymenthandler(request):
 
#     # only accept POST request.
#     if request.method == "POST":
#         try:
           
#             # get the required parameters from post request.
#             payment_id = request.POST.get('razorpay_payment_id', '')
#             razorpay_order_id = request.POST.get('razorpay_order_id', '')
#             signature = request.POST.get('razorpay_signature', '')
#             params_dict = {
#                 'razorpay_order_id': razorpay_order_id,
#                 'razorpay_payment_id': payment_id,
#                 'razorpay_signature': signature
#             }
 
#             # verify the payment signature.
#             result = razorpay_client.utility.verify_payment_signature(
#                 params_dict)
#             if result is None:
#                 amount = 20000  # Rs. 200
#                 try:
 
#                     # capture the payemt
#                     razorpay_client.payment.capture(payment_id, amount)
 
#                     # render success page on successful caputre of payment
#                     return render(request, 'paymentsuccess.html')
#                 except:
 
#                     # if there is an error while capturing payment.
#                     return render(request, 'paymentfail.html')
#             else:
 
#                 # if signature verification fails.
#                 return render(request, 'paymentfail.html')
#         except:
 
#             # if we don't find the required parameters in POST data
#             return HttpResponseBadRequest()
#     else:
#        # if other than POST request is made.
#         return HttpResponseBadRequest()
            



class Paymenthandler(APIView):
    def post (self, request, formate = None):
        data = request.data
        try:
            razorpay_payment_id = data['razorpay_payment_id']
            razorpay_order_id = data['razorpay_order_id']
            razorpay_signature = data['razorpay_signature']
            params_dict = {
                    'razorpay_order_id': razorpay_order_id,
                    'razorpay_payment_id': razorpay_payment_id,
                    'razorpay_signature': razorpay_signature
                }

            
            try:
                # verify the payment signature.
                result = razorpay_client.utility.verify_payment_signature(
                    params_dict)
                print("check 1", result)
                if result is True:
                    
                    # data_save = Order.objects.create(user = od_id, payment_id= razorpay_payment_id, signature_id =  razorpay_signature)
                    return_data = {"success":"True","message":"Your payment is successfully"}
                    return Response(return_data, status=status.HTTP_201_CREATED)

                else :
                    return_data = {"success":"False", 'error': 'Something went wrong'}
                    return Response(return_data)

            except:

                return_data = {"success": False, "message":"SignatureVerificationError"}
                return Response(return_data)
        except:
            return_data = {"success": False,"message":"bad request"}
            return Response(return_data)
            
        



        

        