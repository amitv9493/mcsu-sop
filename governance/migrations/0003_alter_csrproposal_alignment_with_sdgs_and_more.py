# Generated by Django 5.0 on 2024-10-25 20:51

import utils.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('governance', '0002_alter_csrproposal_prepared_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csrproposal',
            name='alignment_with_sdgs',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='csrproposal',
            name='budget_breakdown',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='csrproposal',
            name='executive_summary',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='csrproposal',
            name='impact_metrics',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='csrproposal',
            name='partnership_details',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='governancebody',
            name='description',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='governancebody',
            name='quorum_requirement',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='governancebody',
            name='terms_of_reference',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='governancemeeting',
            name='action_items',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='governancemeeting',
            name='agenda',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='governancemeeting',
            name='decisions_made',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='governancemeeting',
            name='minutes',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='governancereport',
            name='challenges_risks',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='governancereport',
            name='executive_summary',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='governancereport',
            name='financial_overview',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='governancereport',
            name='progress_overview',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='governancereport',
            name='recommendations',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='projecttimeline',
            name='description',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='resourceallocation',
            name='description',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='contingency_plan',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='description',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='fallback_strategy',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='riskassessment',
            name='mitigation_plan',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='teamrole',
            name='responsibilities',
            field=utils.fields.CustomRichTextField(blank=True),
        ),
    ]