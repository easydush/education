# Generated by Django 3.2 on 2021-06-09 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studying', '0002_alter_courselistener_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='courselistener',
            name='points',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
