# Generated by Django 3.2.22 on 2023-10-24 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_alter_videoproxy_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
