from django.db import models

class Purchase(models.Model):
    city = models.CharField(max_length=50)
    customer_type = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    unit_price = models.FloatField()
    quantity = models.IntegerField()
    product_line = models.CharField(max_length=50)
    tax = models.FloatField()
    total = models.FloatField()
    date = models.DateField()
    time = models.TimeField()
    payment	= models.CharField(max_length=50)
    cogs = models.FloatField()
    profit = models.FloatField()
    rating  = models.FloatField()

    
