from rest_framework import viewsets
from rest_framework.generics import UpdateAPIView
from .serializers import ShoppingListSerializer, ListItemSerializer
from .models import ShoppingList, ListItem
from rest_framework.response import Response
from rest_framework import status


class ShoppingListViewSet(viewsets.ModelViewSet):
    """
    <h3>Returns a list of all lists for all users. </h3><h4> Endpoints: </h4>
    <pre>
    - <b>/shopping-lists/?owner=&ltowner_id&gt</b>:   returns all lists for user with specified id
    - <b>/shopping-lists/?id=&ltid&gt</b>:            returns all lists with specified id
    - <b>/shopping-lists/?name=&ltname&gt</b>:        returns all lists with specified name
    - <b>/shopping-lists/edit/&ltid&gt</b>:           updates list with specified id
    </pre>
    <h4>Or any combination of above parameters (separated by ';'): </h4>
    <pre>
    - <b>/shopping-lists/?name=&ltname&gt;owner=&ltowner_id&gt;id=&ltid&gt</b>
    </pre>
    """
    queryset = ShoppingList.objects.all().order_by('name')
    serializer_class = ShoppingListSerializer
    FILTER_PARAMS = {'owner', 'name', 'id'}

    def get_queryset(self):
        queryset = self.queryset
        params_to_filter = {}
        for fp in self.FILTER_PARAMS:
            param = self.request.query_params.get(fp)
            if param is not None:
                params_to_filter[fp] = param

        queryset = queryset.filter(**params_to_filter)

        return queryset

    def put(self, request, pk):
        """
        Handles updating an object.
        """
        shopping_list = self.get_object(pk)
        serializer = ShoppingListSerializer(shopping_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditShoppingList(UpdateAPIView):
    queryset = ShoppingList.objects.all().order_by('name')
    serializer_class = ShoppingListSerializer
    # lookup_field = 'id'

class ItemsInListViewSet(viewsets.ModelViewSet):
    """
    <h3>Returns a list of all items of all lists.</h3><h4> Endpoints: </h4>
    <pre>
    - <b>/items/?id=&ltid&gt</b>:                              returns items with specified id
    - <b>/items/?name=&ltname&gt</b>:                          returns items with specified name
    - <b>/items/?content=&ltcontent&gt</b>:                    returns items with specified content
    - <b>/items/?shopping_list=&ltshopping_list_id&gt</b>:     returns items for shopping list with specified id
    - <b>/items/?is_bought=&ltis_bought&gt</b>:                returns items for with is_bought value (True/False)
    </pre>
    <h4>Or any combination of above parameters (separated by ';').</h4>
    """
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer
    FILTER_PARAMS = {'id', 'name', 'content', 'shopping_list', 'is_bought'}

    def get_queryset(self):
        queryset = self.queryset
        params_to_filter = {}
        for fp in self.FILTER_PARAMS:
            param = self.request.query_params.get(fp)
            if param is not None:
                params_to_filter[fp] = param

        queryset = queryset.filter(**params_to_filter)
        return queryset
