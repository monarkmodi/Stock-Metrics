from django.shortcuts import render

# Create your views here.
from .models import User, Stock, StockMetrics, Portfolio

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_stocks=Stock.objects.all().count()
    num_users=User.objects.all().count()
    num_stocks_GOOG = Stock.objects.filter(title__contains = 'GOOG').count()

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_stocks':num_stocks,'num_users':num_users,'num_stocks_GOOG':num_stocks_GOOG,'num_visits':num_visits},
    )
