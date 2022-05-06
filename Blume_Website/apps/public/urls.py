from django.urls import path

from . import views  # from local directory, import views

app_name = "public"  # these are now referenced as public:index... etc
urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.projects, name="projects"),
]
