# Generated by Django 4.2 on 2023-04-04 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='Ism')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='Familiya')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Pochta')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Xodimlarning holati')),
                ('is_active', models.BooleanField(default=True, verbose_name='Faol')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name="Tug'ilgan kun")),
                ('phone', models.CharField(max_length=255, null=True, verbose_name='Telefon raqami')),
                ('user_type', models.CharField(choices=[('super_user', 'Drector'), ('admin', 'Admin'), ('seller', 'Soruvchi')], default='seller', max_length=255, verbose_name='Foydalanuvchi turi')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Foydalanuvchi',
                'verbose_name_plural': 'Foydalanuvchilar',
            },
        ),
    ]