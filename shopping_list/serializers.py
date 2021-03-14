from rest_framework import serializers

from .models import ShoppingList, ListItem


class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ('name', 'access_code')

class ListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListItem
        fields = ('id', 'name', 'content', 'shopping_list', 'is_bought')