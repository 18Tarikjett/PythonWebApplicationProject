# Generated by Django 3.2.21 on 2023-09-18 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tickets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='TicketProblem',
            new_name='Problem',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='TicketStatus',
            new_name='Status',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='TicketTitle',
            new_name='Title',
        ),
    ]
