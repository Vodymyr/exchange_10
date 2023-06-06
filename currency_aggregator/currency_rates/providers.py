import requests

class VkurseProvider:
    def get_rates(self):
        response = requests.get('https://vkurse.dp.ua/course.json')
        data = response.json()
        rates = {}
        for item in data:
            rates[item['code']] = float(item['rate'])
        return rates

class NbuProvider:
    def get_rates(self):
        response = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
        data = response.json()
        rates = {}
        for item in data:
            rates[item['cc']] = float(item['rate'])
        return rates

class MinfinProvider:
    def get_rates(self):
        response = requests.get('https://minfin.com.ua/ua/currency/')
        rates = {}

        return rates

from currency_rates.models import Currency

def get_best_rate():
    currencies = Currency.objects.all()
    best_currency = currencies.order_by('-rate').first()
    return best_currency


