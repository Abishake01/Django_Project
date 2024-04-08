from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.cal),
    path('submitquery',views.submitquery,name='submitquery'),
]