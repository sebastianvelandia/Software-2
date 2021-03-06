# Generated by Django 3.1.7 on 2021-03-13 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('autorId', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('isbn', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('autores', models.ManyToManyField(to='HistoriaApp.Autor')),
            ],
        ),
        migrations.CreateModel(
            name='Reseña',
            fields=[
                ('reseñaId', models.AutoField(primary_key=True, serialize=False)),
                ('comentario', models.CharField(max_length=300)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HistoriaApp.libro')),
            ],
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('calificacionId', models.AutoField(primary_key=True, serialize=False)),
                ('calificacion', models.IntegerField()),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HistoriaApp.libro')),
            ],
        ),
    ]
