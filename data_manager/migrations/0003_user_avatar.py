# Generated by Django 5.2.3 on 2025-07-22 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_manager', '0002_user_name_user_phone_number_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar.svg', null=True, upload_to=''),
        ),
    ]
