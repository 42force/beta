# Generated by Django 2.1.2 on 2018-11-30 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0138_auto_20181127_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradeGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gradename', models.CharField(blank=True, max_length=30, verbose_name='Grade Year')),
                ('gradedesc', models.CharField(blank=True, max_length=64, verbose_name='Grade Description')),
            ],
            options={
                'verbose_name_plural': 'Student Grade Year Options',
            },
        ),
        migrations.AlterModelOptions(
            name='students',
            options={'verbose_name_plural': 'Student Information'},
        ),
        migrations.AlterField(
            model_name='characterratings',
            name='chargrades',
            field=models.CharField(choices=[('VERY GOOD', 'VG'), ('UNSATISFACTORY / FAILED', 'U'), ('EXCELLENT', 'E'), ('FAIR / PASSED', 'F'), ('GOOD', 'G'), ('NEEDS IMPROVEMENT', 'NI')], default='EXCELLENT', help_text='Choose the appropriate grade', max_length=64, verbose_name='Character Rates'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('SP', 'Single Parent'), ('M', 'Married'), ('W', 'Widowed'), ('D', 'Divorcee')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('C', 'Catholic'), ('B', 'Buddhist'), ('I', 'INC'), ('M', 'Muslim')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='rolegroup',
            field=models.CharField(blank=True, choices=[('SH', 'SCHOOL HEAD'), ('F', 'FACULTY'), ('S', 'STAFF')], default='F', help_text='Please choose Role / Duty', max_length=10),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('AST', 'Asthma'), ('LP', 'Lung Problem'), ('A', 'Allergy'), ('VP', 'Viral Infection'), ('SZ', 'Seizures'), ('HMP', 'Hematologic Problem'), ('EPL', 'Epilepsy'), ('MP', 'Metabolc Problem'), ('DM', 'Diabetes Mellitus'), ('CV', 'Convulsion'), ('HT', 'Hypertension'), ('GP', 'Gastrointestinal Problems'), ('HP', 'Heart Problem'), ('O', 'Others'), ('EP', 'Ear Problems'), ('ANE', 'Anemia'), ('DP', 'Dermatology Problem'), ('TP', 'Thyroid Problem')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('H', 'HEADACHE'), ('L', 'LBM'), ('V', 'VOMITING'), ('F', 'FEVER'), ('CO', 'COUGH'), ('S', 'STOMACH ACHE'), ('C', 'COLDS'), ('D', 'DIARRHEA'), ('0', 'OTHERS')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='gradeyear',
            field=models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, related_name='statement_gradegroup', to='students.GradeGroup', verbose_name='Grade Year'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='modeofpayment',
            field=models.CharField(choices=[('QRT', 'QUARTERLY'), ('SA', 'SEMI-ANNUAL'), ('PLAN D', 'PLAN D - 6 MONTH PAYMENT'), ('A', 'ANNUAL')], default='A', help_text='Choose Terms of Payment', max_length=64, verbose_name='Mode of Payment'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='grades',
            field=models.CharField(choices=[('76', 'B'), ('82-86', 'AP'), ('97-100', 'E'), ('92-96', 'A'), ('77-81', 'D'), ('87-91', 'P')], default='B', help_text='Choose appropriate marks', max_length=64, verbose_name='Grading System'),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('GRADE4', 'G4'), ('TEACHPM GRADE3', 'TEP-GR3'), ('TEACHPM GRADE1', 'TEP=GR1'), ('GRADE1', 'G1'), ('GRADE5', 'G5'), ('CASA AFTERNOON 1:30', 'CA'), ('TEACHPM GRADE2', 'TEP-GR2'), ('GRADE8', 'G8'), ('GRADE10', 'G10'), ('TEACHPM', 'TEP'), ('PLAY GROUP', 'PG'), ('GRADE2', 'G2'), ('GRADE6', 'G6'), ('GRADE7', 'G7'), ('GRADE3', 'G3'), ('TEACHAM', 'TEA'), ('CASA AM', 'CM'), ('GRADE9', 'G9')], default='CASA AM', help_text='Choose Group for Students', max_length=64),
        ),
        migrations.DeleteModel(
            name='GradeYear',
        ),
    ]
