from rest_framework import serializers
from .models import Profile, CreditCard

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'password', 'name', 'email', 'address']


class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ('user', 'card_number', 'exp_date', 'cvv')

