from django.urls import path
from .views import CreateAndListProjectAPIView

urlpatterns = [
    path("all/", CreateAndListProjectAPIView.as_view(), name="project-get-post"),
]