# Generated by Django 4.2.16 on 2024-11-21 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initiatives', '0010_alter_kpi_baseline_value_alter_kpi_unit_of_measure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpi',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]