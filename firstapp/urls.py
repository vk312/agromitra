from django.urls import path
from .views import Expertsdata, Farmersdata, Assistantdata, GenericFarmerView, GenericExpertView, GenericAssistantView, \
    GenericStatesView, GenericCitiesView,Talukas_List

urlpatterns = [
    # path('farmers/', farmer_list),
    path('farmers/', Farmersdata.as_view()),
    path('experts/', Expertsdata.as_view()),
    path('agri_assistants/', Assistantdata.as_view()),
    path('generic_farmer/<int:id>/', GenericFarmerView.as_view()),
    path('generic_expert/<int:id>/', GenericExpertView.as_view()),
    path('generic_assistant/<int:id>/', GenericAssistantView.as_view()),
    path('states/<int:id>/', GenericStatesView.as_view()),
    path('states/', GenericStatesView.as_view()),
    path('cities/<int:state_id>/', GenericCitiesView.as_view()),
    path('cities/', GenericCitiesView.as_view()),
    path('talukas/<int:city_id>/', Talukas_List.as_view()),
    #path('talukas_delete/<int:id>/', GenericTalukasView.as_view()),
    #path('taluka_update/<int:id>/', GenericTalukasView.as_view()),

]
