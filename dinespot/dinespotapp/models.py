from django.db import models
from django.contrib.auth import get_user_model

client = get_user_model()
restaurant = get_user_model()

# Create your models here.
class Client(models.Model):
    user = models.ForeignKey(client, on_delete=models.CASCADE, default=None)
    client_id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    mail = models.EmailField(max_length=100)

    def __str__(self):
        return self.user.username

class Restaurant(models.Model):
    user = models.ForeignKey(restaurant, on_delete=models.CASCADE, default=None)
    rest_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    country = models.CharField(max_length=60)
    state = models.CharField(max_length=80)
    city = models.CharField(max_length=21)
    p_code = models.CharField(max_length=10)
    colony = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    num_ext = models.SmallIntegerField()
    num_int = models.SmallIntegerField(null=True, blank=True)
    max_cap = models.SmallIntegerField()

    def __str__(self):
        return self.user.username

class Reserve(models.Model):
    resrv_id = models.AutoField(primary_key=True)
    hr = models.TimeField()
    date = models.DateField()
    num_people = models.PositiveSmallIntegerField()

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    rest = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.resrv_id