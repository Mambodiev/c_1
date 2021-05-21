from django.contrib import admin
from .models import Customer, Carousel, Terms_of_use, Faq, About, Shipping_returns


admin.site.register(Customer)
admin.site.register(Carousel)
admin.site.register(About)
admin.site.register(Faq)
admin.site.register(Terms_of_use)
admin.site.register(Shipping_returns)
