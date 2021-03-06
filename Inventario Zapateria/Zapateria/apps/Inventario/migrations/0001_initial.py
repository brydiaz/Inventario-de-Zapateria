# Generated by Django 3.1.3 on 2020-11-25 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('color', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('talla', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Zapato',
            fields=[
                ('codigoZapato', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('modeloZapato', models.CharField(max_length=100)),
                ('descripcionZapato', models.CharField(max_length=100)),
                ('tipoZapato', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ZapatoPorTallaPorColor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidadZapatosPorTallaPorColor', models.IntegerField()),
                ('codigoZapatoFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.zapato')),
                ('colorFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.color')),
                ('tallaFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.talla')),
            ],
        ),
    ]
