# Generated by Django 4.0.6 on 2022-07-20 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='cracreator',
            new_name='maker',
        ),
    ]
