# Generated by Django 2.2 on 2019-10-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_song_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
