from django.urls import path
from .views import TaskListCreateView, TaskDetailView
from djoser import views as djoser_views
from djoser.urls import authtoken
from django.urls import path, include
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('auth/', include('djoser.urls.authtoken')),
]
