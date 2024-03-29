from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginpage, name="login"),
    path('logout/',views.logoutuser, name="logout"),
    path('register/',views.registerpage, name="register"),
    
    path('profile/<str:pk>', views.userprofile, name='user-profile'),

    path('', views.home, name= "home"),
    path('room/<str:pk>/', views.room, name= "room" ),

    path('create-room/',views.createroom, name="create-room"),
    path('update-Room/<str:pk>', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>', views.deleteroom, name='delete-room'),
    path('delete-message/<str:pk>', views.deletemessage, name='delete-message'),
    path('edit-message/<str:pk>', views.editmessage, name='edit-message'),

    path('update-user/', views.updateuser, name='update-user'),
    path('topics/', views.topicspage, name='topics'),
    path('activity/',  views.activitypage, name='activity')
]