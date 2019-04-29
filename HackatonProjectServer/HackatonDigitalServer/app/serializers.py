
from rest_framework import serializers
from app.models import user,product,inventory_products

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return user.objects.create(**validated_data)

    class Meta:
        model = user
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'

class InventoryProductsSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer()
    class Meta:
        model = inventory_products
        fields = '__all__'