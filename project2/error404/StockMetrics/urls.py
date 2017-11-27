from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^portfolio/?', views.portfolio, name='portfolio'),
	url(r'^stockMetric/?', views.stockMetric, name='stockMetric'),
	url(r'^user/?', views.user, name='user'),
	url(r'^order/?', views.order, name='order')
]
