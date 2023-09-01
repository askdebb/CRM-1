# Generated by Django 4.2.4 on 2023-08-31 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gbc_crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='contact_no',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Contact Number'),
        ),
        migrations.AddField(
            model_name='employee',
            name='email_address',
            field=models.EmailField(blank=True, max_length=60, null=True, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_department', to='gbc_crm.department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='supervisor',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_supervisor', to='gbc_crm.supervisor'),
        ),
    ]