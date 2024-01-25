# Generated by Django 5.0.1 on 2024-01-24 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='costo',
            field=models.IntegerField(blank=True, default=0, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='codigo',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='direccion',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='cantidad',
            field=models.IntegerField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='precio',
            field=models.IntegerField(blank=True, default=0, max_length=30, null=True),
        ),
    ]
