# tasks/views.py
from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import generate_report

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


@api_view(['POST'])
def generate_report_view(request):
    user_id = request.data.get('user_id')
    task = generate_report.delay(user_id)
    return Response({"task_id": task.id, "status": "Processing"})

# tasks/views.py
from kafka.producer import log_event

def some_view(request):
    # Ваш код
    log_event("User performed an action")
    return Response({"message": "Action logged"})

