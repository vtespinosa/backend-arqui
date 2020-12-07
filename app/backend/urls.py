from django.urls import path, include
from . import views

urlpatterns = [
  path('rooms/', views.rooms.as_view() ),
  path('messages/', views.messages.as_view() ),
  path('create_user/', views.create_user),
  path('create_room/', views.create_room),
  path('', views.check_health),

  # Social django
  path('', include('social_django.urls')),
  path('', include('django.contrib.auth.urls')),
  path('logout/', views.logout),
]