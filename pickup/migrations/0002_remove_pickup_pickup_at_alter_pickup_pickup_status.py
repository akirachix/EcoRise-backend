# Generated by Django 5.2.4 on 2025-07-17 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pickup', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pickup',
            name='pickup_at',
        ),
        migrations.AlterField(
            model_name='pickup',
            name='pickup_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed')], default='Pending', max_length=50),
        ),
    ]
