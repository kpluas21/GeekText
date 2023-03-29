from django.shortcuts import render
from django.http import JsonResponse
from .models import Profile, CreditCard
from .serializers import ProfileSerializer, CreditCardSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getUser(request, username):
    user = Profile.objects.get(username = username)
    serializer = ProfileSerializer(user, many = False)
    return Response(serializer.data)

@api_view(['GET'])
def getUserList(request):
    userList = Profile.objects.all()
    serializer = ProfileSerializer(userList, many = True)
    return Response(serializer.data)


@api_view(['POST'])
def createUser(request):
    serializer = ProfileSerializer(data = request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT', 'PATCH'])
def updateUser(request, username):
    user = Profile.objects.get(username = username)
    serializer = ProfileSerializer(instance = user, data = request.data)
    for field, value in request.data.items():
        if field != 'email':
            setattr(user, field, value)   

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

    
@api_view(['POST'])
def addCreditCard(request, username):
    user = Profile.objects.get(username = username)
    serializer = CreditCardSerializer(instance = user, data = request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)        


@api_view(['GET'])
def listCreditCard(request, username):
    creditCardList = CreditCard.objects.filter(username = username)
    serializer = CreditCardSerializer(creditCardList, many = True)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteUser(request, username):
    user = Profile.objects.get(username = username)
    user.delete()
    return Response("User deleted")
   