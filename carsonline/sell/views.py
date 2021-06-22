from django.shortcuts import render
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView
from .models import Car, PurchaseOrder
from .forms import ListCarForm, BuyCarForm
from django.http import HttpResponseRedirect

class HomeView(ListView):
  model = Car 
  paginate_by = 5
  template_name = "home.html"
  context_object_name = "car_list"
  ordering = ['-created_at']

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["is_paginated"] = True
    return context

  def get_queryset(self):
    filters = {}
    if self.request.GET.get("make"):
      filters["make__iexact"] = self.request.GET.get("make")
    if self.request.GET.get("year"):
      filters["year__iexact"] = self.request.GET.get("year")

    return Car.objects.filter(**filters).order_by('-created_at')


class ListCarView(CreateView):
  template_name = 'list_car.html'
  form_class = ListCarForm
  success_url = '/success/'


class BuyCarView(CreateView):
  template_name = "buy_car.html"
  form_class = BuyCarForm
  success_url = '/success/'

  def form_valid(self, form):
    data = form.cleaned_data
    data["car"] = Car.objects.get(id= self.kwargs["pk"])
    PurchaseOrder.objects.create(**data)
    Car.objects.filter(id= self.kwargs["pk"]).update(status='S')
    return HttpResponseRedirect('/success/')


def car_make_available_view(request, pk=None):
  Car.objects.filter(id= pk).update(status='A')
  return HttpResponseRedirect('/home/')