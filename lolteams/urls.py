from django.urls import path
from . import views

app_name = 'lolteams'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:member_id>/', views.detail, name='detail'),
    path('member/', views.member, name='member'),
    path('league/', views.league, name='league'),
    path('league_list/', views.league_list, name='league_list')
]