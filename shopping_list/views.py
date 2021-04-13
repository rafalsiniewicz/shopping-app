from rest_framework import viewsets

from .serializers import ShoppingListSerializer, ListItemSerializer
from .models import ShoppingList, ListItem


class ShoppingListViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all lists for all users. <br /> Endpoints: <br />
    - **/shopping-lists/?owner=<owner_id\>**:  returns lists for user with specified id
    """
    queryset = ShoppingList.objects.all().order_by('name')
    serializer_class = ShoppingListSerializer

    def get_queryset(self):
        queryset = self.queryset
        owner_id = self.request.query_params.get('owner')
        if owner_id is not None:
            queryset = queryset.filter(owner=owner_id)

        return queryset

class ItemsInListViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all items of all lists. <br /> Endpoints: <br />
    - **/items/?id=<shopping_list_id\>**:  returns items for shopping list with specified id
    """
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer

    def get_queryset(self):
        queryset = self.queryset
        item_id = self.request.query_params.get('id')
        if item_id is not None:
            queryset = queryset.filter(shopping_list=item_id)
        return queryset
