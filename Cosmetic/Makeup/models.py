from django.db import models



class Productes(models.Model):
    product_name = models.CharField(max_length=100)
    product_kind = models.CharField(max_length=100)
    product_descreption = models.CharField(max_length=500)
    Expir_date = models.DateField()
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    