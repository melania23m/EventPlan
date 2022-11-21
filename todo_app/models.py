from django.db import models


#
#
#
class ToDoList(models.Model):
    name = models.CharField(max_length=300)
    is_checked = models.BooleanField(default=False)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Budget(models.Model):
    denumire = models.CharField(max_length=300)
    cost_total = models.FloatField()
    avans = models.FloatField()
    rest_de_plata = models.FloatField(default=0)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.denumire}"

    def get_budget(self):
        rest_de_plata = 0

        for x in Budget.objects.all():
            rest_de_plata = x.cost_total - x.avans

        return rest_de_plata
