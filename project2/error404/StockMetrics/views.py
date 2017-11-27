from django.shortcuts import render

# Create your views here.
from .models import User, Stock, StockMetrics, Portfolio

def index(request):

    all_stocks = list(Stock.objects.all())

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'all_stocks':all_stocks},
    )

def portfolio(request):
    all_portfolio = list(Portfolio.objects.all())


    return render(
        request,
        'portfolio.html',
        context={'all_portfolio':all_portfolio},
    )

def order(request):

    all_stocks = list(Stock.objects.all())

    return render(
        request,
        'order.html',
        context={'all_stocks':all_stocks},
    )


def user(request):
    all_users = list(User.objects.all())

    return render(
        request,
        'user.html',
        context={'all_users':all_users},
    )

def stockMetric(request):
    all_metrics = list(StockMetrics.objects.all())

    return render(
        request,
        'stockMetric.html',
        context={'all_metrics':all_metrics},
    )
