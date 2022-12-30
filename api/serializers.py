from rest_framework import serializers
from .models import Products,ProductColor,ProductImage



class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = '__all__'
        
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    color = ProductColorSerializer(many=True, read_only = True)
    image = ProductImageSerializer(many=True, read_only = True)
    class Meta:
        model = Products
        fields = '__all__'
        

        
        