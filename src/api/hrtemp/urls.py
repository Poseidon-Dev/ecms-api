from django.urls import path
from hrtemp import views

urlpatterns = [
    path('views/', views.HRTEMPList.as_view()),
]
