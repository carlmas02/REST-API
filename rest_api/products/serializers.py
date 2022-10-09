from rest_framework import serializers

from .models import *


class ProductSerializer(serializers.ModelSerializer):
    product_discount = serializers.SerializerMethodField(read_only=True)
    class Meta :
        model = Product
        # fields = ['title','sale_price']
        fields = ['title','content','price','sale_price','product_discount']

    
    def get_product_discount(self,obj):
        return obj.product_discount()