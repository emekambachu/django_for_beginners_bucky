# Generated by Django 2.2 on 2019-10-21 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
