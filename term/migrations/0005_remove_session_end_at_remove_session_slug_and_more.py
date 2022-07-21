# Generated by Django 4.0.6 on 2022-07-20 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('term', '0004_remove_term_cracreator_term_maker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='end_at',
        ),
        migrations.RemoveField(
            model_name='session',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='session',
            name='time',
        ),
        migrations.AddField(
            model_name='session',
            name='type',
            field=models.CharField(choices=[('present', 'present'), ('absent', 'absent'), ('absenceallowed', 'absenceallowed')], default='present', max_length=14, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='session',
            name='description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='session',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='name session'),
        ),
    ]
