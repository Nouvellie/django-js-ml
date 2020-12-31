from .model_loader import ModelLoader
from django.shortcuts import render
from djangojsml.settings import DEBUG
from PIL import Image
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

import numpy as np
import re
import time
import traceback

# Preload TFLite models with some pre-post process.
fashion_mnist_model = ModelLoader("fashionmnist")
imdb_model = ModelLoader("imdb")
print("\n")


class FashionMnistAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):

        
        try:
            filename = request.data['image'].name
            
            if not filename.endswith(".png"):
                return Response({'error': 'unsupported_media_type',}, status=HTTP_415_UNSUPPORTED_MEDIA_TYPE)

            start_time = time.time()

            img_buffer = list(request.FILES.getlist('image'))
            

            fashion_mnist_result = fashion_mnist_model.predict(img_buffer, confidence_bool=True)
            
            return Response(fashion_mnist_result, status=status.HTTP_200_OK)
        
        except Exception as e:
            full_traceback = re.sub(r"\n\s*", " || ", traceback.format_exc())

            if DEBUG:
                return Response({'error': "bad_request", 'detail': full_traceback,}, status=status.HTTP_400_BAD_REQUEST)
            
            else:
                return Response({'error': "bad_request",}, status=status.HTTP_400_BAD_REQUEST)