from django.shortcuts import render
from .models import Players, Category
from .serializers import PlayersSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.decorators import action
from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class PlayersAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'rage_size'
    max_page_size = 10000


class PlayersAPIList(generics.ListCreateAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PlayersAPIListPagination


class PlayersAPIUpdate(generics.UpdateAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )


class PlayersAPIDestroy(generics.ListCreateAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
    permission_classes = (IsAdminOrReadOnly,)


# class PlayersViewSet(mixins.CreateModelMixin,
#                      mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.ListModelMixin,
#                      GenericViewSet):
#     # queryset = Players.objects.all()
#     serializer_class = PlayersSerializer

#     def get_queryset(self):
#         pk = self.kwargs.get("pk")

#         if not pk:
#             return Players.objects.all()[:3]

#         return Players.objects.filter(pk=pk)

#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objecrs.get(pk=pk)
#         return Response({'cats': cats.name})
# class PlayersAPIList(generics.ListCreateAPIView):
#     queryset = Players.objects.all()
#     serializer_class = PlayersSerializer
# class PlayersAPIUpdate(generics.UpdateAPIView):
#     queryset = Players.objects.all()
#     serializer_class = PlayersSerializer
# class PlayerAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Players.objects.all()
#     serializer_class = PlayersSerializer
# class PlayersAPIView(APIView):
#     def get(self, request):
#         w = Players.objects.all().values()
#         return Response({'posts': PlayersSerializer(w, many=True).data})
#     def post(self, request):
#         serializer = PlayersSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not alowwed"})
#         try:
#             instance = Players.objects.get(pk=pk)
#         except:
#             return Response({"error": "Objects does not exists"})
#         serializer = PlayersSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
# class PlayersAPIView(generics.ListAPIView):
#    queryset = Players.objects.all()
#    serializer_class = PlayersSerializer
