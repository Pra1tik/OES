from django.urls import path
from . import views

urlpatterns = [
    path('lobby/', views.lobby, name="lobby"),
    path('tlobby/', views.tlobby, name="tlobby"),

    path('room/', views.room),
    path('get_token/', views.getToken),

    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
]