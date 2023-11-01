from django.urls import path
from . import views

urlpatterns = [
    
    path('myapp/', views.my_view, name='my_view'),  
   
]
