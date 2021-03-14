from django.contrib import admin
from .models import ShoppingList, ListItem


admin.site.register(ShoppingList)
admin.site.register(ListItem)