# Generated by Django 5.0 on 2024-10-26 16:52

import django.utils.timezone
import utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0003_alter_csrreport_beneficiary_impact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programlogbook',
            name='activity_description',
            field=utils.fields.CustomRichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='programlogbook',
            name='activity_type',
            field=models.CharField(blank=True, choices=[('WORKSHOP', 'Workshop Session'), ('OUTREACH', 'Outreach Campaign'), ('TRAINING', 'Training Program'), ('MEETING', 'Stakeholder Meeting'), ('EVENT', 'Community Event'), ('OTHER', 'Other Activity')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='programlogbook',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='programlogbook',
            name='participants_count',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]