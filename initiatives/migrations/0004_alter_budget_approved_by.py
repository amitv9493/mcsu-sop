# Generated by Django 5.0 on 2024-10-25 19:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initiatives', '0003_alter_task_assigned_to'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='approved_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='initiative_approved_budgets', to='users.member'),
        ),
    ]
