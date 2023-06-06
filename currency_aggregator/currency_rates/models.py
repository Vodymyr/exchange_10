from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)
    rate_vkurse = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    rate_nbu = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    rate_minfin = models.DecimalField(max_digits=10, decimal_places=4, null=True)

    def __str__(self):
        return self.code
