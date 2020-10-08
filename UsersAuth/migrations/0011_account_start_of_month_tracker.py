# Generated by Django 3.0.8 on 2020-08-20 17:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('UsersAuth', '0010_remove_account_start_of_month_tracker'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='start_of_month_tracker',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
