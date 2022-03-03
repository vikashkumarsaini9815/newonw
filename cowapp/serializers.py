from rest_framework import serializers
from cowapp.models import *


class Amount_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amount_info
        fields = ['id','amount','user']
       # fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    user=Amount_infoSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'name', 'contact', 'email', 'address', 'comment', 'amount', 'join_date', 'updated', 'user']
