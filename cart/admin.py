from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import (
    Product, OrderItem, Order, ColourVariation,
    SizeVariation, Address, Payment, Comment, Category, StripePayment, Image, Product_detail
)


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

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name',]


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ['title', 
                    'price', 
                    'stock', 
                    'updated']
    # list_filter = ['status']
    # readonly_fields = ('subject', 'comment', 'user', 'product', 'rate', 'id')
    # prepopulated_fields = {'slug': ('title',)}
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}


# admin.site.register(Category)
admin.site.register(Address, AddressAdmin)
admin.site.register(ColourVariation)
# admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(SizeVariation)
admin.site.register(Payment)
admin.site.register(StripePayment)
admin.site.register(Image)
admin.site.register(Product_detail)