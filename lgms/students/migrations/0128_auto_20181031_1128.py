# Generated by Django 2.0.6 on 2018-10-31 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0127_auto_20181031_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterratings',
            name='chargrades',
            field=models.CharField(choices=[('FAIR / PASSED', 'F'), ('NEEDS IMPROVEMENT', 'NI'), ('GOOD', 'G'), ('EXCELLENT', 'E'), ('VERY GOOD', 'VG'), ('UNSATISFACTORY / FAILED', 'U')], default='EXCELLENT', help_text='Choose the appropriate grade', max_length=64, verbose_name='Character Rates'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('GRADE SCHOOL PROGRAM', 'Grade School Program'), ('SENIOR HIGH SCHOOL PROGRAM', 'Senior High School Program'), ('CASA PROGRAM', 'CASA Program'), ('SPED', 'Special Education Program'), ('JUNIOR HIGH SCHOOL PROGRAM', 'Junior High School Program')], default='CASA PROGRAM', help_text='Choose Application Program', max_length=64),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('M', 'Married'), ('D', 'Divorcee'), ('SP', 'Single Parent'), ('W', 'Widowed')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('C', 'Catholic'), ('B', 'Buddhist'), ('M', 'Muslim'), ('I', 'INC')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('A', 'Allergy'), ('AST', 'Asthma'), ('DM', 'Diabetes Mellitus'), ('GP', 'Gastrointestinal Problems'), ('HT', 'Hypertension'), ('MP', 'Metabolc Problem'), ('SZ', 'Seizures'), ('EP', 'Ear Problems'), ('HP', 'Heart Problem'), ('CV', 'Convulsion'), ('DP', 'Dermatology Problem'), ('EPL', 'Epilepsy'), ('TP', 'Thyroid Problem'), ('ANE', 'Anemia'), ('LP', 'Lung Problem'), ('VP', 'Viral Infection'), ('O', 'Others'), ('HMP', 'Hematologic Problem')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('H', 'HEADACHE'), ('S', 'STOMACH ACHE'), ('CO', 'COUGH'), ('L', 'LBM'), ('F', 'FEVER'), ('C', 'COLDS'), ('0', 'OTHERS'), ('D', 'DIARRHEA'), ('V', 'VOMITING')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='modeofpayment',
            field=models.CharField(choices=[('PLAN D', 'PLAN D - 6 MONTH PAYMENT'), ('SA', 'SEMI-ANNUAL'), ('A', 'ANNUAL'), ('QRT', 'QUARTERLY')], default='A', help_text='Choose Terms of Payment', max_length=64, verbose_name='Mode of Payment'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='grades',
            field=models.CharField(choices=[('76', 'B'), ('82-86', 'AP'), ('77-81', 'D'), ('87-91', 'P'), ('97-100', 'E'), ('92-96', 'A')], default='B', help_text='Choose appropriate marks', max_length=64, verbose_name='Grading System'),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('GRADE 4', 'G4'), ('TEACH PM GRADE 1', 'TEP=GR1'), ('TEACH PM GRADE 2', 'TEP-GR2'), ('GRADE 1', 'G1'), ('GRADE 9', 'G9'), ('CASA AM', 'CM'), ('PLAY GROUP', 'PG'), ('TEACH PM', 'TEP'), ('GRADE 3', 'G3'), ('GRADE 5', 'G5'), ('CASA AFTERNOON 1:30', 'CA'), ('TEACH AM', 'TEA'), ('GRADE 6', 'G6'), ('GRADE 8', 'G8'), ('TEACH PM GRADE 3', 'TEP-GR3'), ('GRADE 2', 'G2'), ('GRADE 7', 'G7'), ('GRADE 10', 'G10')], default='CASA AM', help_text='Choose Group for Students', max_length=64),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='rolegroup',
            field=models.CharField(blank=True, choices=[('F', 'FACULTY'), ('SH', 'SCHOOL HEAD'), ('S', 'STAFF')], default='F', help_text='Please choose Role / Duty', max_length=10),
        ),
    ]
