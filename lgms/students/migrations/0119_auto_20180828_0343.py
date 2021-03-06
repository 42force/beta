# Generated by Django 2.0.6 on 2018-08-28 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0118_auto_20180828_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterratings',
            name='chargrades',
            field=models.CharField(choices=[('FAIR / PASSED', 'F'), ('EXCELLENT', 'E'), ('VERY GOOD', 'VG'), ('GOOD', 'G'), ('NEEDS IMPROVEMENT', 'NI'), ('UNSATISFACTORY / FAILED', 'U')], default='EXCELLENT', help_text='Choose the appropriate grade', max_length=64, verbose_name='Character Rates'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('SPED', 'Special Education Program'), ('GRADE SCHOOL PROGRAM', 'Grade School Program'), ('SENIOR HIGH SCHOOL PROGRAM', 'Senior High School Program'), ('CASA PROGRAM', 'CASA Program'), ('JUNIOR HIGH SCHOOL PROGRAM', 'Junior High School Program')], default='CASA PROGRAM', help_text='Choose Application Program', max_length=64),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('D', 'Divorcee'), ('SP', 'Single Parent'), ('W', 'Widowed'), ('M', 'Married')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('M', 'Muslim'), ('I', 'INC'), ('B', 'Buddhist'), ('C', 'Catholic')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('DM', 'Diabetes Mellitus'), ('EPL', 'Epilepsy'), ('DP', 'Dermatology Problem'), ('HMP', 'Hematologic Problem'), ('ANE', 'Anemia'), ('SZ', 'Seizures'), ('GP', 'Gastrointestinal Problems'), ('HP', 'Heart Problem'), ('TP', 'Thyroid Problem'), ('O', 'Others'), ('A', 'Allergy'), ('EP', 'Ear Problems'), ('VP', 'Viral Infection'), ('LP', 'Lung Problem'), ('CV', 'Convulsion'), ('MP', 'Metabolc Problem'), ('AST', 'Asthma'), ('HT', 'Hypertension')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('0', 'OTHERS'), ('S', 'STOMACH ACHE'), ('V', 'VOMITING'), ('F', 'FEVER'), ('CO', 'COUGH'), ('D', 'DIARRHEA'), ('H', 'HEADACHE'), ('L', 'LBM'), ('C', 'COLDS')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='modeofpayment',
            field=models.CharField(choices=[('PLAN D', 'PLAN D - 6 MONTH PAYMENT'), ('A', 'ANNUAL'), ('SA', 'SEMI-ANNUAL'), ('QRT', 'QUARTERLY')], default='A', help_text='Choose Terms of Payment', max_length=64, verbose_name='Mode of Payment'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='grades',
            field=models.CharField(choices=[('77-81', 'D'), ('92-96', 'A'), ('76', 'B'), ('87-91', 'P'), ('97-100', 'E'), ('82-86', 'AP')], default='B', help_text='Choose appropriate marks', max_length=64, verbose_name='Grading System'),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('GRADE 6', 'G6'), ('TEACH PM GRADE 1', 'TEP=GR1'), ('TEACH PM GRADE 3', 'TEP-GR3'), ('TEACH AM', 'TEA'), ('TEACH PM', 'TEP'), ('PLAY GROUP', 'PG'), ('GRADE 7', 'G7'), ('GRADE 10', 'G10'), ('CASA AFTERNOON 1:30', 'CA'), ('GRADE 2', 'G2'), ('GRADE 3', 'G3'), ('GRADE 8', 'G8'), ('GRADE 9', 'G9'), ('CASA AM', 'CM'), ('GRADE 4', 'G4'), ('GRADE 1', 'G1'), ('GRADE 5', 'G5'), ('TEACH PM GRADE 2', 'TEP-GR2')], default='CASA AM', help_text='Choose Group for Students', max_length=64),
        ),
    ]
