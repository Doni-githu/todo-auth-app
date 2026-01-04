from django.urls import path
from .views import (
    PostAndListProjectAPIView,
    DeleteAndPutProjectAPIView,
    PostAndListTodosAPIView,
    RetrieveDeleteAndPutTodoAPIView,
    RetrieveProjectAPIView
)

urlpatterns = [
    path("all/", PostAndListProjectAPIView.as_view(), name="project-get-post"),
    path("<int:id>/action/", DeleteAndPutProjectAPIView.as_view(), name="project-delete-get-put"),
    path("<int:id>/info/", RetrieveProjectAPIView.as_view(), name="project-delete-get-put"),
    path("<int:id>/todos/", PostAndListTodosAPIView.as_view(), name="todo-get-post"),
    path("<int:project_id>/todos/<int:pk>/", RetrieveDeleteAndPutTodoAPIView.as_view(), name="todo-get-post"),
]