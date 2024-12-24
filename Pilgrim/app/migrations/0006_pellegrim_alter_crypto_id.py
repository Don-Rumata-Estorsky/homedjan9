# Generated by Django 5.1.3 on 2024-12-11 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pellegrim',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('kompas_roda', models.CharField(max_length=100)),
                ('chasy_roda', models.FloatField()),
                ('kventa', models.CharField(max_length=303)),
                ('kokova_chel', models.CharField(max_length=303)),
                ('wepon', models.CharField(max_length=100)),
                ('mirovozrenye', models.CharField(max_length=303)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='crypto',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]