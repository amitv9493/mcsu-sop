# Generated by Django 5.0 on 2024-11-08 20:11

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Industries',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('short_description', models.CharField(blank=True, max_length=255)),
                ('website', models.URLField(blank=True)),
                ('location', models.CharField(max_length=100)),
                ('established_date', models.DateField()),
                ('company_size', models.CharField(choices=[('1-10', '1-10 employees'), ('11-50', '11-50 employees'), ('51-200', '51-200 employees'), ('201-500', '201-500 employees'), ('501-1000', '501-1000 employees'), ('1001+', '1001+ employees')], max_length=50)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('logo', models.ImageField(blank=True, upload_to='company_logos/')),
                ('cover_image', models.ImageField(blank=True, upload_to='company_covers/')),
                ('linkedin_url', models.URLField(blank=True)),
                ('twitter_url', models.URLField(blank=True)),
                ('facebook_url', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('verification_documents', models.FileField(blank=True, upload_to='verification_docs/')),
                ('company_email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('registration_number', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('industry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job_portal.industry')),
            ],
            options={
                'verbose_name_plural': 'Companies',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('short_description', models.CharField(max_length=255)),
                ('requirements', models.TextField()),
                ('responsibilities', models.TextField()),
                ('benefits', models.TextField()),
                ('job_type', models.CharField(choices=[('FT', 'Full Time'), ('PT', 'Part Time'), ('CT', 'Contract'), ('IN', 'Internship'), ('RM', 'Remote'), ('FL', 'Freelance'), ('TP', 'Temporary')], max_length=2)),
                ('experience_level', models.CharField(choices=[('EN', 'Entry Level'), ('JR', 'Junior'), ('MD', 'Mid Level'), ('SR', 'Senior'), ('LD', 'Lead'), ('EX', 'Executive')], max_length=2)),
                ('experience_years_min', models.IntegerField()),
                ('experience_years_max', models.IntegerField()),
                ('education_requirement', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('is_remote', models.BooleanField(default=False)),
                ('salary_min', models.DecimalField(decimal_places=2, max_digits=10)),
                ('salary_max', models.DecimalField(decimal_places=2, max_digits=10)),
                ('salary_is_negotiable', models.BooleanField(default=False)),
                ('hide_salary', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('DR', 'Draft'), ('PN', 'Pending'), ('AC', 'Active'), ('PS', 'Paused'), ('CL', 'Closed'), ('EX', 'Expired')], default='DR', max_length=2)),
                ('is_featured', models.BooleanField(default=False)),
                ('posted_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('deadline', models.DateTimeField()),
                ('positions_available', models.IntegerField(default=1)),
                ('applications_count', models.IntegerField(default=0)),
                ('views_count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='job_portal.company')),
                ('industry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job_portal.industry')),
                ('skills_preferred', models.ManyToManyField(related_name='preferred_for_jobs', to='job_portal.skill')),
                ('skills_required', models.ManyToManyField(related_name='required_for_jobs', to='job_portal.skill')),
            ],
        ),
        migrations.CreateModel(
            name='JobAlert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(max_length=200)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('job_type', models.CharField(blank=True, choices=[('FT', 'Full Time'), ('PT', 'Part Time'), ('CT', 'Contract'), ('IN', 'Internship'), ('RM', 'Remote'), ('FL', 'Freelance'), ('TP', 'Temporary')], max_length=2)),
                ('min_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('frequency', models.CharField(choices=[('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly')], default='W', max_length=1)),
                ('is_active', models.BooleanField(default=True)),
                ('last_sent', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('industry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='job_portal.industry')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_alerts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(blank=True, upload_to='application_resumes/')),
                ('cover_letter', models.TextField()),
                ('status', models.CharField(choices=[('PD', 'Pending'), ('RV', 'Reviewing'), ('SC', 'Shortlisted'), ('IV', 'Interview Scheduled'), ('AC', 'Accepted'), ('RJ', 'Rejected'), ('WD', 'Withdrawn')], default='PD', max_length=2)),
                ('applied_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_viewed', models.BooleanField(default=False)),
                ('viewed_date', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True)),
                ('expected_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('reference', models.CharField(blank=True, max_length=100)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='job_portal.job')),
            ],
            options={
                'ordering': ['-applied_date'],
            },
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_type', models.CharField(choices=[('PH', 'Phone'), ('VI', 'Video'), ('F2F', 'Face to Face'), ('TS', 'Technical Screen'), ('AS', 'Assignment')], max_length=3)),
                ('scheduled_date', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('location', models.CharField(blank=True, max_length=200)),
                ('meeting_link', models.URLField(blank=True)),
                ('status', models.CharField(choices=[('SC', 'Scheduled'), ('IP', 'In Progress'), ('CM', 'Completed'), ('CN', 'Cancelled'), ('RS', 'Rescheduled')], default='SC', max_length=2)),
                ('feedback', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('interviewer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='conducted_interviews', to=settings.AUTH_USER_MODEL)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interviews', to='job_portal.jobapplication')),
            ],
            options={
                'ordering': ['scheduled_date'],
            },
        ),
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('assessment_type', models.CharField(choices=[('SK', 'Skills Test'), ('PS', 'Problem Solving'), ('PG', 'Programming'), ('LG', 'Language'), ('PS', 'Personality'), ('CT', 'Custom')], max_length=2)),
                ('description', models.TextField()),
                ('instructions', models.TextField()),
                ('duration', models.DurationField(blank=True, null=True)),
                ('deadline', models.DateTimeField()),
                ('is_completed', models.BooleanField(default=False)),
                ('completion_date', models.DateTimeField(blank=True, null=True)),
                ('score', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('feedback', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessments', to='job_portal.jobapplication')),
            ],
        ),
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('resume', models.FileField(blank=True, upload_to='resumes/')),
                ('cover_letter_template', models.TextField(blank=True)),
                ('experience_years', models.DecimalField(decimal_places=1, max_digits=4)),
                ('education', models.TextField()),
                ('preferred_job_types', models.CharField(max_length=100)),
                ('preferred_locations', models.CharField(max_length=200)),
                ('expected_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('linkedin_url', models.URLField(blank=True)),
                ('portfolio_url', models.URLField(blank=True)),
                ('github_url', models.URLField(blank=True)),
                ('is_available', models.BooleanField(default=True)),
                ('profile_visibility', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('preferred_industries', models.ManyToManyField(to='job_portal.industry')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='job_portal.jobseeker'),
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_current', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='job_portal.jobseeker')),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('field_of_study', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_current', models.BooleanField(default=False)),
                ('gpa', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='job_portal.jobseeker')),
            ],
            options={
                'verbose_name_plural': 'Education',
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='JobSeekerPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferred_job_types', models.CharField(blank=True, max_length=100)),
                ('preferred_locations', models.CharField(blank=True, max_length=200)),
                ('min_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('is_open_to_remote', models.BooleanField(default=True)),
                ('is_willing_to_relocate', models.BooleanField(default=False)),
                ('notice_period', models.IntegerField(blank=True, help_text='Notice period in days', null=True)),
                ('job_search_status', models.CharField(choices=[('active', 'Actively Looking'), ('passive', 'Passively Looking'), ('not_looking', 'Not Looking')], default='active', max_length=20)),
                ('job_seeker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='preferences', to='job_portal.jobseeker')),
                ('preferred_industries', models.ManyToManyField(blank=True, to='job_portal.industry')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('read_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL)),
                ('related_job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='job_portal.job')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(choices=[('AP', 'Application Update'), ('IV', 'Interview Schedule'), ('JB', 'New Job Match'), ('MS', 'Message'), ('AS', 'Assessment'), ('SY', 'System')], max_length=2)),
                ('title', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('link', models.URLField(blank=True)),
                ('is_read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='JobSeekerSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proficiency_level', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced'), ('expert', 'Expert')], max_length=20)),
                ('years_of_experience', models.DecimalField(decimal_places=1, max_digits=4)),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_portal.jobseeker')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_portal.skill')),
            ],
            options={
                'unique_together': {('job_seeker', 'skill')},
            },
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='skills',
            field=models.ManyToManyField(through='job_portal.JobSeekerSkill', to='job_portal.skill'),
        ),
        migrations.CreateModel(
            name='CompanyFollower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed_date', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='job_portal.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_companies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('company', 'user')},
            },
        ),
        migrations.CreateModel(
            name='CompanyReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('title', models.CharField(max_length=200)),
                ('review_text', models.TextField()),
                ('pros', models.TextField()),
                ('cons', models.TextField()),
                ('is_anonymous', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('helpful_votes', models.IntegerField(default=0)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='job_portal.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('company', 'user')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='jobapplication',
            unique_together={('job', 'applicant')},
        ),
        migrations.CreateModel(
            name='SavedJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_date', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_portal.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-saved_date'],
                'unique_together': {('user', 'job')},
            },
        ),
    ]