from django.contrib import admin
from .models import Category
from .models import Item
from .models import Order
from .models import ItemOrder

# Register your models here.
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(ItemOrder)
