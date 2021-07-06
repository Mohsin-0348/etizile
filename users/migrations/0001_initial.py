# Generated by Django 3.2.4 on 2021-07-05 16:04

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import django_countries.fields
import easy_thumbnails.fields


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
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone_code', models.CharField(blank=True, max_length=5, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('gender', models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male')], max_length=8, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('photo', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='profile_pictures/', verbose_name='Profile Picture')),
                ('photo_uploaded_at', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('last_active_on', models.DateTimeField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('deactivation_reason', models.TextField(blank=True, null=True)),
                ('nationality', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('current_city', models.CharField(blank=True, choices=[('Abu Dhabi', 'Abu Dhabi'), ('Al Ain', 'Al Ain'), ('Ajman', 'Ajman'), ('Dubai', 'Dubai'), ('Fujairah', 'Fujairah'), ('Sharjah', 'Sharjah'), ('Umm Al Quwain', 'Umm Al Quwain'), ('Ras Al Khaimah', 'Ras Al Khaimah')], max_length=30, null=True)),
                ('carrier_level', models.CharField(blank=True, max_length=20, null=True)),
                ('current_position', models.CharField(blank=True, max_length=32, null=True)),
                ('current_company', models.CharField(blank=True, max_length=32, null=True)),
                ('salary_expectations', models.CharField(blank=True, max_length=32, null=True)),
                ('commitment', models.CharField(blank=True, max_length=32, null=True)),
                ('notice_period', models.CharField(blank=True, max_length=32, null=True)),
                ('visa_status', models.CharField(blank=True, max_length=32, null=True)),
                ('highest_education', models.CharField(blank=True, max_length=32, null=True)),
                ('cv', models.FileField(blank=True, null=True, upload_to='user/cv/')),
                ('is_deleted', models.BooleanField(default=False)),
                ('term_and_condition_accepted', models.BooleanField(default=False)),
                ('privacy_policy_accepted', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
