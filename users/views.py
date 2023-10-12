from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


@login_required
def user_detail_view(request):
    user = request.user
    return render(request, 'pages/user_profile.html', {'user': user})


def user_update_view(request):
    user = request.user
    return render(request, 'pages/user_profile_edit.html', {'user': user})