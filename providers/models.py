from django.db import models




class Provider(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    city = models.CharField(max_length=150)
    description = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.name} {self.description}"
