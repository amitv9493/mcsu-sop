# Generated by Django 5.0 on 2024-10-25 11:53

import django.core.validators
import initiatives.models
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrainstormingSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_type', models.CharField(choices=[('INTERNAL', 'Internal Team'), ('COMMUNITY', 'Community Leaders'), ('STAKEHOLDER', 'Stakeholder Workshop'), ('FGD', 'Focus Group Discussion')], max_length=20)),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('participants_count', models.PositiveIntegerField()),
                ('agenda', models.TextField()),
                ('summary', models.TextField()),
                ('key_outcomes', models.TextField()),
                ('next_steps', models.TextField()),
                ('notes', models.TextField(blank=True)),
                ('materials_used', models.TextField(blank=True, help_text='List materials used in the session')),
                ('attachments', models.FileField(blank=True, upload_to='brainstorming_docs/', validators=[initiatives.models.validate_file_size])),
                ('feedback_summary', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_type', models.CharField(choices=[('OPERATIONAL', 'Operational'), ('CAPITAL', 'Capital'), ('PROGRAM', 'Program'), ('EMERGENCY', 'Emergency')], max_length=20)),
                ('item_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('estimated_amount', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('actual_amount', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('unit_cost', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('variance_explanation', models.TextField(blank=True)),
                ('date_required', models.DateField()),
                ('approval_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['date_required'],
            },
        ),
        migrations.CreateModel(
            name='CommunityFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_type', models.CharField(choices=[('SURVEY', 'Survey Response'), ('SUGGESTION', 'Suggestion Box'), ('VERBAL', 'Verbal Feedback'), ('ONLINE', 'Online Portal')], max_length=20)),
                ('feedback_date', models.DateField(auto_now_add=True)),
                ('feedback_text', models.TextField()),
                ('submitted_by', models.CharField(blank=True, help_text='Optional: Name of person providing feedback', max_length=100)),
                ('contact_info', models.CharField(blank=True, help_text='Optional: Contact information', max_length=100)),
                ('category', models.CharField(help_text='Category of feedback (e.g., Services, Facilities)', max_length=100)),
                ('priority', models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')], default='MEDIUM', max_length=20)),
                ('status', models.CharField(choices=[('NEW', 'New'), ('IN_REVIEW', 'In Review'), ('ADDRESSED', 'Addressed'), ('CLOSED', 'Closed')], default='NEW', max_length=20)),
                ('response_text', models.TextField(blank=True)),
                ('response_date', models.DateField(blank=True, null=True)),
                ('is_anonymous', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CommunityMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=255)),
                ('population_size', models.PositiveIntegerField()),
                ('demographic_data', models.TextField(help_text='Detailed breakdown of community demographics')),
                ('existing_services', models.TextField(help_text='List of current services in the area')),
                ('key_stakeholders', models.TextField(help_text='Important community leaders and organizations')),
                ('challenges', models.TextField(help_text='Main challenges faced by the community')),
                ('opportunities', models.TextField(help_text='Potential opportunities for intervention')),
                ('resources_available', models.TextField()),
                ('map_file', models.FileField(blank=True, upload_to='community_maps/', validators=[initiatives.models.validate_file_size])),
                ('mapping_date', models.DateField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('event_type', models.CharField(choices=[('WORKSHOP', 'Workshop'), ('SEMINAR', 'Seminar'), ('TRAINING', 'Training'), ('COMMUNITY', 'Community Event'), ('MEETING', 'Stakeholder Meeting')], max_length=20)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('virtual_meeting_link', models.URLField(blank=True)),
                ('status', models.CharField(choices=[('PLANNED', 'Planned'), ('CONFIRMED', 'Confirmed'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed'), ('CANCELLED', 'Cancelled')], default='PLANNED', max_length=20)),
                ('max_participants', models.PositiveIntegerField()),
                ('current_participants', models.PositiveIntegerField(default=0)),
                ('agenda', models.TextField()),
                ('resources_needed', models.TextField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('actual_spend', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('feedback_summary', models.TextField(blank=True)),
                ('materials', models.FileField(blank=True, upload_to='event_materials/', validators=[initiatives.models.validate_file_size])),
                ('photos', models.FileField(blank=True, upload_to='event_photos/', validators=[initiatives.models.validate_file_size])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='ExecutionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('activity', models.TextField()),
                ('outcomes', models.TextField()),
                ('challenges', models.TextField(blank=True)),
                ('photos', models.FileField(blank=True, upload_to='execution_photos/', validators=[initiatives.models.validate_file_size])),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('feedback_text', models.TextField()),
                ('suggestions', models.TextField(blank=True)),
                ('would_recommend', models.BooleanField(default=True)),
                ('areas_of_improvement', models.TextField(blank=True)),
                ('is_anonymous', models.BooleanField(default=False)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-submitted_at'],
            },
        ),
        migrations.CreateModel(
            name='Initiative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('start_date', models.DateField(help_text='Format: YYYY-MM-DD')),
                ('end_date', models.DateField(help_text='Format: YYYY-MM-DD')),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('actual_spend', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('status', models.CharField(choices=[('PLANNED', 'Planned'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed'), ('ON_HOLD', 'On Hold'), ('CANCELLED', 'Cancelled')], default='PLANNED', max_length=20)),
                ('sdg_alignment', models.CharField(choices=[('SDG_1', 'No Poverty'), ('SDG_2', 'Zero Hunger'), ('SDG_3', 'Good Health and Well-being'), ('SDG_4', 'Quality Education'), ('SDG_5', 'Gender Equality'), ('SDG_6', 'Clean Water and Sanitation'), ('SDG_7', 'Affordable and Clean Energy'), ('SDG_8', 'Decent Work and Economic Growth'), ('SDG_9', 'Industry, Innovation and Infrastructure'), ('SDG_10', 'Reduced Inequalities'), ('SDG_11', 'Sustainable Cities and Communities'), ('SDG_12', 'Responsible Consumption and Production'), ('SDG_13', 'Climate Action'), ('SDG_14', 'Life Below Water'), ('SDG_15', 'Life on Land'), ('SDG_16', 'Peace, Justice and Strong Institutions'), ('SDG_17', 'Partnerships for the Goals')], max_length=50)),
                ('target_beneficiaries', models.TextField(help_text='Describe the target groups and expected impact')),
                ('success_metrics', models.TextField(help_text='Define how success will be measured')),
                ('challenges_faced', models.TextField(blank=True)),
                ('lessons_learned', models.TextField(blank=True)),
                ('attachments', models.FileField(blank=True, upload_to='initiative_docs/', validators=[initiatives.models.validate_file_size])),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='KPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('target_value', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('current_value', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('unit_of_measure', models.CharField(max_length=50)),
                ('measurement_frequency', models.CharField(choices=[('DAILY', 'Daily'), ('WEEKLY', 'Weekly'), ('MONTHLY', 'Monthly'), ('QUARTERLY', 'Quarterly'), ('YEARLY', 'Yearly')], max_length=20)),
                ('data_source', models.TextField(help_text='Where and how is this KPI measured?')),
                ('baseline_value', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('target_date', models.DateField()),
                ('achieved', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'KPI',
                'verbose_name_plural': 'KPIs',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('target_date', models.DateField()),
                ('actual_completion_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed'), ('DELAYED', 'Delayed')], default='PENDING', max_length=20)),
                ('deliverables', models.TextField()),
                ('progress', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['target_date'],
            },
        ),
        migrations.CreateModel(
            name='NeedsAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_group', models.CharField(max_length=100)),
                ('identified_need', models.TextField()),
                ('priority_level', models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')], default='MEDIUM', max_length=20)),
                ('current_services', models.TextField(help_text='Describe existing services addressing this need')),
                ('service_gaps', models.TextField(help_text='Identify gaps in current services')),
                ('proposed_solution', models.TextField()),
                ('required_resources', models.TextField()),
                ('estimated_budget', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('implementation_timeline', models.TextField()),
                ('success_indicators', models.TextField()),
                ('data_sources', models.TextField(help_text='Sources of information for this analysis')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_type', models.CharField(choices=[('FINANCIAL', 'Financial Risk'), ('OPERATIONAL', 'Operational Risk'), ('STRATEGIC', 'Strategic Risk'), ('COMPLIANCE', 'Compliance Risk'), ('REPUTATION', 'Reputational Risk'), ('SAFETY', 'Safety Risk')], max_length=20)),
                ('description', models.TextField()),
                ('risk_level', models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High'), ('CRITICAL', 'Critical')], max_length=20)),
                ('probability', models.IntegerField(help_text='1 (Very Unlikely) to 5 (Very Likely)', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('impact', models.IntegerField(help_text='1 (Minimal Impact) to 5 (Severe Impact)', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('mitigation_plan', models.TextField()),
                ('contingency_plan', models.TextField()),
                ('status', models.CharField(choices=[('IDENTIFIED', 'Identified'), ('ASSESSED', 'Assessed'), ('MITIGATED', 'Mitigated'), ('CLOSED', 'Closed'), ('OCCURRED', 'Risk Occurred')], default='IDENTIFIED', max_length=20)),
                ('review_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-risk_level', '-probability'],
            },
        ),
        migrations.CreateModel(
            name='Stakeholder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('organization_type', models.CharField(choices=[('NGO', 'Non-Governmental Organization'), ('GOVT', 'Government Body'), ('CORP', 'Corporate Partner'), ('COMM', 'Community Organization'), ('ACAD', 'Academic Institution')], max_length=20)),
                ('contact_person', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('involvement_level', models.CharField(choices=[('HIGH', 'High'), ('MEDIUM', 'Medium'), ('LOW', 'Low')], default='MEDIUM', max_length=20)),
                ('resources_provided', models.TextField(blank=True)),
                ('expectations', models.TextField(blank=True)),
                ('contribution_type', models.TextField(help_text='How the stakeholder contributes to initiatives')),
                ('notes', models.TextField(blank=True)),
                ('last_contact', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('priority', models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High'), ('URGENT', 'Urgent')], default='MEDIUM', max_length=20)),
                ('status', models.CharField(choices=[('TODO', 'To Do'), ('IN_PROGRESS', 'In Progress'), ('REVIEW', 'Under Review'), ('COMPLETED', 'Completed'), ('ON_HOLD', 'On Hold')], default='TODO', max_length=20)),
                ('start_date', models.DateField()),
                ('due_date', models.DateField()),
                ('completion_date', models.DateField(blank=True, null=True)),
                ('progress', models.PositiveIntegerField(default=0, help_text='Progress percentage', validators=[django.core.validators.MaxValueValidator(100)])),
                ('comments', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]