# Generated by Django 4.2.16 on 2024-11-21 08:35

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initiatives', '0008_alter_budget_unit_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='unit_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))]),
        ),
    ]