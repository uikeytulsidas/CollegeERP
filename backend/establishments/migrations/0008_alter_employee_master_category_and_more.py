# Generated by Django 4.2.19 on 2025-03-04 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_remove_department_institute_and_more'),
        ('establishments', '0007_alter_employee_master_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_master',
            name='CATEGORY',
            field=models.ForeignKey(db_column='CATEGORY_ID', default=1, on_delete=django.db.models.deletion.PROTECT, to='accounts.category'),
        ),
        migrations.AlterField(
            model_name='employee_master',
            name='DEPARTMENT',
            field=models.ForeignKey(db_column='DEPARTMENT_ID', default=1, on_delete=django.db.models.deletion.PROTECT, to='accounts.department'),
        ),
        migrations.AlterField(
            model_name='employee_master',
            name='DESIGNATION',
            field=models.ForeignKey(db_column='DESIGNATION_ID', default=1, on_delete=django.db.models.deletion.PROTECT, to='accounts.designation'),
        ),
        migrations.AlterField(
            model_name='employee_master',
            name='EMP_TYPE',
            field=models.ForeignKey(db_column='EMP_TYPE_ID', default=1, on_delete=django.db.models.deletion.PROTECT, related_name='employees_type', to='establishments.type_master'),
        ),
        migrations.AlterField(
            model_name='employee_master',
            name='MARITAL_STATUS',
            field=models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('other', 'Other')], db_column='MARITAL_STATUS', default='single', max_length=10),
        ),
        migrations.AlterField(
            model_name='employee_master',
            name='SHIFT',
            field=models.ForeignKey(db_column='SHIFT', default=1, on_delete=django.db.models.deletion.PROTECT, to='establishments.shift_master'),
        ),
        migrations.AlterField(
            model_name='employee_master',
            name='STATUS',
            field=models.ForeignKey(db_column='STATUS_ID', default=1, on_delete=django.db.models.deletion.PROTECT, related_name='employees_status', to='establishments.status_master'),
        ),
    ]
