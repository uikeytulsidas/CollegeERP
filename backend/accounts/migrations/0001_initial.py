# Generated by Django 4.2.19 on 2025-02-17 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('DELETED_AT', models.DateTimeField(blank=True, db_column='DELETED_AT', null=True)),
                ('IS_DELETED', models.BooleanField(db_column='IS_DELETED', default=False)),
                ('USER_ID', models.CharField(db_column='USER_ID', max_length=20, primary_key=True, serialize=False)),
                ('USERNAME', models.CharField(db_column='USERNAME', max_length=150, unique=True)),
                ('PASSWORD', models.CharField(db_column='PASSWORD', max_length=128)),
                ('EMAIL', models.EmailField(db_column='EMAIL', max_length=254, unique=True)),
                ('FIRST_NAME', models.CharField(db_column='FIRST_NAME', max_length=150)),
                ('LAST_NAME', models.CharField(db_column='LAST_NAME', max_length=150)),
                ('PHONE_NUMBER', models.CharField(blank=True, db_column='PHONE_NUMBER', max_length=15, null=True)),
                ('PROFILE_PICTURE', models.ImageField(blank=True, db_column='PROFILE_PICTURE', null=True, upload_to='profile_pics/')),
                ('IS_ACTIVE', models.BooleanField(db_column='IS_ACTIVE', default=True)),
                ('IS_STAFF', models.BooleanField(db_column='IS_STAFF', default=False)),
                ('IS_SUPERUSER', models.BooleanField(db_column='IS_SUPERUSER', default=False)),
                ('IS_EMAIL_VERIFIED', models.BooleanField(db_column='IS_EMAIL_VERIFIED', default=False)),
                ('CREATED_AT', models.DateTimeField(auto_now_add=True, db_column='CREATED_AT')),
                ('UPDATED_AT', models.DateTimeField(auto_now=True, db_column='UPDATED_AT')),
                ('LAST_LOGIN', models.DateTimeField(blank=True, db_column='LAST_LOGIN', null=True)),
                ('LAST_LOGIN_IP', models.GenericIPAddressField(blank=True, db_column='LAST_LOGIN_IP', null=True)),
                ('LAST_LOGIN_ATTEMPT', models.DateTimeField(blank=True, db_column='LAST_LOGIN_ATTEMPT', null=True)),
                ('FAILED_LOGIN_ATTEMPTS', models.IntegerField(db_column='FAILED_LOGIN_ATTEMPTS', default=0)),
                ('IS_LOCKED', models.BooleanField(db_column='IS_LOCKED', default=False)),
                ('LOCKED_UNTIL', models.DateTimeField(blank=True, db_column='LOCKED_UNTIL', null=True)),
                ('PASSWORD_CHANGED_AT', models.DateTimeField(blank=True, db_column='PASSWORD_CHANGED_AT', null=True)),
                ('OTP_SECRET', models.CharField(blank=True, db_column='OTP_SECRET', max_length=16, null=True)),
                ('OTP_CREATED_AT', models.DateTimeField(blank=True, db_column='OTP_CREATED_AT', null=True)),
                ('OTP_ATTEMPTS', models.IntegerField(db_column='OTP_ATTEMPTS', default=0)),
                ('OTP_VERIFIED', models.BooleanField(db_column='OTP_VERIFIED', default=False)),
                ('MAX_OTP_TRY', models.IntegerField(db_column='MAX_OTP_TRY', default=3)),
                ('OTP_BLOCKED_UNTIL', models.DateTimeField(blank=True, db_column='OTP_BLOCKED_UNTIL', null=True)),
                ('CREATED_BY', models.ForeignKey(blank=True, db_column='CREATED_BY', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('DELETED_BY', models.ForeignKey(blank=True, db_column='DELETED_BY', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_deleted', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'USERS',
                'ordering': ['USER_ID'],
            },
        ),
        migrations.CreateModel(
            name='DESIGNATION',
            fields=[
                ('DELETED_AT', models.DateTimeField(blank=True, db_column='DELETED_AT', null=True)),
                ('IS_DELETED', models.BooleanField(db_column='IS_DELETED', default=False)),
                ('DESIGNATION_ID', models.AutoField(db_column='DESIGNATION_ID', primary_key=True, serialize=False)),
                ('NAME', models.CharField(db_column='NAME', max_length=50, unique=True)),
                ('CODE', models.CharField(db_column='CODE', max_length=20, unique=True)),
                ('DESCRIPTION', models.TextField(blank=True, db_column='DESCRIPTION', null=True)),
                ('PERMISSIONS', models.JSONField(db_column='PERMISSIONS', default=dict, help_text='Define permissions like {"module_name": {"action": bool}}')),
                ('IS_ACTIVE', models.BooleanField(db_column='IS_ACTIVE', default=True)),
                ('CREATED_AT', models.DateTimeField(auto_now_add=True, db_column='CREATED_AT')),
                ('UPDATED_AT', models.DateTimeField(auto_now=True, db_column='UPDATED_AT')),
                ('CREATED_BY', models.ForeignKey(blank=True, db_column='CREATED_BY', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('DELETED_BY', models.ForeignKey(blank=True, db_column='DELETED_BY', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_deleted', to=settings.AUTH_USER_MODEL)),
                ('UPDATED_BY', models.ForeignKey(blank=True, db_column='UPDATED_BY', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Designation',
                'verbose_name_plural': 'Designations',
                'db_table': 'DESIGNATIONS',
            },
        ),
        migrations.CreateModel(
            name='USER_HISTORY',
            fields=[
                ('HISTORY_ID', models.AutoField(db_column='HISTORY_ID', primary_key=True, serialize=False)),
                ('ACTION', models.CharField(db_column='ACTION', max_length=10)),
                ('ACTION_AT', models.DateTimeField(auto_now_add=True, db_column='ACTION_AT')),
                ('OLD_DATA', models.JSONField(blank=True, db_column='OLD_DATA', null=True)),
                ('NEW_DATA', models.JSONField(blank=True, db_column='NEW_DATA', null=True)),
                ('ACTION_BY', models.ForeignKey(db_column='ACTION_BY', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('USER', models.ForeignKey(db_column='USER_ID', on_delete=django.db.models.deletion.CASCADE, related_name='history_records', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'USERS_HISTORY',
            },
        ),
        migrations.CreateModel(
            name='DESIGNATION_HISTORY',
            fields=[
                ('HISTORY_ID', models.AutoField(db_column='HISTORY_ID', primary_key=True, serialize=False)),
                ('ACTION', models.CharField(db_column='ACTION', max_length=10)),
                ('ACTION_AT', models.DateTimeField(auto_now_add=True, db_column='ACTION_AT')),
                ('OLD_DATA', models.JSONField(blank=True, db_column='OLD_DATA', null=True)),
                ('NEW_DATA', models.JSONField(blank=True, db_column='NEW_DATA', null=True)),
                ('ACTION_BY', models.ForeignKey(db_column='ACTION_BY', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('DESIGNATION', models.ForeignKey(db_column='DESIGNATION_ID', on_delete=django.db.models.deletion.CASCADE, to='accounts.designation')),
            ],
            options={
                'db_table': 'DESIGNATIONS_HISTORY',
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='DESIGNATION',
            field=models.ForeignKey(blank=True, db_column='DESIGNATION_ID', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='users', to='accounts.designation'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='UPDATED_BY',
            field=models.ForeignKey(blank=True, db_column='UPDATED_BY', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]
