from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import User, Stock, StockMetrics, Portfolio, StockData
from .forms import StockForm
from .client import get_price_data, get_prices_data, get_prices_time_data

def index(request):

    all_stocks = list(StockData.objects.all())

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'all_stocks':all_stocks},
    )

@login_required
def portfolio(request):
    user = request.user.id
    print(user)
    infos = []
    sym = []
    form = StockForm()
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data['symbol'].upper()
            sym.append(symbol)
            
            
            param = {'q':symbol,'i':"86400",'x':"INDEXDJX",'p':"1M"}
            data2 = get_price_data(param)
            data = data2[-1]
            infos = [data] if data.__class__ == dict else data
            


    return render(request, 'portfolio.html', {'form': form,
                                                     'infos': infos, 'sym':sym})

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
