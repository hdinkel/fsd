# Generated by Django 2.0 on 2017-12-05 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0006_auto_20171205_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='id',
        ),
        migrations.AlterField(
            model_name='files',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]