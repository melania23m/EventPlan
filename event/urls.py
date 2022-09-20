from django.urls import path

from event import views

urlpatterns=[
    path('create_event/', views.EventCreateView.as_view(), name='create-event'),
    path('list_of_events/', views.EventListView.as_view(), name='list-of-events'),
    path('update_event/<int:pk>/', views.EventUpdateView.as_view(), name='update-event'),
    path('detail_event/<int:pk>/', views.EventDetailView.as_view(), name='detail-event'),
    path('delete_event_modal/<int:pk>/', views.delete_provider, name='delete-event-modal'),

]