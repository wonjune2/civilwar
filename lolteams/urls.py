from django.urls import path
from .views import base_views, member_views, league_views

app_name = 'lolteams'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('member/', member_views.member, name='member'),
    path('entry/', base_views.entry, name='entry'),
    path('league_list/', league_views.league_list, name='league_list'),
    path('member/<int:member_id>', member_views.member_detail, name='member_detail'),
]