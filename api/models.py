from django.db import models


# Create your models here.
class Ticket(models.Model):
    text = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    date_created = models.CharField(max_length=255, blank=True, null=True)
    data_finish = models.CharField(max_length=255, blank=True, null=True)


class IwaterProducts(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    shname = models.CharField(max_length=255, blank=True, null=True)
    app_name = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    gallery = models.TextField(blank=True, null=True)
    date_created = models.IntegerField(blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    site = models.IntegerField(blank=True, null=True)
    app = models.IntegerField(blank=True, null=True)
    company_id = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iwater_products'