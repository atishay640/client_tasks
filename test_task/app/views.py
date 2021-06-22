from django.db import models
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import (Task, Tile,)
from .forms import (TaskForm, TileForm)
from django.urls import reverse_lazy

class TaskCreateView(CreateView):
    template_name = 'task/form.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    model = Task

class TileCreateView(CreateView):
    template_name = 'tile/form.html'
    form_class = TileForm
    success_url = reverse_lazy('tiles')
    model = Tile

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task/list.html'

class TileListView(LoginRequiredMixin, ListView):
    model = Tile
    template_name = 'tile/list.html'

class TaskUpdateView(UpdateView):
    template_name = 'task/form.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    model = Task


class TileUpdateView(UpdateView):
    template_name = 'tile/form.html'
    form_class = TileForm
    success_url = reverse_lazy('tiles')
    model = Tile

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    template_name = 'task/delete.html'

class TileDeleteView(DeleteView):
    model = Tile
    success_url = reverse_lazy('tiles')
    template_name = 'tile/delete.html'

    
