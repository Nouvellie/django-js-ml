from .model_loader import ModelLoader
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


fashion_mnist_model = ModelLoader(model_name="fashionmnist")


class Test(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):

        import time
        time.sleep(2)
        try:
            result = fashion_mnist_model.predict()

        except Exception as e:
            import re, traceback
            result = re.sub(r"\n\s*", " || ", traceback.format_exc())

        return Response({'test': result}, status=status.HTTP_200_OK)