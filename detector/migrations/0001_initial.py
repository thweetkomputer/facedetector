# Generated by Django 2.0.5 on 2018-06-06 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FaceDetectionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('face_id', models.CharField(max_length=100, null=True)),
                ('created', models.TimeField(default=datetime.datetime(2018, 6, 6, 17, 57, 36, 379197))),
            ],
        ),
    ]