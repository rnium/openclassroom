# Generated by Django 3.2 on 2023-01-24 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_work_submission_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
