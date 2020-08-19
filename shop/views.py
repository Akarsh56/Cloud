# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Shop,Category,Product
from .Serializer import CategorySerializer,ProductSerializer, ShopSerializer
class shopView(APIView):

    def get(self,request,shop_id):
        category = Category.objects.filter(shop_id=shop_id)
        serializer = CategorySerializer(category, many=True)
        return Response({"ok": True, "category":serializer.data})

