from django.contrib import admin

# Register your models here.
from .models import Stock, User, StockMetrics, Portfolio

#admin.site.register(Stock)
#admin.site.register(User)
#admin.site.register(StockMetrics)
#admin.site.register(Portfolio)


class StockDisplay(admin.ModelAdmin):
    list_display = ('title', 'stock_id', 'volume', 'buy_price','sell_price')
    fields = ['title', 'stock_id', 'volume', 'buy_price','sell_price']
    

# Register the admin class with the associated model
admin.site.register(Stock, StockDisplay)


# Register the Admin classes for Book using the decorator
class UserDisplay(admin.ModelAdmin):
	list_display = ('name','date_of_birth','email','password','balance')
	fields = ['name','date_of_birth','email','password','balance']

admin.site.register(User, UserDisplay)

class MetricsDisplay(admin.ModelAdmin):
	list_display = ('Metric_Title','StockName')
	fields = ['Metric_Title','StockName']

admin.site.register(StockMetrics, MetricsDisplay)

class PortfolioDisplay(admin.ModelAdmin):
	list_display = ('user','portfolio_value','buying_power','withdrawable_cash','cash_balance','invested_fund')
	fields = ['user','portfolio_value','buying_power','withdrawable_cash','cash_balance','invested_fund']

admin.site.register(Portfolio, PortfolioDisplay)