# Generated by Django 4.0.6 on 2022-07-25 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Familia', '0004_remove_familia_creation_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='familia',
            name='dni',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
