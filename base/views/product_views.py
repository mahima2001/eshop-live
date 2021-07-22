from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes#permission class to allow only authorized users to login
from rest_framework.permissions import IsAuthenticated, IsAdminUser#for user and admin(Staff status is true)
from rest_framework.response import Response



from base.models import Product
from base.serializers import ProductSerializer
from rest_framework import status #to catch error if registered user tries to register again



@api_view(['GET'])#it gives permission to authorized users too
def getProducts(request):

    products = Product.objects.all()
    
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

