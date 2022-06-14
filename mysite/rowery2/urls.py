from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('typeofbike/', views.typeofbike, name='typeofbike'),
    path('parts/', views.parts, name='parts'),
    path('bike/', views.bike, name='bike'),
    path('form/', views.form, name='form'),
    ]