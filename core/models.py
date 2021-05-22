from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

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


class About(models.Model):
    about_text = RichTextUploadingField()
    
    def __str__(self):
        return self.about_text


class Faq(models.Model):
    faq_text = RichTextUploadingField(blank=True, null=True,)
    
    def __str__(self):
        return self.faq_text
        

class Privacy_policy(models.Model):
    privacy_policiy_text = RichTextUploadingField(blank=True, null=True,)
    
    def __str__(self):
        return self.privacy_policiy_text



class Shipping_returns(models.Model):
    shipping_returns_text = RichTextUploadingField(blank=True, null=True,)
    
    def __str__(self):
        return self.shipping_returns_text
    


class Terms_of_use(models.Model):
    terms_of_use_text = RichTextUploadingField(blank=True, null=True,)
    
    def __str__(self):
        return self.terms_of_use_text