# Generated by Django 3.2 on 2021-05-09 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210509_1624'),
        ('studying', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courselistener',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listeners', to='core.course'),
        ),
    ]
