from django.contrib import admin

from providers.models import Provider, Review
admin.site.register(Provider)
admin.site.register(Review)