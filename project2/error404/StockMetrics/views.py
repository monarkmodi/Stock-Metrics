from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import User, Stock, StockMetrics, Portfolio, StockData
from .forms import StockForm
from .client import get_price_data, get_prices_data, get_prices_time_data
import numpy

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
            Stock(user=user, symbol=symbol).save()
        
            param = {'q':symbol,'i':"86400",'x':"INDEXDJX",'p':"1M"}
            data2 = get_price_data(param)
            data = data2[-1]
            infos = [data] if data.__class__ == dict else data

    all_portfolio = list(Stock.objects.all().order_by('-id')[:5])

    return render(request, 'portfolio.html', {'all_portfolio':all_portfolio,'form': form,
                                                     'infos': infos, 'sym':sym})

@login_required
def order(request):
    user = request.user.id
    all_stocks = list(Stock.objects.all())
    print(user)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data['symbol'].upper()
            shares = form.cleaned_data['shares']
            
            param = {'q':symbol,'i':"86400",'x':"INDEXDJX",'p':"1M"}
            data2 = get_price_data(param)
#            print(type(data2))
            print('data2',data2.at('close'))
#            infos = [data] if data.__class__ == dict else data
            
            print(symbol, shares)
    else:
        form = OrderForm()
#        symbol = form.cleaned_data['symbol'].upper()
#        shares = form.cleaned_data['shares']

    return render(
        request,
        'order.html',
        context={'all_stocks':all_stocks, 'form':form},
    )


def user(request):
    all_users = list(User.objects.all())

    return render(
        request,
        'user.html',
        context={'all_users':all_users},
    )

@login_required
def stockMetric(request):
    all_metrics = list(StockMetrics.objects.all())
    infos = []
    sym = []
    form = StockForm()

    val = 0.0
    upward = []
    up_mean = 0.0
    downward = []
    down_mean = 0.0
    val_array = []
    symbol = ''
    a = numpy.random.uniform(low=0.1, high=99.9, size=10)
    Metric_value = dict(enumerate(a))
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            for i in all_metrics:
                symbol = i.StockName
            sym.append(symbol)
            
            
            param = {'q':symbol,'i':"86400",'x':"INDEXDJX",'p':"1M"}
            data2 = get_price_data(param)
            data = data2[-1]
            print(symbol)
            
            for i in all_metrics:
                for j in data2:
                    if i.Metric_Title == 'RSI':
                        if (j.Close > j.Open):
                            upward.append(j.Close - j.Open)
                            up_mean = numpy.mean(upward)
                        else:
                            downward.append(j.Open - j.Close)
                            down_mean = numpy.mean(downward)
                        val = 100 - (100/(1 + (up_mean/down_mean)))
                        print(val)
                        val_array.append(val)


    return render(request, 'stockMetric.html', {'all_metrics':all_metrics,'form': form,
                                                     'Metric_value':Metric_value, 'sym':sym})
