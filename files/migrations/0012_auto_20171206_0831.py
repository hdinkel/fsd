# Generated by Django 2.0 on 2017-12-06 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0011_auto_20171205_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='hash',
            field=models.CharField(editable=False, max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]
