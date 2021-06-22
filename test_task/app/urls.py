
from django.urls import path
from  . import views


urlpatterns = [
    path('tasks/create/', views.TaskCreateView.as_view(), name='task-create'),
    path('tiles/create/', views.TileCreateView.as_view(), name='tile-create'),
    path('tasks/' , views.TaskListView.as_view(), name='tasks'),
    path('tiles/' , views.TileListView.as_view(), name='tiles'),
    path('tasks/<int:pk>/update', views.TaskUpdateView.as_view(), name='task-update'),
    path('tiles/<int:pk>/update', views.TileUpdateView.as_view(), name='tile-update'),
    path('tasks/<int:pk>/delete', views.TaskDeleteView.as_view(), name='task-delete'),
    path('tiles/<int:pk>/delete', views.TileDeleteView.as_view(), name='tile-delete'),
]
