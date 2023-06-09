# Generated by Django 4.2 on 2023-04-19 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('income', '0003_income_warehouse'),
        ('client', '0002_alter_client_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('provider', '0002_alter_provider_options'),
        ('order', '0005_remove_orderitem_warehouse_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outlay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Xarajot nomi')),
                ('outlay_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payment.outlay', verbose_name='Xarajot kategoriyasi')),
            ],
        ),
        migrations.CreateModel(
            name='OutlayCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Xarajotlar kategoriyasi')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('cash', 'Naqd pul'), ('card', 'Cartadan'), ('bank', 'Bank')], max_length=255, verbose_name="To'lov usuli")),
                ('payment_type', models.CharField(choices=[('income', 'Tavar krimi'), ('order', 'Zakaz'), ('client', 'Xaridor'), ('provider', 'Yetkazib beruvchi'), ('outlay', 'Xarajat')], max_length=255, verbose_name="To'lov turi")),
                ('transaction_type', models.CharField(choices=[('income', 'Krim'), ('outcome', 'Chiqim')], max_length=50, verbose_name='Tranzaksiya turi')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Qiymati')),
                ('is_deleted', models.BooleanField(verbose_name="O'chirilgan")),
                ('comment', models.CharField(max_length=400, verbose_name='Izoh')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')),
                ('deleted_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name="O'chirilgan sana")),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='client.client', verbose_name='Xaridor')),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_user', to=settings.AUTH_USER_MODEL, verbose_name='Yaratgan xodim')),
                ('deleted_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deleted_user', to=settings.AUTH_USER_MODEL, verbose_name="O'chirgan xodim")),
                ('income', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='income.income', verbose_name='Maxsulot krimi')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='order.order', verbose_name='Zakaz')),
                ('outlay', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='payment.outlay', verbose_name='Xarajat nomi')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='provider.provider', verbose_name='Yetkazib beruvchi')),
            ],
        ),
    ]
