from django.urls import path
from .views import Experts_View,Farmers_View, Assistant_View,States_View, Cities_View,Talukas_View

urlpatterns = [
    # path('farmers/', farmer_list),
    path('farmers/', Farmers_View.as_view()),
    path('farmers/<int:id>/', Farmers_View.as_view()),
    path('agri_experts/', Experts_View.as_view()),
    path('agri_experts/<int:id>/', Experts_View.as_view()),
    path('agri_assistant/', Assistant_View.as_view()),
    path('agri_assistant/<int:id>/',Assistant_View.as_view()),
    path('states/', States_View.as_view()),
    path('cities/<int:state_id>/', Cities_View.as_view()),
    path('talukas/<int:city_id>/', Talukas_View.as_view()),


]
