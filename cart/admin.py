from django.contrib import admin
from .models import (
    Product, OrderItem, Order, ColourVariation,
    SizeVariation, Address, Payment, Comment, Category, StripePayment, Image, Product_detail, ColourVariationLang, SizeVariationLang, ProductLang, CategoryLang
)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
    

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'address_line_1',
        'address_line_2',
        'city',
        'zip_code',
        'address_type',
    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'status', 'create_at']
    list_filter = ['status']
    readonly_fields = ('subject', 'comment', 'user', 'product', 'rate', 'id')


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'stock', 'updated']
    # list_filter = ['status']
    prepopulated_fields = {'slug': ('title',)}


class ColourVariationLangAdmin(admin.ModelAdmin):
    list_display = ['name', 'lang']
    list_filter = ['lang']


class SizeVariationLangAdmin(admin.ModelAdmin):
    list_display = ['name', 'lang']
    list_filter = ['lang']


class ProductLangAdmin(admin.ModelAdmin):
    list_display = ['title', 'lang', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['lang']


class CategoryLangAdmin(admin.ModelAdmin):
    list_display = ['name', 'lang']
    list_filter = ['lang']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(ColourVariation)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(SizeVariation)
admin.site.register(Payment)
admin.site.register(StripePayment)
admin.site.register(Image)
admin.site.register(Product_detail)
admin.site.register(ColourVariationLang, ColourVariationLangAdmin)
admin.site.register(SizeVariationLang, SizeVariationLangAdmin)
admin.site.register(ProductLang, ProductLangAdmin)
admin.site.register(CategoryLang, CategoryLangAdmin)

