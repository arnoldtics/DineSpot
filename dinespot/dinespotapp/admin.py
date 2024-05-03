from django.contrib import admin
from .models import Client, Reserve, Restaurant

# Register your models here.
admin.site.register(Client)
admin.site.register(Restaurant)
admin.site.register(Reserve)