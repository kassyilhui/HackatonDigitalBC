"""
Definition of models.
"""

from django.db import models

# Create your models here.
class user(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 40)
    password = models.CharField(max_length = 40)
    commercial_name = models.CharField(max_length = 40)
    city = models.CharField(max_length = 40)
    state = models.CharField(max_length = 40)
    district = models.CharField(max_length = 40)
    postal_code = models.CharField(max_length = 40)
    shipping_notes = models.CharField(max_length = 40)
    pos_lat = models.FloatField()
    pos_lon = models.FloatField()
    creation_date = models.DateField(auto_now=True)


    def __unicode__(self):
        return self.username

class type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 40)

    def __unicode__(self):
        return self.name

class product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    price = models.FloatField()
    type_id = models.ForeignKey(type)

    def __unicode__(self):
        return self.name

class inventory(models.Model):
    id = models.AutoField(primary_key=True)
    creation_date = models.DateField()
    user_id = models.ForeignKey(user)

class inventory_products(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(product)
    inventory_id = models.ForeignKey(inventory)
    creation_date = models.DateField()
    quantity = models.IntegerField()

class status(models.Model):
    id=models.AutoField(primary_key=True)
    description = models.CharField(max_length=40)

class order(models.Model):
    id = models.AutoField(primary_key=True)
    owner_user_id = models.ForeignKey(user,related_name='owner')
    requester_user_id = models.ForeignKey(user,related_name='requester')
    status_id = models.ForeignKey(status)
    creation_date = models.DateField()

class order_products(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(product)
    quantity = models.IntegerField()