from django.contrib import admin
from .models import (
    Product, OrderItem, Order, ColourVariation,
    SizeVariation, Address, Payment, Comment, Category, StripePayment, Image
)
from . import models
class EcommerceAdminArea(admin.AdminSite):
    site_header = 'Ecom Admin Area'

ecom_site = EcommerceAdminArea(name = 'EcomAdmin')

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'address_line_1',
        'address_line_2',
        'city',
        'zip_code',
        'address_type',
    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'content', 'approved', 'create_at']
    list_filter = ['approved']
    list_editable = ['approved']
    readonly_fields = ('subject', 'content', 'user', 'product', 'rate', 'id')


class ProductAdmin(admin.ModelAdmin):
    list_display = [
                    'title', 
                    'active',
                    'price', 
                    'stock', 
                    'updated']

    fieldsets = [
            (u'ColourVariation', {'fields': (
                    'title_en',
                    'slug_en',
                    'product_detail_en',
                    'specification_en',
                    'featured',
                    'available_colours',
                    'available_sizes',
                    'active',
                    'primary_category',
                    'secondary_categories',
                    'price', 
                    'price_save',
                    'stock', 
                    'title_fr',
                    'slug_fr',
                    'product_detail_fr',
                    'specification_fr',
                    
            )})
        ]
    prepopulated_fields = {'slug_en': ('title_en',), 'slug_fr': ('title_fr',)}


class SizeVariationAdmin(admin.ModelAdmin):
    list_display = ['name',]
    
    fieldsets = [
            (u'SizeVariation', {'fields': ('name_en', 'name_fr',)})
        ]
        

class ColourVariationAdmin(admin.ModelAdmin):
    list_display = ['name',]
    
    fieldsets = [
            (u'ColourVariation', {'fields': ('name_en', 'name_fr',)})
        ]

ecom_site.register(models.Product)
admin.site.register(Category)
admin.site.register(Address, AddressAdmin)
admin.site.register(ColourVariation,ColourVariationAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(SizeVariation, SizeVariationAdmin)
admin.site.register(Payment)
admin.site.register(StripePayment)
admin.site.register(Image)
