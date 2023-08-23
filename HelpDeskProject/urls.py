from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='HelpDeskProject-home'),
    path('about/',views.about,name='HelpDeskProject-about'),
    path('login/',views.login,name='HelpDeskProject-login' )
]