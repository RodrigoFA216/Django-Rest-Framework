from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewset(viewsets.ModelViewSet):
    queryset= Project.objects.all()
    #esto se puede cambiar por IsAuthenticated en el caso de que se requiera que solo se modifiquen si está autenticado
    #O se puede cambiar por IsAuthenticatedOrReadOnly en el caso de que se consulten si no está autenticado pero no permita escribir
    permission_classes=[permissions.AllowAny]
    serializer_class=ProjectSerializer