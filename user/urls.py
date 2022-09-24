from django.urls import path,include
from user import views


urlpatterns = [
    path("user/", views.user, name='user'),
    #path("about/", views.about, name ='about'),
    #path("" , views.layout, name = "layout"),
]
