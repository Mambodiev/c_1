from cart.models import Product
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from cart.models import Product

User = get_user_model()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email


def post_save_user_receiver(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)


post_save.connect(post_save_user_receiver, sender=User)


class Carousel(models.Model):
    carousel_image = models.ImageField()
    carousel_logo_slider = models.ImageField()
    carousel_title = models.CharField(max_length=100, blank=True)
    carousel_sub_title = models.CharField(max_length=100)
    carousel_action = models.CharField(max_length=100) or models

    def __str__(self):
        return self.carousel_title
