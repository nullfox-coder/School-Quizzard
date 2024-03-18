from django.contrib import admin
from django.urls import path
from quiz_app import views

# urlpatterns = [
#     path("", views.index, name = "quiz_app"),
#     path("about", views.about, name = "about"),
#     path("services", views.services, name = "services"),
# ]

urlpatterns = [
    path('',views.home,name="home"),
]