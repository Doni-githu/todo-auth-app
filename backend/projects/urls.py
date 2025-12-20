from django.urls import path
from .views import CreateAndListProjectAPIView, RetrieveDeleteAndPutProjectAPIView

urlpatterns = [
    path("all/", CreateAndListProjectAPIView.as_view(), name="project-get-post"),
    path("<int:id>/", RetrieveDeleteAndPutProjectAPIView.as_view(), name="project-delete-get-put")
]