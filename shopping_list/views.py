from rest_framework import viewsets

from .serializers import ShoppingListSerializer, ListItemSerializer
from .models import ShoppingList, ListItem



class ShoppingListViewSet(viewsets.ModelViewSet):
    queryset = ShoppingList.objects.all().order_by('name')
    serializer_class = ShoppingListSerializer

class ListItemViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all().order_by('name')
    serializer_class = ListItemSerializer

class ItemsInListViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(shopping_list=self.request.query_params.get('access_code'))
        return query_set