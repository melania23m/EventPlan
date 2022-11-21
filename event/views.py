from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import request
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

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

    # def get_queryset(self):
    #     queryset = super(EventListView, self).get_queryset()
    #     status = self.request.GET.get('status')
    #     if status:
    #         queryset = queryset.filter(status=status)
    #     filter_queryset = queryset.filter(client_name=self.request.user)
    #     return filter_queryset
    #


class EventUpdateView(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    template_name = 'event/update_event.html'
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('list-of-events')


class EventDetailView(DetailView):
    template_name = 'event/detail_event.html'
    model = Event
    permission_required = 'event.detail_event'


class EventDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'event/delete_event.html'
    model = Event
    success_url = reverse_lazy('list-of-events')
    permission_required = 'event.delete_event'

#
# @login_required
# @permission_required('event.delete_event')
# def delete_event(request, pk):
#     Event.objects.filter(id=pk).delete()
#
#     return redirect('list-of-events')
