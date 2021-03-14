from django.db import models
import random,string


def gen_access_code():
    while True:
        code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        if ShoppingList.objects.filter(access_code=code).count() == 0:
            break;
    return code

class ShoppingList(models.Model):
    name = models.CharField(max_length=60)
    access_code = models.CharField(max_length=8, default=gen_access_code, primary_key=True)

    def __str__(self):
        return self.name

class ListItem(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    content = models.CharField(max_length=200)
    is_bought = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.name
