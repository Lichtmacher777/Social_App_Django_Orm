# Generated by Django 4.2.7 on 2023-11-23 15:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0004_alter_post_options_alter_user_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='default_password', max_length=50, validators=[django.core.validators.RegexValidator(message='Password must contain at least 10 characters with at least one uppercase letter, one lowercase letter, one number, and one special character.', regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{10,}$')]),
        ),
    ]