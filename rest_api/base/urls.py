from django.urls import path


from .views import *


urlpatterns = [
    path('hey',api_home_tradational),
    path('api_models',api_models)
    
]   
