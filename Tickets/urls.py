from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateTicket, name='Create_Ticket'),
    path('display/', views.DisplayTicket, name='Display_Ticket')
    # path('ticket/<int:pk>', views.display_ticket, name='display_ticket')
]