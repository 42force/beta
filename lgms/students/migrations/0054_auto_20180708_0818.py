# Generated by Django 2.0.6 on 2018-07-08 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0053_auto_20180708_0808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('SPED', 'Special Education Program'), ('GS', 'Grade School Program'), ('SH', 'Senior High School Program'), ('JH', 'Junior High School Program'), ('CA', 'CASA Program')], default='CA', help_text='Choose Application Program', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('SP', 'Single Parent'), ('M', 'Married'), ('D', 'Divorcee'), ('W', 'Widowed')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('C', 'Catholic'), ('M', 'Muslim'), ('I', 'INC'), ('B', 'Buddhist')], default='C', help_text='Please select your Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('TEP', 'TEACH PM'), ('G1', 'GRADE 1'), ('G9', 'GRADE 9'), ('PG', 'PLAY GROUP'), ('TEA', 'TEACH AM'), ('G2', 'GRADE 2'), ('G4', 'GRADE 4'), ('G8', 'GRADE 8'), ('TEP-GR2', 'TEACH PM GRADE 2'), ('CM', 'CASA AM'), ('G5', 'GRADE 5'), ('TEP-GR2', 'TEACH PM GRADE 3'), ('CA', 'CASA AFTERNOON 1:30'), ('G7', 'GRADE 7'), ('G3', 'GRADE 3'), ('TEP-GR1', 'TEACH PM GRADE 1'), ('G10', 'GRADE 10'), ('G6', 'GRADE 6')], default='CM', help_text='Choose Group for Students', max_length=10),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='rolegroup',
            field=models.CharField(blank=True, choices=[('SH', 'SCHOOL HEAD'), ('F', 'FACULTY'), ('S', 'STAFF')], default='F', help_text='Please choose Role / Duty', max_length=10),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
