# Generated by Django 2.1 on 2020-01-01 07:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0004_auto_20200101_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='dor',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]
