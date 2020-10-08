# Generated by Django 3.0.2 on 2020-04-18 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeDashboard', '0003_auto_20200418_2331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaveform',
            name='id',
        ),
        migrations.AddField(
            model_name='leaveform',
            name='slug',
            field=models.SlugField(default='test'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='leaveform',
            name='ReferenceId',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
