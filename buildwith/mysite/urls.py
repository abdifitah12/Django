from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    
    path('blog/', views.blog, name="blog"),
    path('optin/', views.optin, name="optin"),
    path('prising/', views.pricing, name="pricing"),
    path('Course/', views.Courser, name="Course"),
    #Specifying defaults for view arguments
    path('Course/<int:num>/', views.pricing, name="details"),
     
    
]