from django.db import models
from django.utils import timezone
from django.shortcuts import render,redirect 
from django.contrib import messages
from django import forms
from django.contrib.auth.decorators import login_required
from .forms import TicketCreationForm
from .models import Ticket

# Create your views here.

# This ticket view imports from forms, which then imports from ticket class.
# The Ticket view has Create and Display ticket.
# Update is in progress 

@login_required
def CreateTicket(request):
    if request.method == 'POST':
        ticket_form = TicketCreationForm(request.POST)
        if ticket_form.is_valid():
            ticket_form.save()
            ticket = ticket_form.save()
            messages.success(request, f'{ticket} has been created.')
            return redirect('display_ticket', pk=ticket.pk)
    else:
        ticket_form = TicketCreationForm()
    return render(request, 'create_ticket.html', {'form' : ticket_form})


@login_required
def DisplayTicket(request):
        ticket_display = Ticket.objects.filter(user=request.user)
        return render(request, 'display_ticket.html', {'ticket' : ticket_display})