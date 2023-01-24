# Generated by Django 3.2 on 2023-01-24 09:23

from django.db import migrations, models
import tasks.models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_taskattachment_attached_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workattachment',
            name='attached_file',
            field=models.FileField(max_length=1000, upload_to=tasks.models.WorkAttachment.filepath),
        ),
    ]
