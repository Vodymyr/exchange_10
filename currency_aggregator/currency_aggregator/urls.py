from django.urls import path
from currency_rates.views import exchange_calculator

urlpatterns = [
    path('exchange/', exchange_calculator, name='exchange_calculator'),
]
