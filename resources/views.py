from django.shortcuts import render

# Create your views here.
# users/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Resources
from .serializers import ResourceSerializer
from rest_framework.permissions import IsAuthenticated


class resources_detail(APIView):
    def get_object(self,pk):
        try:
            return Resources.objects.get(pk=pk)
        except Resources.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,format= None):
        resource = self.get_object(pk)
        serializer = ResourceSerializer(resource)
        return Response(serializer.data)

    

class all_resources(APIView):

    def get_resources(self):
        try:
            return Resources.objects.all()
        except:
            raise Http404
        
    def get(self,request):
        Resource = self.get_resources()
        serializer = ResourceSerializer(Resource, many=True)
        return Response(serializer.data)
    