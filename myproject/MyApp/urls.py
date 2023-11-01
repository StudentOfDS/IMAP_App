from django.urls import path
from . import views

urlpatterns = [
    
    path('MyApp/', views.my_view, name='my_view'),  
   
]
