from django.urls import path
from . import views
urlpatterns = [ 
    path('memeberFun/', views.members, name = 'members'),
    path('greetFun/', views.great, name = 'great')
]




