# Generated by Django 4.2.7 on 2023-11-23 08:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('bio', models.TextField(blank=True)),
                ('joined_at', models.DateTimeField(default=datetime.datetime(2023, 11, 23, 8, 27, 15, 236501, tzinfo=datetime.timezone.utc))),
                ('age', models.PositiveIntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 11, 23, 8, 27, 15, 236733, tzinfo=datetime.timezone.utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_app.user')),
            ],
        ),
    ]
