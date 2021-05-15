from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register',views.register, name='register'),
    path('home', views.index, name='home'),
    path('about',views.about, name='about'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('profile',views.profile, name='profile'),
    path('player',views.player, name='player'),
    #path('edit',views.edit, name='edit'),
    path('SaveData',views.SaveData, name='SaveData'),
    path('search',views.search, name='search'),
    path('VerifyUser',views.VerifyUser, name='VerifyUser'),
    path('EditData',views.EditData, name='EditData'),
    path('delete',views.delete, name='delete'),
    path('Album',views.Album, name='Album')
]