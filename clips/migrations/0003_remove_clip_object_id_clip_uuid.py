# Generated by Django 4.2.4 on 2023-08-19 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clips', '0002_clip_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clip',
            name='object_id',
        ),
        migrations.AddField(
            model_name='clip',
            name='uuid',
            field=models.CharField(default='b76a9bf6692f4aa98d22b5d342dd0958', max_length=200, unique=True),
        ),
    ]
