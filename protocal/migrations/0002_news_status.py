# Generated by Django 4.0.4 on 2022-04-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
