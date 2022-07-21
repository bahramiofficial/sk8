# Generated by Django 4.0.6 on 2022-07-20 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('term', '0003_remove_term_session_session_term'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='term',
            name='cracreator',
        ),
        migrations.AddField(
            model_name='term',
            name='maker',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='terms', to=settings.AUTH_USER_MODEL),
        ),
    ]
