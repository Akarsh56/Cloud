from rest_framework import serializers
from .models import Shop,Category,Product,Media

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['product_image']


class ProductSerializer(serializers.ModelSerializer):
    media = MediaSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id','product_name','media']



class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = ['id','category_name','product']



