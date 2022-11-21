from django.conf.urls.static import static
from django.urls import path

from finalProject import settings
from providers import views
from providers.views import providerr

urlpatterns = [
    path('create_provider/', views.ProviderCreateView.as_view(), name='create-provider'),
    path('list_of_providers/', views.ProviderListView.as_view(), name='list-of-providers'),
    path('update_provider/<int:pk>/', views.ProviderUpdateView.as_view(), name='update-provider'),
    path('detail_provider/<slug:slug>/', providerr, name='detail-provider'),
    path('delete_provider_modal/<int:pk>/', views.delete_provider, name='delete-provider-modal'),
    # path('provider-review/<int:pid>/',views.ProviderCreateReview.as_view(), name='create-review'),




 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
