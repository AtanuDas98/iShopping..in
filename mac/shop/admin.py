from django.contrib import admin

# Register your models here.
from . models import product
from . models import Contact,Orders,OrderUpdate

admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)