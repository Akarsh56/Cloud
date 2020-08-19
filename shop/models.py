# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Shop(models.Model):
    id = models.IntegerField(primary_key=True)
    shop_name = models.CharField(max_length=100)
    shop_location = models.CharField(max_length=32)

    def __str__(self):
        return self.id


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=100)
    parent_cat = models.CharField(max_length=32)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    @property
    def product(self):
        return self.product_set.all()

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    @property
    def media(self):
        return self.media_set.all()


class Media(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='Media/',null=True,blank=True)

    def __str__(self):
        return self.id
