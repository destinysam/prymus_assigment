# Generated by Django 3.2.7 on 2021-10-03 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prymusNews', '0002_viewonnews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewonnews',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
