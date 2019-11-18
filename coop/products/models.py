from django.db import models


class Producer(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created = models.DateTimeField('date created', default=None, blank=True, null=True)
    updated = models.DateTimeField('last updated', default=None, blank=True, null=True)
    ## should be linked to a user id model there... think about that later
    def __str__(self):
        return self.name

class Product(models.Model):
    unit_types = [
        ('UNIT', 'unit'),
        ('LB', 'pound'),
        ('CUP', 'cup'),
    ]

    name = models.CharField(max_length=200)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, default='')
    description = models.CharField(max_length=200)
    deleted = models.BooleanField
    created = models.DateTimeField('date created')
    updated = models.DateTimeField('last updated', default=None, blank=True, null=True)
    price_per_unit = models.IntegerField(default=0)
    unit_tye = models.CharField(
        max_length=4,
        choices = unit_types,
        default = 'UNIT'
    ) ## this is horrible. haha
    ammount = models.IntegerField
    # - Image
    # - Category

    def __str__(self):
        return self.name

# class Order(models.Model):
