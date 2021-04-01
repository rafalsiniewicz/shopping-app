from rest_framework import serializers

from .models import ShoppingList, ListItem


class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ('id', 'name', 'owner')


class ListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListItem
        fields = ('id', 'name', 'content', 'shopping_list', 'is_bought')
