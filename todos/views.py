from todos.serializers import TodoSerializer
from rest_framework.generics import CreateAPIView, ListAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Todo 

class TodosAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)


# class CreateToDoAPIView(CreateAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = (IsAuthenticated,)

#     def perform_create(self, serializer):
#         return serializer.save(owner=self.request.user)

# class TodoListAPIView(ListAPIView):
#     serializer_class=TodoSerializer
#     permission_classes=(IsAuthenticated,)
#     queryset= Todo.objects.all()

#     def get_queryset(self):
#         return Todo.objects.filter(owner=self.request.user)