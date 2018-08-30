# Generated by Django 2.0.6 on 2018-08-28 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0119_auto_20180828_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterratings',
            name='chargrades',
            field=models.CharField(choices=[('FAIR / PASSED', 'F'), ('UNSATISFACTORY / FAILED', 'U'), ('VERY GOOD', 'VG'), ('GOOD', 'G'), ('NEEDS IMPROVEMENT', 'NI'), ('EXCELLENT', 'E')], default='EXCELLENT', help_text='Choose the appropriate grade', max_length=64, verbose_name='Character Rates'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('JUNIOR HIGH SCHOOL PROGRAM', 'Junior High School Program'), ('GRADE SCHOOL PROGRAM', 'Grade School Program'), ('SPED', 'Special Education Program'), ('SENIOR HIGH SCHOOL PROGRAM', 'Senior High School Program'), ('CASA PROGRAM', 'CASA Program')], default='CASA PROGRAM', help_text='Choose Application Program', max_length=64),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('W', 'Widowed'), ('M', 'Married'), ('D', 'Divorcee'), ('SP', 'Single Parent')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('C', 'Catholic'), ('I', 'INC'), ('B', 'Buddhist'), ('M', 'Muslim')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('A', 'Allergy'), ('HP', 'Heart Problem'), ('DM', 'Diabetes Mellitus'), ('EP', 'Ear Problems'), ('SZ', 'Seizures'), ('HT', 'Hypertension'), ('O', 'Others'), ('DP', 'Dermatology Problem'), ('LP', 'Lung Problem'), ('MP', 'Metabolc Problem'), ('CV', 'Convulsion'), ('EPL', 'Epilepsy'), ('ANE', 'Anemia'), ('HMP', 'Hematologic Problem'), ('TP', 'Thyroid Problem'), ('AST', 'Asthma'), ('VP', 'Viral Infection'), ('GP', 'Gastrointestinal Problems')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('D', 'DIARRHEA'), ('0', 'OTHERS'), ('V', 'VOMITING'), ('H', 'HEADACHE'), ('L', 'LBM'), ('CO', 'COUGH'), ('F', 'FEVER'), ('S', 'STOMACH ACHE'), ('C', 'COLDS')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='gtotal',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='modeofpayment',
            field=models.CharField(choices=[('A', 'ANNUAL'), ('QRT', 'QUARTERLY'), ('PLAN D', 'PLAN D - 6 MONTH PAYMENT'), ('SA', 'SEMI-ANNUAL')], default='A', help_text='Choose Terms of Payment', max_length=64, verbose_name='Mode of Payment'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='grades',
            field=models.CharField(choices=[('82-86', 'AP'), ('77-81', 'D'), ('76', 'B'), ('87-91', 'P'), ('97-100', 'E'), ('92-96', 'A')], default='B', help_text='Choose appropriate marks', max_length=64, verbose_name='Grading System'),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('CASA AM', 'CM'), ('TEACH AM', 'TEA'), ('TEACH PM', 'TEP'), ('GRADE 5', 'G5'), ('GRADE 6', 'G6'), ('GRADE 8', 'G8'), ('GRADE 4', 'G4'), ('TEACH PM GRADE 2', 'TEP-GR2'), ('GRADE 1', 'G1'), ('GRADE 3', 'G3'), ('PLAY GROUP', 'PG'), ('GRADE 9', 'G9'), ('GRADE 7', 'G7'), ('GRADE 10', 'G10'), ('GRADE 2', 'G2'), ('CASA AFTERNOON 1:30', 'CA'), ('TEACH PM GRADE 3', 'TEP-GR3'), ('TEACH PM GRADE 1', 'TEP=GR1')], default='CASA AM', help_text='Choose Group for Students', max_length=64),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='rolegroup',
            field=models.CharField(blank=True, choices=[('F', 'FACULTY'), ('SH', 'SCHOOL HEAD'), ('S', 'STAFF')], default='F', help_text='Please choose Role / Duty', max_length=10),
        ),
    ]