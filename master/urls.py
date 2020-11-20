from django.urls import path
from .views import ProductsMaster,master,ProductRisk,AgentCreate,AgentCommission,vehicleMasterView,\
    vehicleDepreciationView,NCBMasterView,ClaimStatusMasterView,ClaimsSurveyorMasterView
app_name='master'

urlpatterns =[
    path("master/",master,name="master-master"),
    path("productmaster/",ProductsMaster,name = "master-ProductMaster"),
    path("productrisk/",ProductRisk,name="master-ProductRisk"),
    path('agentcreate/',AgentCreate,name = 'master-AgentCreate'),
    path('agentcommision/',AgentCommission,name='master-AgentCommision'),
    path('vehiclemaster/',vehicleMasterView,name='master-vehicleMasterView'),
    path('depriciation/',vehicleDepreciationView,name='master-vehicleDepreciationView'),
    path('ncb/',NCBMasterView,name='master-NCBMasterView'),
    path('claim/',ClaimStatusMasterView,name='master-ClaimStatusMasterView'),
    path('survey/',ClaimsSurveyorMasterView,name='master-ClaimsSurveyorMasterView'),

]
