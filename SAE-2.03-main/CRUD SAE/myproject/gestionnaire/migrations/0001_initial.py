# Generated by Django 4.1.7 on 2023-06-16 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Enseignant',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_etudiant', models.IntegerField(blank=True, null=True, unique=True)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('groupe', models.CharField(max_length=100)),
                ('photo', models.ImageField(null=True, upload_to='gestionnaire/photo/')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'Etudiant',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('coefficient', models.IntegerField()),
            ],
            options={
                'db_table': 'Examen',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RessourcesUE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_ressource', models.CharField(max_length=50, unique=True)),
                ('nom', models.TextField()),
                ('descriptif', models.TextField()),
                ('coefficient', models.IntegerField()),
            ],
            options={
                'db_table': 'RessourcesUE',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UnitesEnseignement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, unique=True)),
                ('nom', models.TextField()),
                ('semestre', models.IntegerField()),
                ('credit_ects', models.IntegerField()),
            ],
            options={
                'db_table': 'UnitesEnseignement',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.FloatField()),
                ('appreciation', models.TextField()),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionnaire.etudiant')),
                ('examen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionnaire.examen')),
            ],
            options={
                'db_table': 'Note',
                'managed': True,
            },
        ),
    ]
