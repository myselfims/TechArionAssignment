from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from .models import Products
from rest_framework.response import Response
from .serializers import ProductsSerializer

# Create your views here.

class ProductsApi(viewsets.ModelViewSet):
    pagination_class = LimitOffsetPagination
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    

class ProductDetail(APIView):
    # pagination_class = LimitOffsetPagination
    def get(self, request, id=None):
        
        if id is not None:
            model = Products.objects.get(id=id)
            ser = ProductsSerializer(model)
            return Response(ser.data)
        models = Products.objects.all()
        ser = ProductsSerializer(models, many = True)
        return Response(ser.data)