from todos.views import CreateToDoAPIView, TodoListAPIView
from django.urls import path


urlpatterns = [
    path('create', CreateToDoAPIView.as_view(), name="create-todo"),
    path('list', TodoListAPIView.as_view(), name="list-todo"),

]
