
from rest_framework import serializers
from app.models import user,type,product,inventory_products

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = type
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    type_id = TypeSerializer()
    class Meta:
        model = product
        fields = '__all__'

class InventoryProductsSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer()
    class Meta:
        model = inventory_products
        fields = '__all__'