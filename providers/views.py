from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, CreateView

from providers.filters import ProviderFilter
from providers.forms import ProviderForm
from providers.models import Provider, Review


class ProviderCreateView(CreateView):
    template_name = 'provider/create_provider.html'
    model = Provider
    form_class = ProviderForm

    success_url = reverse_lazy('create-provider')
    permission_required = 'provider.add_provider'


class ProviderListView(ListView):
    template_name = 'provider/list_of_providers.html'
    model = Provider
    context_object_name = 'all_providers'
    permission_required = 'provider.view_provider'

    def get_context_data(self, **kwargs):
        data = super(ProviderListView, self).get_context_data(**kwargs)

        providers = Provider.objects.all()
        myFilter = ProviderFilter(self.request.GET, queryset=providers)
        data['all_providers'] = myFilter.qs
        data['my_filter'] = myFilter

        return data


#
class ProviderUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'provider/update_provider.html'
    model = Provider
    form_class = ProviderForm
    success_url = reverse_lazy('list-of-providers')
    permission_required = 'provider.update_provider'


# class ProviderDetailView(DetailView):
#     template_name = 'provider/detail_provider.html'
#     model = Provider
#     permission_required = 'provider.detail_provider'

def providerr(request, slug):
    provider = get_object_or_404(Provider, pk=slug)
    if request.method == "POST":
        rating = request.POST.get('rating', 3)
        content = request.POST.get('content', '')

        if content:
            reviews = Review.objects.filter(created_by=request.user, provider=provider)

            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.content = content
                review.save()

            else:

                review = Review.objects.create(
                    provider=provider,
                    rating=rating,
                    content=content,
                    created_by=request.user)

            return redirect('detail-provider', pk=slug)
    return render(request, 'provider/detail_provider.html', {'provider': provider})


@login_required
@permission_required('provider.delete_provider')
def delete_provider(request, pk):
    Provider.objects.filter(id=pk).delete()

    return redirect('list-of-providers')

# class ProviderCreateReview(CreateView):
#     model = ProviderReview
#     template_name = 'provider/review.html'
#     context_object_name = 'form'
#     fields = ['review_text']
#
#     def get(self, request, *args, **kwargs):
#         pk = self.kwargs.get('pk')
#         form = ReviewAdd()
#         return render(request, 'provider/review.html', {'pk': pk, 'form': form})
#
#     def post(self, request, *args, **kwargs):
#         pk = self.kwargs.get('pk')
#         form = self.get_form()
#         if form.is_valid():
#             review = ProviderReview.objects.create(
#                 user=request.user,
#                 provider=Provider.objects.get(pk=pk),
#                 review_text=form.cleaned_data['review_text'],
#
#
#             )
#             review.save()
#             return redirect('provider.detail_provider', pk=pk)
#         return redirect('provider.detail_provider', pk=pk)
#
#

# def save_review(request,pid):
#     provider=Provider.objects.get(pk=pid)
#     user=request.user
#     review=ProviderReview.objects.create(
#         user=user,
#         provider=provider,
#         review_text=request.POST['review_text'],
#         review_rating=request.POST['review_rating'],
#     )
#     return JsonResponse({'bool':True})

# def save_review(request):
#     if request.method == 'POST':
#         form = ReviewAdd(request.POST or None)
#         if form.is_valid():
#             form.save()
#             form = ReviewAdd()
#             reviews = ProviderReview.objects.all()
#             context = {'form': form, 'reviews': reviews}
#             return render(request, 'provider/review.html', context)
#         else:
#             form = ReviewAdd()
#             reviews = ProviderReview.objects.all()
#             context = {'form': form, 'reviews': reviews}
#             return render(request, 'provider/review.html', context)
