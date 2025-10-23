from django.urls import path
from . import views


urlpatterns = [
    # Define your account-related URL patterns here
    path("profile/", views.profile_view, name="profile"),
    # path("settings/", views.settings_view, name="settings"),
    # path("logout/", views.logout_view, name="logout"),
    # path("login/", views.login_view, name="login"),
    # path("register/", views.register_view, name="register"),
    # path("password-reset/", views.password_reset_view, name="password_reset"),
    # path("password-change/", views.password_change_view, name="password_change"),
    # path("dashboard/", views.dashboard_view, name="dashboard"),
    
]