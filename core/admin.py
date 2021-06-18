from django.contrib import admin
from .models import About, Customer, Carousel, Terms_of_use, Faq, Shipping_returns, Privacy_policy, AboutLang, Language


class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'created','updated']
    

class AboutLangAdmin(admin.ModelAdmin):
    list_display = ['title', 'lang']
    list_filter = ['lang']


class LanguagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'code','status']
    list_filter = ['status']


admin.site.register(Customer)
admin.site.register(Carousel)
admin.site.register(About, AboutAdmin)
admin.site.register(AboutLang, AboutLangAdmin)
admin.site.register(Faq)
admin.site.register(Terms_of_use)
admin.site.register(Shipping_returns)
admin.site.register(Privacy_policy)
admin.site.register(Language, LanguagesAdmin)
