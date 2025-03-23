# Generated by Django 4.2.19 on 2025-03-23 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_delete_student_master_alter_dashboard_master_emp_id'),
        ('student', '0002_alter_student_created_by_alter_student_deleted_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='STUDENT_MASTER',
            fields=[
                ('CREATED_BY', models.CharField(blank=True, db_column='CREATED_BY', max_length=50, null=True)),
                ('CREATED_AT', models.DateTimeField(auto_now_add=True, db_column='CREATED_AT')),
                ('UPDATED_BY', models.CharField(blank=True, db_column='UPDATED_BY', max_length=50, null=True)),
                ('UPDATED_AT', models.DateTimeField(auto_now=True, db_column='UPDATED_AT')),
                ('DELETED_BY', models.CharField(blank=True, db_column='DELETED_BY', max_length=50, null=True)),
                ('DELETED_AT', models.DateTimeField(blank=True, db_column='DELETED_AT', null=True)),
                ('IS_DELETED', models.BooleanField(db_column='IS_DELETED', default=False)),
                ('RECORD_ID', models.AutoField(db_column='RECORD_ID', primary_key=True, serialize=False)),
                ('STUDENT_ID', models.CharField(db_column='STUDENT_ID', max_length=20, unique=True)),
                ('INSTITUTE', models.CharField(db_column='INSTITUTE_CODE', max_length=20)),
                ('ACADEMIC_YEAR', models.CharField(db_column='ACADEMIC_YEAR', max_length=10)),
                ('BATCH', models.CharField(db_column='BATCH', max_length=10)),
                ('ADMISSION_CATEGORY', models.CharField(db_column='ADMISSION_CATEGORY', max_length=20)),
                ('FORM_NO', models.IntegerField(db_column='FORM_NO')),
                ('VALIDITY', models.DateField(db_column='VALIDITY')),
                ('NAME_ON_CERTIFICATE', models.CharField(db_column='NAME_ON_CERTIFICATE', max_length=100)),
                ('NAME', models.CharField(db_column='NAME', max_length=100)),
                ('SURNAME', models.CharField(db_column='SURNAME', max_length=100)),
                ('PARENT_NAME', models.CharField(db_column='PARENT_NAME', max_length=100)),
                ('MOTHER_NAME', models.CharField(db_column='MOTHER_NAME', max_length=100)),
                ('FATHER_NAME', models.CharField(db_column='FATHER_NAME', max_length=100)),
                ('GENDER', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], db_column='GENDER', max_length=10)),
                ('DOB', models.DateField(db_column='DOB')),
                ('DOP', models.DateField(blank=True, db_column='DOP', null=True)),
                ('PER_ADDRESS', models.TextField(db_column='PER_ADDRESS')),
                ('LOC_ADDRESS', models.TextField(db_column='LOC_ADDRESS')),
                ('PER_STATE_ID', models.IntegerField(db_column='PER_STATE_ID')),
                ('LOC_STATE_ID', models.IntegerField(db_column='LOC_STATE_ID')),
                ('PER_PHONE_NO', models.CharField(db_column='PER_PHONE_NO', max_length=15)),
                ('LOC_PHONE_NO', models.CharField(db_column='LOC_PHONE_NO', max_length=15)),
                ('MOB_NO', models.CharField(db_column='MOB_NO', max_length=15)),
                ('EMAIL_ID', models.EmailField(db_column='EMAIL_ID', max_length=254)),
                ('PER_CITY', models.CharField(db_column='PER_CITY', max_length=50)),
                ('LOC_CITY', models.CharField(db_column='LOC_CITY', max_length=50)),
                ('NATIONALITY', models.CharField(db_column='NATIONALITY', max_length=50)),
                ('BLOOD_GR', models.CharField(db_column='BLOOD_GR', max_length=5)),
                ('CASTE', models.CharField(db_column='CASTE', max_length=50)),
                ('ENROLMENT_NO', models.CharField(db_column='ENROLMENT_NO', max_length=20)),
                ('IS_ACTIVE', models.CharField(db_column='IS_ACTIVE', default=True, max_length=3)),
                ('HANDICAPPED', models.CharField(db_column='HANDICAPPED', max_length=3)),
                ('MARK_ID', models.CharField(db_column='MARK_ID', max_length=20)),
                ('ADMISSION_DATE', models.DateField(db_column='ADMISSION_DATE')),
                ('QUOTA_ID', models.IntegerField(db_column='QUOTA_ID')),
                ('ENTRYPERSON', models.CharField(db_column='ENTRYPERSON', max_length=100)),
                ('DATEOFENTRY', models.DateField(auto_now_add=True, db_column='DATEOFENTRY')),
                ('DATEOFEDIT', models.DateField(auto_now=True, db_column='DATEOFEDIT')),
                ('PER_PIN', models.CharField(db_column='PER_PIN', max_length=6)),
                ('LOC_PIN', models.CharField(db_column='LOC_PIN', max_length=6)),
                ('YEAR_SEM_ID', models.IntegerField(db_column='YEAR_SEM_ID')),
                ('DATE_LEAVING', models.DateField(blank=True, db_column='DATE_LEAVING', null=True)),
                ('RELIGION', models.CharField(db_column='RELIGION', max_length=50)),
                ('DOB_WORD', models.CharField(db_column='DOB_WORD', max_length=100)),
                ('ADMN_ROUND', models.CharField(db_column='ADMN_ROUND', max_length=10)),
                ('BANK_NAME', models.CharField(db_column='BANK_NAME', max_length=100)),
                ('BANK_ACC_NO', models.CharField(db_column='BANK_ACC_NO', max_length=20)),
                ('EMERGENCY_NO', models.CharField(db_column='EMERGENCY_NO', max_length=15)),
                ('PER_TALUKA', models.CharField(db_column='PER_TALUKA', max_length=50)),
                ('PER_DIST', models.CharField(db_column='PER_DIST', max_length=50)),
                ('LOC_TALUKA', models.CharField(db_column='LOC_TALUKA', max_length=50)),
                ('LOC_DIST', models.CharField(db_column='LOC_DIST', max_length=50)),
                ('EDITPERSON', models.CharField(db_column='EDITPERSON', max_length=100)),
                ('ADMN_QUOTA_ID', models.IntegerField(db_column='ADMN_QUOTA_ID', default=0)),
                ('STATUS', models.CharField(db_column='STATUS', max_length=20)),
                ('JOINING_STATUS', models.CharField(db_column='JOINING_STATUS', max_length=20)),
                ('REGISTRATION_DATE', models.DateField(db_column='REGISTRATION_DATE')),
                ('LATERAL_STATUS', models.CharField(db_column='LATERAL_STATUS', max_length=20)),
                ('JOINING_STATUS_DATE', models.DateField(db_column='JOINING_STATUS_DATE')),
                ('RETENTION_STATUS_DATE', models.DateField(db_column='RETENTION_STATUS_DATE')),
                ('BRANCH_ID', models.ForeignKey(db_column='BRANCH_ID', on_delete=django.db.models.deletion.PROTECT, to='accounts.branch')),
            ],
            options={
                'verbose_name': 'Student Master',
                'verbose_name_plural': 'Student Masters',
                'db_table': '"STUDENT"."STUDENT_MASTER"',
                'indexes': [models.Index(fields=['STUDENT_ID'], name='STUDENT_MAS_STUDENT_d6572a_idx'), models.Index(fields=['EMAIL_ID'], name='STUDENT_MAS_EMAIL_I_635c12_idx'), models.Index(fields=['MOB_NO'], name='STUDENT_MAS_MOB_NO_ab0b9c_idx')],
            },
        ),
    ]
