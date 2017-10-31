from django.contrib import admin

# Register your models here.
from .models import Stock, User, StockMetrics, Portfolio

admin.site.register(Stock)
admin.site.register(User)
admin.site.register(StockMetrics)
admin.site.register(Portfolio)

