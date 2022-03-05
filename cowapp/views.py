from django.shortcuts import render
from cowapp.models import *
from cowapp.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
import sys

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
            
        
            


