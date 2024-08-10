from django.contrib import admin

from app.models import Client, Car, Sale
# Register your models here.
admin.site.register(Client)
admin.site.register(Car)
admin.site.register(Sale)