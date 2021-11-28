from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer
from .models import Students


class StudentsViewSet(ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
