# Generated by Django 4.1.2 on 2022-11-01 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_delete_students'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='username',
        ),
    ]