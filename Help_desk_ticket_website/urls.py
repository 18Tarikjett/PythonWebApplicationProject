from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='Help_desk_ticket_website-home'),
    path('about/',views.about,name='Help_desk_ticket_website-about')
]