# Generated by Django 4.1.5 on 2023-05-22 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='oferta',
            field=models.BooleanField(default=False),
        ),
    ]
