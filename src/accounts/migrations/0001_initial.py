# Generated by Django 3.2 on 2021-04-14 17:35

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='Email Id')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Username')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('mobile_number', models.CharField(max_length=10, unique=True, verbose_name='Mobile Number')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('is_admin', models.BooleanField(default='False')),
                ('is_active', models.BooleanField(default='True')),
                ('is_staff', models.BooleanField(default='False')),
                ('is_superuser', models.BooleanField(default='False')),
                ('profile_image', models.ImageField(blank=True, default=accounts.models.get_default_profile_image_filepath, max_length=255, null=True, upload_to=accounts.models.get_profile_image_filepath)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
