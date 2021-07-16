from django.db import models

# Create your models here.
class Ticket(models.Model):
    text = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    date_created = models.CharField(max_length=255, blank=True, null=True)
    data_finish = models.CharField(max_length=255, blank=True, null=True)