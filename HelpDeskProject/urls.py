from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from Users import views as user_view


urlpatterns = [
    path('',views.home,name='HelpDeskProject-home'),
    path('about/',views.about,name='HelpDeskProject-about'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='Users-login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='Users-logout'),
    path('register/', user_view.register, name='Users-register'),
]