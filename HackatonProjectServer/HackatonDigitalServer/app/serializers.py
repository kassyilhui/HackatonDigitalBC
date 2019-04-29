
from rest_framework import serializers
from app.models import user,product,inventory_products,order,order_products,inventory

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

class OrderSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return user.objects.create(**validated_data)

    owner_user_id = UserSerializer()
    requester_user_id = UserSerializer()

    class Meta:
        model = order
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    user_id = UserSerializer()
    class Meta:
        model = inventory
        fields = '__all__'

class InventoryProductsSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer()
    inventory_id = InventorySerializer()
    class Meta:
        model = inventory_products
        fields =  ('inventory_id', 'quantity','product_id')


class OrderProductsSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return user.objects.create(**validated_data)

    product_id = ProductSerializer()
    order_id = OrderSerializer()
    class Meta:
        model = order_products
        fields = '__all__'