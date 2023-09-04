from django.urls import path
from backend import views

urlpatterns = [
    path("songs/", views.song_list),
    path("songs/<int:pk>/", views.song_detail),
    path("shows/", views.show_list),
    path("shows/<int:pk>/", views.show_detail),
]
