from django.urls import path
from .views import (
    PostAndListProjectAPIView,
    RetrieveDeleteAndPutProjectAPIView,
    PostAndListTodosAPIView,
    RetrieveDeleteAndPutTodoAPIView
)

urlpatterns = [
    path("all/", PostAndListProjectAPIView.as_view(), name="project-get-post"),
    path("<int:id>/", RetrieveDeleteAndPutProjectAPIView.as_view(), name="project-delete-get-put"),
    path("<int:id>/todos/", PostAndListTodosAPIView.as_view(), name="todo-get-post"),
    path("<int:id>/todos/<int:todo_id>/", RetrieveDeleteAndPutTodoAPIView.as_view(), name="todo-get-post"),
    path("<int:id>/todos/<int:todo_id>/", RetrieveDeleteAndPutTodoAPIView.as_view(), name="todo-get-post"),
]