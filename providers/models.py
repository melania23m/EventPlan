from django.contrib.auth.models import User
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

    def get_rating(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total = review.rating

        if reviews_total > 0:
            return reviews_total/ self.reviews.count()

        return 0




class Review(models.Model):
    provider = models.ForeignKey(Provider, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(default=3)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
