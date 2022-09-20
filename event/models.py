from django.db import models


#
#
#
class Event(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=150)
    event_date = models.DateTimeField()

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name}"
