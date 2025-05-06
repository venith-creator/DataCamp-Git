from django.contrib import admin
from .models import Product, Offer
from .models import ContactMessage


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'product')


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at' )


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)