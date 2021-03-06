# Generated by Django 3.1.7 on 2021-06-26 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actualite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('contenu', models.TextField()),
                ('image', models.ImageField(upload_to='images/articles')),
            ],
        ),
        migrations.CreateModel(
            name='AppelOffert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Apropos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=250)),
                ('logo', models.ImageField(upload_to='images/logo')),
                ('video', models.FileField(upload_to='videos/')),
                ('libelle', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='publiciteadmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/publicites')),
                ('status', models.CharField(default='en attente', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SousCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('Categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myAdmin.categories')),
            ],
        ),
    ]
