# Generated by Django 2.0 on 2017-12-14 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0014_auto_20171214_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=400)),
            ],
        ),
    ]
