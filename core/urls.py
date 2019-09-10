from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_list, name='profile_list'),
    path('create/', views.profile_create, name='profile_create'),

    path('programmer/list/', views.programmer_list, name='programmer_list'),
    path('programmer/create/', views.programmer_create, name='programmer_create'),
    path('programmer/<int:programmer_id>/', views.programmer_update, name='programmer_update'),
]