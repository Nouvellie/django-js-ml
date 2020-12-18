from django.shortcuts import render
from rest_framework import (
    generics,
    status,
)
from rest_framework.response import Response
from rest_framework.views import APIView


class FirstApiView(APIView):

    def post(self, request):
        pass