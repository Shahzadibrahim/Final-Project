# Generated by Django 4.0.1 on 2022-01-12 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='heading1',
            field=models.CharField(default=3, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='heading2',
            field=models.CharField(default=3, max_length=100),
            preserve_default=False,
        ),
    ]
