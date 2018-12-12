# Generated by Django 2.1.4 on 2018-12-08 12:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailAppModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2018, 12, 8, 13, 14, 0, 790246))),
            ],
        ),
    ]