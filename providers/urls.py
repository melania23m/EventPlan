from django.urls import path

from providers import views

urlpatterns = [
    path('create_provider/', views.ProviderCreateView.as_view(), name='create-provider'),
    path('list_of_providers/', views.ProviderListView.as_view(), name='list-of-providers'),
    path('update_provider/<int:pk>/', views.ProviderUpdateView.as_view(), name='update-provider'),
    path('detail_provider/<int:pk>/', views.ProviderDetailView.as_view(), name='detail-provider'),
    path('delete_provider/<int:pk>/', views.ProviderDeleteView.as_view(), name='delete-provider'),
    path('delete_provider_modal/<int:pk>/', views.delete_provider, name='delete-provider-modal'),

]
