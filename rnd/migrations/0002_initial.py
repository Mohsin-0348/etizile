# Generated by Django 3.2.4 on 2021-07-05 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rnd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseadvertise',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='posted_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='advertiseattachment',
            name='base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='attachment_base', to='rnd.baseadvertise'),
        ),
    ]
