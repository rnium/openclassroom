# Generated by Django 3.2 on 2023-01-24 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='instruction',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]