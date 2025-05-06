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
    path('submit-ajax/', views.create_prayer_ajax, name='create_prayer_ajax'),
    path('refresh-prayers/', views.refresh_prayer_list, name='refresh_prayer_list'),
    path('prayer/<int:pk>/edit/', views.edit_prayer, name='edit_prayer'),
    path('prayer/<int:pk>/delete/', views.delete_prayer, name='delete_prayer'),
]
