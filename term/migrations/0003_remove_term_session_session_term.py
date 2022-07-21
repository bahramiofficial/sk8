# Generated by Django 4.0.6 on 2022-07-18 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('term', '0002_remove_session_term_term_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='term',
            name='session',
        ),
        migrations.AddField(
            model_name='session',
            name='term',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sessions', to='term.term'),
        ),
    ]