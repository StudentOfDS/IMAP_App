from django.shortcuts import render
from django.urls import path 
from . import views 

 

urlpatterns = [ 

    path('my-view/', views.my_view, name='my-view'), 

] 

 
def my_view(request): 

    return render(request, 'my_view.html')   

 
urlpatterns = [ 

    path('my-view/', views.my_view, name='my-view'), 

] 
