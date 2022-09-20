from django.views.generic import ListView
from django.shortcuts import render
from .models import *


class FilmsView(ListView):

    model = FilmsModel
    template_name = 'index.html'
    context_object_name = 'films'

    def get_context_object_date(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["range"]= range()



