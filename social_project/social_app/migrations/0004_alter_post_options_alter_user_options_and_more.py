# Generated by Django 4.2.7 on 2023-11-23 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0003_alter_user_age_alter_user_bio_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_at'], 'verbose_name': 'user posts'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-joined_at', 'username'], 'verbose_name': 'user from app'},
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('username', 'email'), name='unique email/username'),
        ),
        migrations.AlterModelTable(
            name='post',
            table='post',
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]
