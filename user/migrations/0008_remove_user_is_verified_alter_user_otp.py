# Generated by Django 4.2 on 2023-05-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_user_email_verification_token_user_otp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_verified',
        ),
        migrations.AlterField(
            model_name='user',
            name='otp',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
