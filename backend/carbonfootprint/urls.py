from django.urls import path
from .views import *

app_name = "Carbon"

urlpatterns = [
    path('',Home,name="Home"),
    path('individual-calculator',IndividualCalculator,name="IndividualCalculator"),
    path('business-calculator',BusinessCalculator,name="BusinessCalculator"),
]
