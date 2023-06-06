from django.test import TestCase
from django.urls import reverse
from .models import Currency

class ExchangeCalculatorTestCase(TestCase):
    def setUp(self):
        self.currency_usd = Currency.objects.create(name='US Dollar', code='USD', rate_vkurse=25.0)
        self.currency_eur = Currency.objects.create(name='Euro', code='EUR', rate_vkurse=30.0)

    def test_exchange_calculator_view(self):
        url = reverse('exchange_calculator')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_exchange_calculator_post(self):
        url = reverse('exchange_calculator')
        data = {
            'currency_a': self.currency_usd.code,
            'currency_b': self.currency_eur.code,
            'amount': '100',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Result:')
