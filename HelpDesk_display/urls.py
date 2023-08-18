from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='HelpDesk_display-home'),
    path('about/',views.about,name='HelpDesk_display-about'),
    path('login/',views.login,name='HelpDesk_display-login' )
]