# Generated by Django 4.2.7 on 2023-11-28 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_venta_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='cliente',
        ),
        migrations.DeleteModel(
            name='Detalle',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.DeleteModel(
            name='Venta',
        ),
    ]