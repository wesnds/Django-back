# Generated by Django 5.0.6 on 2024-05-27 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='codigo_curso',
            field=models.CharField(max_length=50),
        ),
    ]
