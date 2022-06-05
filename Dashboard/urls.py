from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.Login),
    path('Dashboard',views.Dashboard),
    path('LawyerAccount',views.LawyerAccount),
    path('ValuationDetails',views.ValuationDetails),
]
