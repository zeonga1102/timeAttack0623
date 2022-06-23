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
      fields = ['delivery_address', 'order_date']


class ItemOrderSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    item_name = serializers.SerializerMethodField()
    def get_item_name(self, obj):
        return obj.item.name
    class Meta:
        model = ItemOrder
        fields = "__all__"
