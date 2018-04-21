from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home' ),
    url(r'^locate/', views.locate, name='locate'),
    url(r'^otp/', views.book, name='otp'),
    url(r'^book/', views.book_food, name='book'),
    url(r'^success/', views.success, name='success'),
]