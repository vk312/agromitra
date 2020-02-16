from django.core.serializers import json
from django.http.response import HttpResponse
from django.views.generic import View
from rest_framework.generics import ListCreateAPIView
from rest_framework.renderers import JSONRenderer
from .models import Farmer, AgriExpert, AgriAssistant, States, Cities, Talukas
from .serializers import FarmerSerializer, ExpertSerializer, AssistantSerializer, StatesSerializer, CitiesSerializer, \
    TalukasSerializer
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# AgriExpert  CRUD operations



# states
class States_View(APIView):

    def get(self, request):
        states = States.objects.all()
        serializer = StatesSerializer(states,many=True)
        return Response(serializer.data)


#cities
class Cities_View(APIView):

    def get(self, request,state_id):
          cities = Cities.objects.filter(state_id=state_id)
          serializer = CitiesSerializer(cities,many=True)
          return Response(serializer.data)

    def post(self, request):
        serializer = CitiesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# talukas
class Talukas_View(APIView):

    def get(self, request,city_id):
          taluka = Talukas.objects.filter(city_id=city_id)
          serializer = TalukasSerializer(taluka,many=True)
          return Response(serializer.data)


    def post(self, request):
        serializer = TalukasSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Farmer  CRUD operations
class Farmers_View(APIView):
    def get(self, request,id=None):
        if id:
            farmers = Farmer.objects.filter(id=id)
            serializer = FarmerSerializer(farmers, many=True)
            return Response(serializer.data)
        else:
            farmers = Farmer.objects.all()
            serializer = FarmerSerializer(farmers, many=True)
            return Response(serializer.data)


    def post(self, request):
        serializer = FarmerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Agri-Expert CRUD operations
class Experts_View(APIView):

    def get(self, request,id=None):
        if id:
            experts = AgriExpert.objects.filter(id=id)
            serializer = ExpertSerializer(experts, many=True)
            return Response(serializer.data)
        else:
            experts = AgriExpert.objects.all()
            serializer = ExpertSerializer(experts, many=True)
            return Response(serializer.data)


    def post(self, request):
        serializer = ExpertSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Agri-Expert CRUD operations
class Assistant_View(APIView):
    def get(self, request, id=None):
        if id:
            experts = AgriAssistant.objects.filter(id=id)
            serializer = AssistantSerializer(experts, many=True)
            return Response(serializer.data)
        else:
            experts = AgriAssistant.objects.all()
            serializer = AssistantSerializer(experts, many=True)
            return Response(serializer.data)



    def post(self, request):
        serializer = AssistantSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# CRUD operations on farmer details
#
# class Farmersdetail(APIView):
#
#     def get_object(self, id):
#         try:
#             return Farmer.objects.get(id=id)
#
#         except Farmer.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self,request,id):
#         farmer = self.get_object(id)
#         serializer = FarmerSerializer(farmer)
#         return Response(serializer.data)
#
#     def put(self, request,id):
#         farmer = self.get_object(id)
#         serializer = FarmerSerializer(farmer, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request):
#         farmer = self.get_object(id)
#         farmer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
