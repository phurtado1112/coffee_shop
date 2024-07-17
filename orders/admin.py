from django.contrib import admin
from .models import Order, OrderProduct


class OrdemrProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrdemrProductInlineAdmin]


admin.site.register(Order, OrderAdmin)
