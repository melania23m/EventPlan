

import django_filters


from providers.models import Provider


class ProviderFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')
    city = django_filters.CharFilter(lookup_expr='icontains', label='City')


    class Meta:
        model = Provider
        fields = ['name', 'city', 'description']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.filters['name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': "Please enter a name"})

        self.filters['city'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': "Please enter a city"})
        self.filters['description'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': "Please enter a description",'required': False})