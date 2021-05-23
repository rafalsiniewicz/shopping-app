from django.test import TestCase
from shopping_list.models import ShoppingList, ListItem
from django.contrib.auth.models import User
from django.urls import reverse
from shopping_list import views


# models test
class ViewsShoppingListTest(TestCase):

    def create_shoppinglist(self, name="test"):
        user = User.objects.create()
        return ShoppingList.objects.create(name=name, owner=user)

    def test_shoppinglist_status(self):
        url = reverse('shoppinglist-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_shoppinglist_view(self):
        sl = self.create_shoppinglist()
        sl_resp = str({"id": sl.id, "name": sl.name, "owner": sl.owner.id}).replace(" ", "").replace("\'", "\"")
        url = reverse('shoppinglist-list')
        resp = self.client.get(url)
        self.assertIn(str(sl_resp), str(resp.content))


class ListItemTest(TestCase):

    def create_listitem(self, name="test", content="example_content", is_bought=False):
        user = User.objects.create()
        shopping_list = ShoppingList.objects.create(name=name, owner=user)
        return ListItem.objects.create(name=name, content=content, is_bought=is_bought, shopping_list=shopping_list)

    def test_listitem_status(self):
        url = reverse('listitem-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_listitem_view(self):
        li = self.create_listitem()
        li_resp = str({"id": li.id, "name": li.name, "content": li.content, "shopping_list": li.shopping_list.id,
                       "is_bought": li.is_bought}).replace(" ", "").replace("\'", "\"").replace("True", "true").replace(
            "False", "false")
        url = reverse('listitem-list')
        resp = self.client.get(url)
        # input(str(resp.content))
        self.assertIn(str(li_resp), str(resp.content))
