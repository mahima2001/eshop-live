from django.db.models import fields
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

from .models import Product, Order,ShippingAddress,OrderItem

class UserSerializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField(read_only=True)#return custom attributes; Django default user object has firstname and last name so me create a custom attribute name to store both
    _id=serializers.SerializerMethodField(read_only=True)
    isAdmin=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id','_id','username','email','name','isAdmin']
    def get__id(self,obj):#refer to JSON data and see the attributes, it has _id attribute
        return obj.id # creating an _id attribute that will value of id

    def get_isAdmin(self,obj):#refer to JSON data and see the attributes, it has _id attribute
        return obj.is_staff# is staff is already present we are just creating new attribute with same value

    def get_name(self,obj): #obj is user object which we wil pass when we will call the function
        name=obj.first_name #we store complete name in first name
        if name=='':
            name=obj.email
        return name

class UserSerializerWithToken(UserSerializer):
    token=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id','_id','username','email','name','isAdmin','token']
    def get_token(self,obj):
        token=RefreshToken.for_user(obj)#now we have two tokens one access token and refresh token(in frontend)
        return str(token.access_token)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):#relationship
    orderItems = serializers.SerializerMethodField(read_only=True)
    shippingAddress = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def get_orderItems(self, obj):
        items = obj.orderitem_set.all()
        serializer = OrderItemSerializer(items, many=True)# one to many
        return serializer.data

    def get_shippingAddress(self, obj):
        try:
            address = ShippingAddressSerializer(
                obj.shippingaddress, many=False).data #one to one: one order can have only one shipping address
        except:
            address = False
        return address

    def get_user(self, obj):
        user = obj.user
        serializer = UserSerializer(user, many=False)# one to one
        return serializer.data
