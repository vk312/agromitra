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
from rest_framework import generics
from rest_framework import mixins

from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.


# Farmer  CRUD operations
class GenericFarmerView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                        mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = FarmerSerializer
    queryset = Farmer.objects.all()
    lookup_field = 'id'

    # authentication_classes = [SessionAuthentication,BasicAuthentication]
    # parser_classes = [permissions.IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


# AgriExpert  CRUD operations
class GenericExpertView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                        mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ExpertSerializer
    queryset = AgriExpert.objects.all()
    lookup_field = 'id'

    # authentication_classes = [SessionAuthentication,BasicAuthentication]
    # parser_classes = [permissions.IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


# AgriAssistant  CRUD operations

class GenericAssistantView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                           mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = AssistantSerializer
    queryset = AgriAssistant.objects.all()
    lookup_field = 'id'

    # authentication_classes = [SessionAuthentication,BasicAuthentication]
    # parser_classes = [permissions.IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


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




# farmer details get and post code
class Farmersdata(APIView):
    def get(self, request):
        farmers = Farmer.objects.all()
        serializer = FarmerSerializer(farmers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FarmerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Agri-Expert details get and post code
class Expertsdata(APIView):

    def get(self, request):
        experts = AgriExpert.objects.all()
        serializer = ExpertSerializer(experts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExpertSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Agri-Expert details get and post code
class Assistantdata(APIView):
    def get(self, request):
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
