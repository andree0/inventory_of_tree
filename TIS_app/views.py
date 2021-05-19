from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.base import View
from rest_framework import generics, viewsets
from TIS_app.permissions import IsOwnerOrReadOnly

from TIS_app.forms import InventoryForm, RegisterForm
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


# API views --------------------------------------------

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]


class AllInventoryAPIView(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class DetailInventoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [IsOwnerOrReadOnly]


# App views ---------------------------------------------

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


class AllInventoryView(ListView):
    model = Inventory


class CreateNewInventoryView(LoginRequiredMixin, CreateView):
    model = Inventory
    form_class = InventoryForm
    success_url = reverse_lazy('index')


class DetailInventoryView(DetailView):
    model = Inventory


