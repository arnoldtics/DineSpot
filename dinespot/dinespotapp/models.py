from django.db import models

# Create your models here.
class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    mail = models.EmailField(max_length=100)

class Restaurant(models.Model):
    rest_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=60)
    state = models.CharField(max_length=80)
    city = models.CharField(max_length=21)
    p_code = models.CharField(max_length=10)
    colony = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    num_ext = models.SmallIntegerField()
    num_int = models.SmallIntegerField(null=True, blank=True)
    max_cap = models.SmallIntegerField()

class Reserve(models.Model):
    resrv_id = models.AutoField(primary_key=True)
    hr = models.TimeField()
    date = models.DateField()
    num_people = models.PositiveSmallIntegerField()

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    rest = models.ForeignKey(Restaurant, on_delete=models.CASCADE)