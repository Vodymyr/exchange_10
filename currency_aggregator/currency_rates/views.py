from django.shortcuts import render
from .models import Currency

def exchange_calculator(request):
    if request.method == "POST":
        currency_a = request.POST["currency_a"]
        currency_b = request.POST["currency_b"]
        amount = float(request.POST["amount"])

        currencies = Currency.objects.all()
        currency_a_obj = currencies.get(code=currency_a)
        currency_b_obj = currencies.get(code=currency_b)

        rate = currency_a_obj.rate_vkurse
        result = amount * rate

        context = {
            "currency_a": currency_a_obj,
            "currency_b": currency_b_obj,
            "amount": amount,
            "result": result,
        }
        return render(request, "exchange_calculator.html", context)

    currencies = Currency.objects.all()
    context = {
        "currencies": currencies,
    }
    return render(request, "exchange_calculator.html", context)


