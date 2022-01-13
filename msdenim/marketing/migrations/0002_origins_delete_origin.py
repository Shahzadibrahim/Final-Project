# Generated by Django 4.0.1 on 2022-01-13 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Origins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Origin', models.CharField(max_length=50, verbose_name='Origin')),
                ('gender', models.PositiveSmallIntegerField(choices=[(0, 'MALE'), (1, 'FEMALE')], default=0, verbose_name='Gender')),
                ('Color', models.PositiveSmallIntegerField(choices=[(0, 'DARKDENIM'), (1, 'MEDIUMDENIM'), (2, 'LIGHTDENIM'), (3, 'COLORFUL'), (4, 'COLORFUL'), (5, 'STRETCH'), (6, 'COTTON')], default=((0, 'DARKDENIM'), (1, 'MEDIUMDENIM'), (2, 'LIGHTDENIM'), (3, 'COLORFUL'), (4, 'COLORFUL'), (5, 'STRETCH'), (6, 'COTTON')), verbose_name='Color')),
                ('Range', models.CharField(max_length=4, verbose_name='Range')),
            ],
            options={
                'verbose_name': 'Origins',
            },
        ),
        migrations.DeleteModel(
            name='Origin',
        ),
    ]