from django.urls import path

from . import views

urlpatterns = [
    path('<int:reqId>', views.detail, name='detail'),
    path('', views.index, name='index'),
]
