from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.views.generic.base import View


class IndexView(View):
    template_name = 'TIS_app/base.html'
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
