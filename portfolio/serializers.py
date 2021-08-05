from rest_framework import serializers
from .models import Customer, Investment, Stock, CustomUser


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer

        fields = ('pk', 'name', 'address', 'cust_number', 'city', 'state', 'zipcode', 'email', 'cell_phone')



class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = (
        'pk', 'customer', 'category', 'cust_number', 'description', 'acquired_value', 'acquired_date', 'recent_value', 'recent_date')


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('pk', 'customer', 'cust_number', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date')

from django.contrib.auth import get_user_model

User = get_user_model()

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
   class Meta:
       model = CustomUser
       fields = '__all__'
       extra_kwargs = {
           'password': {'write_only': True},
       }

   def create(self, validated_data):
       print("VALIDATED DATA")
       print(validated_data)
       customuser = CustomUser.objects.create_user(
           validated_data['username'],
           password=validated_data['password'],
       )
       return customuser

# User serializer
class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ('pk', 'username',)
