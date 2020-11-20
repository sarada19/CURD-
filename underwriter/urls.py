from django.urls import path
from .views import (InsuredcreateView,PolicyCreateView,underwriter)
#from .Utilities import get_risk_details
app_name = 'underwriter'

urlpatterns = [
    path('underwriter/',underwriter,name='underwriter'),
    path('CreateInsured/', InsuredcreateView, name='CreateInsured'),
    path('PolicyCreate/', PolicyCreateView, name='PolicyCreate'),
]