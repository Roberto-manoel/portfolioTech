from django.urls import path
from pages import views as pages_views
from projects import views as projects_views

urlpatterns = [
    path('', pages_views.home, name='home'),
    path("", projects_views.project_index, name="project_index"),
    path("<int:pk>/", projects_views.project_detail, name="project_detail"),
]