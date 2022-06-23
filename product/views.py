from django.db.models.query_utils import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from .models import Item, ItemOrder
from .serializers import ItemSerializer, ItemOrderSerializer

# Create your views here.
class ItemView(APIView):
    def get(self, request):
        category = request.GET.get('category')
        items = Item.objects.filter(category__name=category)

        item_serializer = ItemSerializer(items, many=True).data

        return Response(item_serializer, status=status.HTTP_200_OK)

    def post(self, request):
        item_serializer = ItemSerializer(data=request.data)

        if item_serializer.is_valid():
            item_serializer.save()
            return Response({"message": "정상"}, status=status.HTTP_200_OK)
        
        return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemOrderView(APIView):
    def get(self, request):
        time = datetime.now() - timedelta(days=7)
        id = request.GET.get('order_id')
        query = Q(order__order_date__gt=time) & Q(order_id=id)
        item_orders = ItemOrder.objects.filter(query)
        item_order_Serializer = ItemOrderSerializer(item_orders, many=True).data

        return Response(item_order_Serializer, status=status.HTTP_200_OK)
