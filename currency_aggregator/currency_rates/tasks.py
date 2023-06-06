from celery import shared_task
from .providers import VkurseProvider, NbuProvider, MinfinProvider
from .models import Currency

@shared_task
def update_exchange_rates():
    # Отримання курсів від провайдерів
    vkurse_provider = VkurseProvider()
    nbu_provider = NbuProvider()
    minfin_provider = MinfinProvider()

    rates_vkurse = vkurse_provider.get_rates()
    rates_nbu = nbu_provider.get_rates()
    rates_minfin = minfin_provider.get_rates()

    # Оновлення валют в базі даних
    for code, rate in rates_vkurse.items():
        currency, created = Currency.objects.get_or_create(code=code)
        currency.rate_vkurse = rate
        currency.save()

    for code, rate in rates_nbu.items():
        currency, created = Currency.objects.get_or_create(code=code)
        currency.rate_nbu = rate
        currency.save()

    for code, rate in rates_minfin.items():
        currency, created = Currency.objects.get_or_create(code=code)
        currency.rate_minfin = rate
        currency.save()
