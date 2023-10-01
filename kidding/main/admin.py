from django.contrib import admin
from .models import shoes
from .models import order

admin.site.register(shoes)
admin.site.register(order)