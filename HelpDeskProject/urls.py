from django.urls import path
from . import views
from Users import views as user_view


urlpatterns = [
    path('',views.home,name='HelpDeskProject-home'),
    path('about/',views.about,name='HelpDeskProject-about'),
    path('login/',views.login,name='HelpDeskProject-login' ),
    path('register/', user_view.register, name='Users-register')
]