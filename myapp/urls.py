from django.urls import path
from . import views

from rest_framework import routers
from .api import ProjectViewSet

# urlpatterns = [
#    path('', views.index, name="index"),
 #   path('about/', views.about, name="about"),
 #   path('hello/<str:username>', views.hello, name="hello"),
 #   path('projects/', views.projects, name="projects"),
 #   path('projects/<int:id>', views.project_detail, name="project_detail"),
 #   path('tasks/', views.tasks, name="tasks"),
 #   path('create_task/', views.create_task, name="create_task"),
 #   path('create_new_project/', views.create_project, name="create_project"),
 #   
#]
#

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')


urlpatterns = router.urls
