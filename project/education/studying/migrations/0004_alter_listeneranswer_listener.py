# Generated by Django 3.2 on 2021-06-09 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studying', '0003_courselistener_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listeneranswer',
            name='listener',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studying.courselistener'),
        ),
    ]