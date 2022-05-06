from django.urls import path

from .views import contact

app_name = "contact"  # these are now referenced as public:index... etc
urlpatterns = [
    path("", contact, name="contact")
]
