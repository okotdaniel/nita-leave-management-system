# Generated by Django 3.0.6 on 2020-07-08 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeDashboard', '0024_auto_20200703_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaves',
            name='file_upload',
            field=models.FileField(default='No file', upload_to='documents/files/'),
            preserve_default=False,
        ),
    ]
