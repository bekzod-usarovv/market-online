# Generated by Django 4.2 on 2023-04-05 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('status', models.CharField(choices=[('created', 'Yaratilgan'), ('accepted', 'Tasdiqlangan'), ('completed', 'Tugallangan'), ('canceled', 'Rad etilgan')], max_length=255, verbose_name='Maxsulot Xolati')),
                ('total', models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Narxi')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.client', verbose_name='Xaridor')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Narxi')),
                ('count', models.IntegerField(verbose_name='Soni')),
                ('total', models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Summasi')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.order', verbose_name='Zakaz')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product', verbose_name='Maxsulot')),
            ],
        ),
    ]
