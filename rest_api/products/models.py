from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 120)
    content = models.TextField(blank=True,null=True)
    price = models.IntegerField()

    @property
    def sale_price(self):
        return self.price + 10

    def product_discount(self):
        return self.price - 10