from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from providers.forms import ProviderForm
from providers.models import Provider


class ProviderCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'provider/create_provider.html'
    model = Provider
    form_class = ProviderForm

    success_url = reverse_lazy('create-provider')
    permission_required = 'provider.add_provider'


class ProviderListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'provider/list_of_providers.html'
    model = Provider
    context_object_name = 'all_providers'
    permission_required = 'provider.view_provider'

#
class ProviderUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'provider/update_provider.html'
    model = Provider
    form_class = ProviderForm
    success_url = reverse_lazy('list-of-providers')
    permission_required = 'provider.update_provider'


class ProviderDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'provider/detail_provider.html'
    model = Provider
    permission_required = 'provider.detail_provider'



@login_required
@permission_required('provider.delete_provider')
def delete_provider(request, pk):
    Provider.objects.filter(id=pk).delete()

    return redirect('list-of-providers')


