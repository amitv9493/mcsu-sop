# Generated by Django 5.0 on 2024-10-25 11:53

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import users.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('initiatives', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_type', models.CharField(choices=[('ASSOCIATE', 'Associate Member'), ('REGULAR', 'Regular Member'), ('SENIOR', 'Senior Member'), ('HONORARY', 'Honorary Member')], max_length=20)),
                ('join_date', models.DateField(default=django.utils.timezone.now)),
                ('skills', models.TextField(blank=True, help_text='Comma-separated list of skills')),
                ('certifications', models.TextField(blank=True, help_text='List relevant certifications with dates')),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'), ('SUSPENDED', 'Suspended'), ('ALUMNI', 'Alumni')], default='ACTIVE', max_length=20)),
                ('bio', models.TextField(blank=True, help_text='Brief introduction about yourself')),
                ('linkedin_profile', models.URLField(blank=True)),
                ('github_profile', models.URLField(blank=True)),
                ('profile_picture', models.ImageField(blank=True, upload_to='member_profiles/', validators=[users.models.validate_file_size])),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('emergency_contact', models.CharField(blank=True, max_length=100)),
                ('emergency_phone', models.CharField(blank=True, max_length=15)),
                ('last_active', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='member_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-join_date'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('established_on', models.DateField()),
                ('vision', models.TextField(blank=True)),
                ('mission', models.TextField(blank=True)),
                ('budget_allocation', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('contact_email', models.EmailField(blank=True, max_length=254)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('head', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='headed_departments', to='users.member')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CoreCommittee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('CHAIR', 'Chairperson'), ('VICE_CHAIR', 'Vice Chairperson'), ('SECRETARY', 'Secretary'), ('TREASURER', 'Treasurer'), ('DEPT_HEAD', 'Department Head'), ('TECHNICAL_LEAD', 'Technical Lead'), ('EVENT_COORDINATOR', 'Event Coordinator'), ('PR_COORDINATOR', 'PR Coordinator')], max_length=20)),
                ('term_start', models.DateField()),
                ('term_end', models.DateField(validators=[users.models.validate_future_end_date])),
                ('responsibilities', models.TextField(blank=True)),
                ('achievements', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('handover_notes', models.TextField(blank=True, help_text='Notes for the next person taking this role')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='committee_positions', to='users.member')),
            ],
            options={
                'verbose_name': 'Core Committee Member',
                'verbose_name_plural': 'Core Committee Members',
                'ordering': ['term_end'],
            },
        ),
        migrations.CreateModel(
            name='StudentVolunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('phone_no', models.CharField(max_length=15)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('university_name', models.CharField(max_length=200)),
                ('current_semester', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('work_duration_months', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('university_permission', models.BooleanField(default=False)),
                ('resume', models.FileField(blank=True, upload_to='student_resumes/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx']), users.models.validate_file_size])),
                ('photograph', models.ImageField(blank=True, upload_to='student_photos/', validators=[users.models.validate_file_size])),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected'), ('ACTIVE', 'Active'), ('COMPLETED', 'Completed')], default='PENDING', max_length=20)),
                ('skills', models.TextField(blank=True)),
                ('interests', models.TextField(blank=True)),
                ('availability', models.TextField(blank=True, help_text='Specify your available hours and days')),
                ('emergency_contact', models.CharField(blank=True, max_length=100)),
                ('emergency_phone', models.CharField(blank=True, max_length=15)),
                ('approval_date', models.DateTimeField(blank=True, null=True)),
                ('rejection_reason', models.TextField(blank=True)),
                ('completion_certificate', models.FileField(blank=True, upload_to='completion_certificates/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf']), users.models.validate_file_size])),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_volunteers', to='users.member')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_volunteers', to='users.department')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_volunteers', to='initiatives.event')),
                ('initiative', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_volunteers', to='initiatives.initiative')),
            ],
            options={
                'verbose_name': 'Student Volunteer',
                'verbose_name_plural': 'Student Volunteers',
                'ordering': ['-application_date'],
            },
        ),
        migrations.AddIndex(
            model_name='member',
            index=models.Index(fields=['member_type'], name='users_membe_member__1a1ac9_idx'),
        ),
        migrations.AddIndex(
            model_name='member',
            index=models.Index(fields=['status'], name='users_membe_status_df765a_idx'),
        ),
        migrations.AddIndex(
            model_name='department',
            index=models.Index(fields=['is_active'], name='users_depar_is_acti_1b6176_idx'),
        ),
        migrations.AddIndex(
            model_name='corecommittee',
            index=models.Index(fields=['role'], name='users_corec_role_a376e9_idx'),
        ),
        migrations.AddIndex(
            model_name='corecommittee',
            index=models.Index(fields=['is_active'], name='users_corec_is_acti_7ec4da_idx'),
        ),
        migrations.AddIndex(
            model_name='studentvolunteer',
            index=models.Index(fields=['status'], name='users_stude_status_34b8cc_idx'),
        ),
        migrations.AddIndex(
            model_name='studentvolunteer',
            index=models.Index(fields=['application_date'], name='users_stude_applica_95f0fe_idx'),
        ),
    ]