from django.shortcuts import render
from django.db.models.query_utils import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from .models import Category, Item, Order
from .serializers import ItemSerializer, OrderSerializer

# Create your views here.
class ItemView(APIView):
    def get(self, request):
        category_name = request.data.get('category')
        category = Category.objects.get(name=category_name)
        items = Item.objects.filter(category=category)

        item_serializer = ItemSerializer(items, many=True).data

        return Response(item_serializer, status=status.HTTP_200_OK)

    def post(self, request):
        item_serializer = ItemSerializer(data=request.data)

        if item_serializer.is_valid():
            item_serializer.save()
            return Response({"message": "정상"}, status=status.HTTP_200_OK)
        
        return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderView(APIView):
    def get(self, request):
        time = datetime.datetime.now() - timedelta(days=7)
        id = request.data.get('order_id')
        query = Q(start_date__gt=time) & Q(id=id)
        orders = Order.objects.filter(query)
        order_Serializer = OrderSerializer(orders, many=True).data

        return Response(order_Serializer, status=status.HTTP_200_OK)
