# Generated by Django 2.0.6 on 2018-07-02 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0032_auto_20180702_0211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parents',
            name='childsname',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('SH', 'Senior High School Program'), ('GS', 'Grade School Program'), ('JH', 'Junior High School Program'), ('SPED', 'Special Education Program'), ('CA', 'CASA Program')], default='CA', help_text='Choose Application Program', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('SP', 'Single Parent'), ('D', 'Divorcee'), ('M', 'Married'), ('W', 'Widowed')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('I', 'INC'), ('B', 'Buddhist'), ('C', 'Catholic'), ('M', 'Muslim')], default='C', help_text='Please select your Religion', max_length=30),
        ),
    ]