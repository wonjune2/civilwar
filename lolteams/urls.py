from django.urls import path
from . import views

app_name = 'lolteams'

urlpatterns = [
    path('', views.index, name='index'),
    path('member/', views.member, name='member'),
    path('league/', views.league, name='league'),
    path('league_list/', views.league_list, name='league_list'),
    path('member/<int:member_id>', views.member_detail, name='member_detail'),
]