from django.contrib import admin
from .models import shoping,product,Cart,CartItems,Categary,Contacts
# Register your models here.
# @admin.register(shoping)
# class shopingadmin(admin.ModelAdmin):
#     list_display=('id','name','email','address','phone','password','gender')

# @admin.register(product)

admin.site.register(shoping)
admin.site.register(Contacts)
admin.site.register(product)
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(Categary)
