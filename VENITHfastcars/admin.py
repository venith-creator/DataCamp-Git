from django.contrib import admin
from .models import Product, offer
from .models import ContactMessage


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class offerAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at' )


admin.site.register(Product, ProductAdmin)
admin.site.register(offer, offerAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)