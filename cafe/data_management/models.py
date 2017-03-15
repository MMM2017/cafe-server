from django.db import models
from django.contrib.auth.models import User


# Example: soup, drink, etc.
class TypeOfDish(models.Model):
    type = models.TextField(max_length=30)


class OrderStatus(models.Model):
    status = models.TextField(max_length=20)


class Role(models.Model):
    role_name = models.TextField(max_length=20)


class Worker(models.Model):
    account = models.ForeignKey(User)
    first_name = models.TextField(max_length=32)
    last_name = models.TextField(max_length=32)
    role = models.ForeignKey(Role)


class Dish(models.Model):
    title = models.TextField(max_length=128, default='')
    weight = models.FloatField(default=0.0)
    ingredients = models.TextField()
    price = models.FloatField(default=0.0)
    type = models.ForeignKey(TypeOfDish)


# Ready, Steady, GO
class StateOfOrderItem(models.Model):
    state = models.TextField(max_length=20)


class OrderItem(models.Model):
    state = models.ForeignKey(StateOfOrderItem)
    amount = models.SmallIntegerField(null=False, default=1)
    comment = models.TextField(max_length=255, null=True)
    cooker = models.ForeignKey(Worker)


class Order(models.Model):
    waiter = models.ForeignKey(Worker)
    status = models.ForeignKey(OrderStatus)
    price = models.FloatField(default=0.0)