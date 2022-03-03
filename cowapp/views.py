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
        srializer = UserSerializer(user, many = True)
        return Response(srializer.data)

    def post (self, request, formate = None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Donation_api(APIView):
    def post(self, request, format = None):
        data = request.data
        mobile = data["contact"]
        amount = data["amount"]

        try:
            user = User.objects.get(contact=mobile)
            amountfield = Amount_info.objects.create(user=user, amount=amount)
            return Response({"success":True}, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            response={"exception_type":exc_type.__name__,"filename": exc_tb.tb_frame.f_code.co_filename,"error_line_no":exc_tb.tb_lineno,"message":"No such user"}
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)