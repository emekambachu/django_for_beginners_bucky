from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [

    # /music/
    path('', views.IndexView.as_view(), name='index'),

    # default html file name should be album_form (modelname_form)
    path('create-album/', views.CreateAlbumView.as_view(), name='create-album'),

    # /music/id/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # /music/id/favorite/
    # path('<int:album_id>/favorite/', views.favorite, name='favorite'),
]