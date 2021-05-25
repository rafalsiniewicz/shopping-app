from django.test import TestCase
from shopping_list.models import ShoppingList, ListItem
from django.contrib.auth.models import User

# models test
class ShoppingListTest(TestCase):

    def create_shoppinglist(self, name="test"):
        user = User.objects.create()
        return ShoppingList.objects.create(name=name, owner=user)

    def test_shoppinglist_creation(self):
        sl = self.create_shoppinglist()
        self.assertTrue(isinstance(sl, ShoppingList))

    def test_shoppinglist_name(self):
        sl = self.create_shoppinglist()
        self.assertEqual(sl.__str__(), sl.name)

class ListItemTest(TestCase):

    def create_listitem(self, name="test", content="example content", is_bought=False):
        user = User.objects.create()
        shopping_list = ShoppingList.objects.create(name=name, owner=user)
        return ListItem.objects.create(name=name, content=content, is_bought=is_bought, shopping_list=shopping_list)

    def test_listitem_creation(self):
        sl = self.create_listitem()
        self.assertTrue(isinstance(sl, ListItem))

    def test_listitem_attributes_equal(self):
        sl = self.create_listitem()
        self.assertEqual(sl.__str__(), {sl.name, sl.content, sl.is_bought})

    def test_listitem_name_not_equal(self):
        sl = self.create_listitem()
        self.assertNotEqual(sl.__str__(), {"not proper name", sl.content, sl.is_bought})

    def test_listitem_content_not_equal(self):
        sl = self.create_listitem()
        self.assertNotEqual(sl.__str__(), {sl.name, "not proper content", sl.is_bought})

    def test_listitem_is_bought_not_equal(self):
        sl = self.create_listitem()
        self.assertNotEqual(sl.__str__(), {sl.name, sl.content, "not proper is_bought"})

class UserTest(TestCase):

    def create_user(self, username="user1", first_name="name", last_name="surname", email="example@example.com"):
        data = {"username": username, "first_name": first_name, "last_name": last_name, "email": email}
        return User.objects.create(**data)

    def test_user_creation(self):
        u = self.create_user()
        self.assertTrue(isinstance(u, User))

    def test_user_username(self):
        u = self.create_user()
        self.assertEqual(u.username, "user1")

    def test_user_first_name(self):
        u = self.create_user()
        self.assertEqual(u.first_name, "name")

    def test_user_last_name(self):
        u = self.create_user()
        self.assertEqual(u.last_name, "surname")

    def test_user_email(self):
        u = self.create_user()
        self.assertEqual(u.email, "example@example.com")


