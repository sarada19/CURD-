from django.urls import path
from .views import *
#from django.contrib.auth import views as auth_views
app_name = 'GenInsuranceApp'
urlpatterns=[
    path('',home,name='GenInsuranceApp-home'),
    path('aboutus/',aboutus,name='GenInsuranceApp-aboutus'),
    path('login/',loginView,name='GenInsuranceApp-login'),
    path('signup/',signup,name= 'GenInsuranceApp-signup'),
    path('logout/',logout_view,name='GenInsuranceApp-logout'),
    path('main/',mainmenu,name='GenInsuranceApp-mainmenu'),
    #path('login1/',auth_views.loginView,{'template_name': 'General/login.html'},name='login')
]