from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('applications/', views.applications, name='applications'),
    # path('applications/', views.applications, name='applications'),
    path('resume/', views.resume, name='resume'),
    path('applications/millionaire/', views.millionaire, name='millionaire'),
    path('applications/atm/', views.atm, name='atm'),
    path('applications/tic_tac_toe/', views.tic_tac_toe, name='tic_tac_toe'),

]