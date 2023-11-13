from rest_framework import serializers
from .models import PlaceOrder,Signup
class PlaceOrderSerilizer(serializers.ModelSerializer):
    class Meta:
        model = PlaceOrder
        fields = '__all__'

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = '__all__'
        