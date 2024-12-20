# Generated by Django 5.0 on 2024-10-25 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('initiatives', '0002_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiversityMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_recorded', models.DateField(auto_now_add=True)),
                ('women_participants_count', models.PositiveIntegerField(default=0)),
                ('lgbtqia_participants_count', models.PositiveIntegerField(default=0)),
                ('marginalized_participants_count', models.PositiveIntegerField(default=0)),
                ('total_participants', models.PositiveIntegerField(default=0)),
                ('notes', models.TextField(blank=True)),
                ('initiative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diversity_metrics', to='initiatives.initiative')),
                ('recorded_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recorded_metrics', to='users.member')),
            ],
        ),
        migrations.CreateModel(
            name='CoCreationWorkshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('PLANNED', 'Planned'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed'), ('CANCELLED', 'Cancelled')], default='PLANNED', max_length=20)),
                ('total_participants', models.PositiveIntegerField(default=0)),
                ('women_count', models.PositiveIntegerField(default=0)),
                ('lgbtqia_count', models.PositiveIntegerField(default=0)),
                ('marginalized_count', models.PositiveIntegerField(default=0)),
                ('agenda', models.TextField()),
                ('outcomes', models.TextField(blank=True)),
                ('next_steps', models.TextField(blank=True)),
                ('materials_used', models.TextField(blank=True)),
                ('attachments', models.FileField(blank=True, upload_to='workshop_materials/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('facilitator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='facilitated_workshops', to='users.member')),
                ('initiative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cocreation_workshops', to='initiatives.initiative')),
            ],
            options={
                'ordering': ['-date'],
                'indexes': [models.Index(fields=['status'], name='program_des_status_f3dba2_idx'), models.Index(fields=['date'], name='program_des_date_1ac80a_idx')],
            },
        ),
        migrations.CreateModel(
            name='CulturalSensitivityAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audit_type', models.CharField(choices=[('PROGRAM', 'Program Audit'), ('COMMUNICATION', 'Communication Audit'), ('MATERIAL', 'Material Audit'), ('FEEDBACK', 'Feedback Analysis')], max_length=20)),
                ('audit_date', models.DateField()),
                ('findings', models.TextField()),
                ('recommendations', models.TextField()),
                ('action_items', models.TextField()),
                ('follow_up_date', models.DateField()),
                ('completion_status', models.BooleanField(default=False)),
                ('attachments', models.FileField(blank=True, upload_to='audit_documents/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('auditor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='conducted_audits', to='users.member')),
                ('initiative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensitivity_audits', to='initiatives.initiative')),
            ],
            options={
                'ordering': ['-audit_date'],
                'indexes': [models.Index(fields=['audit_type'], name='program_des_audit_t_dc0e2d_idx'), models.Index(fields=['completion_status'], name='program_des_complet_15b53d_idx')],
            },
        ),
        migrations.CreateModel(
            name='InclusionTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('training_type', models.CharField(choices=[('STEREOTYPE_BIAS', 'Understanding Stereotypes and Bias'), ('INCLUSIVE_COMM', 'Inclusive Communication'), ('CULTURAL_SENSITIVITY', 'Cultural Sensitivity'), ('CASE_STUDIES', 'Case Studies and Role Play')], max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('SCHEDULED', 'Scheduled'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed'), ('CANCELLED', 'Cancelled')], default='SCHEDULED', max_length=20)),
                ('description', models.TextField()),
                ('objectives', models.TextField()),
                ('materials', models.FileField(blank=True, upload_to='training_materials/')),
                ('feedback_summary', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('facilitator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='facilitated_trainings', to='users.member')),
                ('participants', models.ManyToManyField(related_name='attended_trainings', to='users.member')),
            ],
            options={
                'ordering': ['-start_date'],
                'indexes': [models.Index(fields=['training_type'], name='program_des_trainin_8e9789_idx'), models.Index(fields=['status'], name='program_des_status_0f60a3_idx')],
            },
        ),
        migrations.CreateModel(
            name='ProgramFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('CONTENT', 'Program Content'), ('DELIVERY', 'Program Delivery'), ('INCLUSION', 'Inclusivity'), ('CULTURAL', 'Cultural Sensitivity'), ('GENERAL', 'General Feedback')], max_length=20)),
                ('feedback_text', models.TextField()),
                ('submitted_by', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('is_anonymous', models.BooleanField(default=False)),
                ('expectations_met', models.BooleanField(default=True)),
                ('culturally_sensitive', models.BooleanField(default=True)),
                ('improvement_suggestions', models.TextField(blank=True)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('action_taken', models.TextField(blank=True)),
                ('initiative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='program_feedback', to='initiatives.initiative')),
                ('reviewed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviewed_feedback', to='users.member')),
            ],
            options={
                'ordering': ['-submitted_at'],
                'indexes': [models.Index(fields=['category'], name='program_des_categor_9e6d10_idx'), models.Index(fields=['submitted_at'], name='program_des_submitt_da8ff6_idx')],
            },
        ),
    ]
