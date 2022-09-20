from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from event.forms import EventForm
from event.models import Event


class EventCreateView(CreateView):
    template_name = 'event/create_event.html'
    model = Event
    form_class = EventForm

    success_url = reverse_lazy('create-event')

class EventListView(ListView):
    template_name = 'event/list_of_events.html'
    model = Event
    context_object_name = 'all_events'


class EventUpdateView(UpdateView):
    template_name = 'event/update_event.html'
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('list-of-events')

class EventDetailView(DetailView):
    template_name = 'event/detail_event.html'
    model = Event
    permission_required = 'event.detail_event'

@login_required
@permission_required('event.delete_event')
def delete_provider(request, pk):
    Event.objects.filter(id=pk).delete()

    return redirect('list-of-events')


