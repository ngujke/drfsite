from .models import Players
from .serializers import PlayersSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import  IsOwnerOrReadOnly

class PlayersViewSet(viewsets.ModelViewSet):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
