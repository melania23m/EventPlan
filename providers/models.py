from django.db import models

#
#
#
from userextend.models import UserExtend


class Provider(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    city = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return f"{self.name} {self.description}"


class Rating(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    user = models.ForeignKey(UserExtend, on_delete=models.CASCADE)
    number = models.IntegerField()
