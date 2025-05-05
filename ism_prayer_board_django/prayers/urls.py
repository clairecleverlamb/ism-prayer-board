from django.urls import path
from . import views, views_auth


urlpatterns = [
    path('', views.home_view, name='home'),
    path('submit/', views.submit_prayer, name='submit_prayer'),
    path('prayer/<int:pk>/', views.prayer_detail, name='prayer_detail'),
    path('pray/<int:pk>/', views.pray_for_request, name='pray_for_request'),
    path("signup/", views_auth.signup_view, name="signup"),
    path("signin/", views_auth.signin_view, name="signin"),
    path("signout/", views_auth.signout_view, name="signout"),
]
