
from django.contrib.auth.models import User

from django.urls import reverse_lazy
from django.views.generic import CreateView

from userextend.forms import UserExtendForm


class UserExtendCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    moder = User
    form_class = UserExtendForm
    success_url = reverse_lazy('login')

