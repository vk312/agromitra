from django.urls import path
from .views import Expertsdata, Farmersdata, Assistantdata, GenericFarmerView, GenericExpertView, GenericAssistantView, \
    States_View, Cities_View ,Talukas_View

urlpatterns = [
    # path('farmers/', farmer_list),
    path('farmers/', Farmersdata.as_view()),
    path('experts/', Expertsdata.as_view()),
    path('agri_assistants/', Assistantdata.as_view()),
    path('generic_farmer/<int:id>/', GenericFarmerView.as_view()),
    path('generic_expert/<int:id>/', GenericExpertView.as_view()),
    path('generic_assistant/<int:id>/', GenericAssistantView.as_view()),
    path('states/', States_View.as_view()),
    path('cities/<int:state_id>/', Cities_View.as_view()),
    path('talukas/<int:city_id>/', Talukas_View.as_view()),


]
