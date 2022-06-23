from rest_framework import serializers
from .models import Category
from .models import Item
from .models import Order
from .models import ItemOrder

class CategorytSerializer(serializers.ModelSerializer):
   class Meta:
      model = Category
      fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
   class Meta:
      model = Item
      fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
   class Meta:
      model = Order
      fields = "__all__"


class ItemOrderSerializer(serializers.ModelSerializer):
   class Meta:
      model = ItemOrder
      fields = "__all__"
