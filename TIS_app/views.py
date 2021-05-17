from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.base import View
from rest_framework import generics, viewsets

from TIS_app.forms import RegisterForm
from TIS_app.models import (
    Circuit,
    Comment,
    Inventory,
    Photo,
    Species,
    Tree,
    User,
)
from TIS_app.serializers import (
    InventorySerializer,
    UserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class IndexView(View):
    template_name = 'TIS_app/base.html'
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)


class RegisterView(CreateView):
    model = get_user_model()
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        form.save()
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return redirect(self.get_success_url())


class AllInventoryAPIView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class AllInventoryView(ListView):
    model = Inventory


class CreateNewInventoryView(CreateView):
    pass
