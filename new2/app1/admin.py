

# Register your models here.
from django.contrib import admin
from app1.models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)

admin.site.register(signup)

admin.site.register(order)
admin.site.register(cart)

# admin.site.register(OrderItems)



