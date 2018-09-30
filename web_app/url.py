from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    # path('applications/tic_tac_toe/', views.tic_tac_toe, name='tic_tac_toe'),
    path('tic_tac_toe/', views.tic_tac_toe, name='tic_tac_toe'),
]
