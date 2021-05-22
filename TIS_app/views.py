from formtools.wizard.views import SessionWizardView
from rest_framework import generics, viewsets

from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.base import View

from TIS_app.forms import (
    CircuitForm,
    InventoryForm,
    PhotoForm,
    RegisterForm,
    TreeForm,
)
from TIS_app.models import (
    Circuit,
    Comment,
    Inventory,
    Photo,
    Species,
    Tree,
    User,
)
from TIS_app.permissions import IsOwnerOrReadOnly
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


# Application views ---------------------------------------------

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
    extra_context = {}

    def get(self, request, *args, **kwargs):
        inventory = get_object_or_404(Inventory, pk=kwargs['pk'])
        self.extra_context['tree_list'] = Tree.objects.filter(
            inventory=inventory)
        return super().get(request, *args, **kwargs)


class AddTreeToInventoryView(LoginRequiredMixin, CreateView):
    model = Tree
    form_class = TreeForm
    initial = {}

    def get(self, request, *args, **kwargs):
        inventory = get_object_or_404(Inventory, pk=kwargs['inventory_pk'])
        self.initial['inventory'] = inventory

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.extra_context['inventory_pk'] =
        return render(self.request, self.template_name, self.extra_context)


class AddCircuitTreeView(LoginRequiredMixin, CreateView):
    model = Circuit
    form_class = CircuitForm
    success_url = reverse_lazy('index')
    initial = {}

    def get(self, request, *args, **kwargs):
        self.extra_context['inventory_pk'] = kwargs['inventory_pk']
        tree = get_object_or_404(Tree, pk=kwargs['tree_pk'])
        self.initial['tree'] = tree

        return super().get(request, *args, **kwargs)


class YourInventoryView(LoginRequiredMixin, ListView):
    model = Inventory

    def get_queryset(self):
        return Inventory.objects.filter(author=self.request.user)


class TreeDetailView(DetailView):
    model = Tree


class AddPhotoToTreeView(CreateView):
    model = Photo
    form_class = PhotoForm
    initial = {}
    extra_context = {}

    def get(self, request, *args, **kwargs):
        inventory = get_object_or_404(Inventory, pk=kwargs['inventory_pk'])
        self.extra_context['inventory'] = inventory
        tree = get_object_or_404(Tree, pk=kwargs['tree_pk'])
        self.initial['tree'] = tree

        return render(self.request, self.template_name, self.extra_context)
