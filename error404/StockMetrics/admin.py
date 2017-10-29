from django.contrib import admin

# Register your models here.
from .models import Stock, User

admin.site.register(Stock)
admin.site.register(User)
