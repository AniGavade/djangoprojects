# Generated by Django 4.1.2 on 2022-10-30 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=100)),
                ('relation', models.IntegerField()),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song', to='meranayaapp.singer')),
            ],
        ),
    ]
