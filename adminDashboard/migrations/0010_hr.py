# Generated by Django 3.0.6 on 2020-07-15 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminDashboard', '0009_auto_20200702_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='HR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
