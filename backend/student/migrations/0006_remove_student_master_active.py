# Generated by Django 4.2.7 on 2025-03-25 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_remove_student_master_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_master',
            name='ACTIVE',
        ),
    ]
