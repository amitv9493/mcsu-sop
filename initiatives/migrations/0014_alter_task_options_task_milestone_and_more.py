# Generated by Django 4.2.16 on 2024-11-21 20:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_department_description_and_more'),
        ('initiatives', '0013_alter_milestone_deliverables'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['due_date', 'priority'], 'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
        migrations.AddField(
            model_name='task',
            name='milestone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='milestone_tasks', to='initiatives.milestone'),
        ),
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_tasks', to='users.member'),
        ),
        migrations.AlterField(
            model_name='task',
            name='comments',
            field=models.TextField(blank=True, help_text='Additional notes or comments about the task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='dependencies',
            field=models.ManyToManyField(blank=True, related_name='dependent_tasks', to='initiatives.task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=utils.fields.CustomRichTextField(blank=True, help_text='Detailed description of the task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(help_text='When should this task be completed?'),
        ),
        migrations.AlterField(
            model_name='task',
            name='initiative',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initiative_tasks', to='initiatives.initiative'),
        ),
        migrations.AlterField(
            model_name='task',
            name='progress',
            field=models.PositiveIntegerField(default=0, help_text='Progress percentage (0-100)', validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(help_text='When should this task begin?'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(help_text='Enter the task title', max_length=255),
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['status'], name='initiatives_status_a1ade1_idx'),
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['priority'], name='initiatives_priorit_87c034_idx'),
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['due_date'], name='initiatives_due_dat_1b9c9e_idx'),
        ),
    ]
