from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    TYPE_CHOICES = [
        ('perishable', 'Perishable'),
        ('non_perishable', 'Non-perishable'),
    ]
    description = models.CharField(max_length=100)
    type = models.CharField(choices=TYPE_CHOICES, max_length=20)

class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    zone = models.CharField(max_length=100)
    base_distance_in_km = models.IntegerField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    km_price_perishable = models.DecimalField(max_digits=10, decimal_places=2)
    km_price_non_perishable = models.DecimalField(max_digits=10, decimal_places=2)
