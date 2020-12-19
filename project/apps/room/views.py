from .models import Room
from .serializers import RoomSerializer
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny


class RoomCreateView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (AllowAny,)


class RoomListView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (AllowAny,)