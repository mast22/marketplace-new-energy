"""
docstring просто чтобы pylint не показывал предупреждение
"""
from django.contrib import admin
from .models import Item, Offer, Images, Material, Contract
# Register your models here.

# class OffersInline(admin.StackedInline):
#     """
#     Предложения на работу в админке
#     """
#     model = Offer
#     extra = 0

# class ItemAdmin(admin.ModelAdmin):
#     """
#     Описание работы
#     """
#     list_display = ('id', 'owner', 'date_added')
#     inlines = [OffersInline]

admin.site.register(Item)
admin.site.register(Offer)
admin.site.register(Images)
admin.site.register(Material)
admin.site.register(Contract)