from rest_framework import serializers
from .models import Profile, CreditCard


class CreditCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = CreditCard
        fields = ('__all__')

class ProfileSerializer(serializers.ModelSerializer):
    user = CreditCardSerializer(read_only = True, many = True)

    class Meta:
        model = Profile
        fields = ('__all__')

        



    

  