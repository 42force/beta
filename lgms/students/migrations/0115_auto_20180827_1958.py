# Generated by Django 2.0.6 on 2018-08-27 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0114_auto_20180827_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterratings',
            name='chargrades',
            field=models.CharField(choices=[('GOOD', 'G'), ('VERY GOOD', 'VG'), ('FAIR / PASSED', 'F'), ('EXCELLENT', 'E'), ('NEEDS IMPROVEMENT', 'NI'), ('UNSATISFACTORY / FAILED', 'U')], default='EXCELLENT', help_text='Choose the appropriate grade', max_length=64, verbose_name='Character Rates'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('D', 'Divorcee'), ('SP', 'Single Parent'), ('M', 'Married'), ('W', 'Widowed')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('I', 'INC'), ('B', 'Buddhist'), ('M', 'Muslim'), ('C', 'Catholic')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('HP', 'Heart Problem'), ('HMP', 'Hematologic Problem'), ('A', 'Allergy'), ('DM', 'Diabetes Mellitus'), ('LP', 'Lung Problem'), ('MP', 'Metabolc Problem'), ('EPL', 'Epilepsy'), ('GP', 'Gastrointestinal Problems'), ('O', 'Others'), ('DP', 'Dermatology Problem'), ('EP', 'Ear Problems'), ('SZ', 'Seizures'), ('HT', 'Hypertension'), ('ANE', 'Anemia'), ('VP', 'Viral Infection'), ('AST', 'Asthma'), ('TP', 'Thyroid Problem'), ('CV', 'Convulsion')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('0', 'OTHERS'), ('V', 'VOMITING'), ('C', 'COLDS'), ('CO', 'COUGH'), ('F', 'FEVER'), ('S', 'STOMACH ACHE'), ('D', 'DIARRHEA'), ('L', 'LBM'), ('H', 'HEADACHE')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='modeofpayment',
            field=models.CharField(choices=[('SA', 'SEMI-ANNUAL'), ('QRT', 'QUARTERLY'), ('A', 'ANNUAL'), ('PLAN D', 'PLAN D - 6 MONTH PAYMENT')], default='A', help_text='Choose Terms of Payment', max_length=64, verbose_name='Mode of Payment'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='grades',
            field=models.CharField(choices=[('92-96', 'A'), ('87-91', 'P'), ('97-100', 'E'), ('76', 'B'), ('77-81', 'D'), ('82-86', 'AP')], default='B', help_text='Choose appropriate marks', max_length=64, verbose_name='Grading System'),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('GRADE 9', 'G9'), ('TEACH PM GRADE 2', 'TEP-GR2'), ('TEACH PM GRADE 3', 'TEP-GR3'), ('CASA AFTERNOON 1:30', 'CA'), ('TEACH PM GRADE 1', 'TEP=GR1'), ('TEACH AM', 'TEA'), ('GRADE 1', 'G1'), ('GRADE 5', 'G5'), ('GRADE 8', 'G8'), ('GRADE 3', 'G3'), ('CASA AM', 'CM'), ('GRADE 10', 'G10'), ('GRADE 2', 'G2'), ('GRADE 4', 'G4'), ('PLAY GROUP', 'PG'), ('GRADE 7', 'G7'), ('GRADE 6', 'G6'), ('TEACH PM', 'TEP')], default='CASA AM', help_text='Choose Group for Students', max_length=64),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='rolegroup',
            field=models.CharField(blank=True, choices=[('SH', 'SCHOOL HEAD'), ('S', 'STAFF'), ('F', 'FACULTY')], default='F', help_text='Please choose Role / Duty', max_length=10),
        ),
    ]
