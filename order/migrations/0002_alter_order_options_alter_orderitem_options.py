# Generated by Django 4.2 on 2023-04-09 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Zakaz', 'verbose_name_plural': 'Zakazlar'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Zakaz birligi', 'verbose_name_plural': 'Zakaz birliklari'},
        ),
    ]
