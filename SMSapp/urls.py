from django.urls import path
from . import views
urlpatterns = [ 
    path('memeberFunction/', views.members, name = 'members'),
    path('greetFunction/', views.great, name = 'great')
]




