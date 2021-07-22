from django.shortcuts import render
from rest_framework import serializers

from rest_framework.decorators import api_view, permission_classes#permission class to allow only authorized users to login
from rest_framework.permissions import IsAuthenticated, IsAdminUser#for user and admin(Staff status is true)
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from base.models import Product
from base.serializers import ProductSerializer,UserSerializer,UserSerializerWithToken
from django.contrib.auth.hashers import make_password
from rest_framework import status #to catch error if registered user tries to register again

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):#actual response of token comes from here so we customize this and add username and email
        data = super().validate(attrs)
        serializer=UserSerializerWithToken(self.user).data #we get serialized(JSON-dict) data here
        # when user tries to log in we get only userid and password ..we create userwithToken class and the user name and password and then we get all the other user details

        for k,v in serializer.items():
            data[k]=v
            #what its like:
            #data['username']=self.username
        return data

    

class MyTokenObtainPairView(TokenObtainPairView):#we inherit from the token
    serializer_class = MyTokenObtainPairSerializer#this is the serializer class that actually returns the user data
    #this class is created in the url so this gets called and we change the serializer that returns the token



@api_view(['GET']) 
@permission_classes([IsAdminUser])
def getUsers(request):#userroute-shows all users which only the admin should be able to see

    users = User.objects.all()
    
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

    
@api_view(['PUT'])#update
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)#We are not using the normal serializer, the one we did in neeche waala function coz we want to create a new token

    data = request.data
    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']

    if data['password'] != '':
        user.password = make_password(data['password'])

    user.save()

    return Response(serializer.data)




@api_view(['GET'])#when we wrap our function in this, Django lookes for a token rather than default authentication system
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user=request.user #in Django when a user is Logged in using that default authentication system you can get request.user to get logged in user dat
    serializer = UserSerializer(user, many=False)#Serialize the user
    return Response(serializer.data)

    
@api_view(['POST'])#we are ADDING new user
def registerUser(request):
    data=request.data
    try:
        user=User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])#hash password
        )
        serializer=UserSerializerWithToken(user,many=False)
        return Response(serializer.data)
    except:
        message={'detail':'User has already registered'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)