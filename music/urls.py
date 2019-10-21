from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [

    # /music/
    path('', views.index, name='index'),

    # /music/id/
    path('<int:id>/', views.detail, name='detail'),
]