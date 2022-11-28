from django.urls import *
from main import views

urlpatterns = [
    path('', views.main_page),
    path('room', views.room, name='room'),
    path('room/<id>/', views.room_edit, name='roomEdit'),
    path('medCard', views.medCard, name='medCard'),
    path('medCard/<id>/', views.medCard_edit, name='medCardEdit'),
    path('move', views.move, name='move'),
    path('helthy', views.helthy, name='helthy'),

    path('roomOfMedCard', views.roomOfMedCard, name='roomOfMedCard'),
    path('medCardOfDate', views.medCardOfDate, name='medCardOfDate'),
    path('medCardOfAge',  views.medCardOfAge,  name='medCardOfAge'),
]