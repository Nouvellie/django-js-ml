from .models import Room
from .serializers import (
    CreateRoomSerializer,
    RoomSerializer,
)
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RoomCreateView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (AllowAny,)


class RoomListView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (AllowAny,)


class CreateRoomAPIView(APIView):

    serializer_class = CreateRoomSerializer
    
    def post(self, request, format=None):
        pass