# Generated by Django 5.0.3 on 2024-03-28 20:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('short_url', models.URLField()),
                ('id_short', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_visits', models.IntegerField()),
                ('id_short', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shorturl_app.shorturl')),
            ],
        ),
    ]
