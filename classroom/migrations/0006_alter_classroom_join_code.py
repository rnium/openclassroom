# Generated by Django 3.2 on 2023-02-16 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_classroom_join_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='join_code',
            field=models.CharField(max_length=10),
        ),
    ]