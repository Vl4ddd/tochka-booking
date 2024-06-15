from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework import routers


from hotel_app.views import *
from users import views as user_views
from hotel_app import views



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("register/", user_views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path("profile/", user_views.profile, name="users/profile"),
    path("hotel/<int:post_id>/", hotel),
    path("booking/<int:post_id>/", booking),
    path("booking/<int:post_id>/payment/", payment),
    path('hotels/', HotelList.as_view(), name='hotel-list'),
    path('hotels/<int:pk>/', HotelDetail.as_view(), name='hotel-detail'),
]
