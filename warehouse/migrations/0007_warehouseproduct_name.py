# Generated by Django 4.2 on 2023-05-02 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0006_movement_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouseproduct',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]