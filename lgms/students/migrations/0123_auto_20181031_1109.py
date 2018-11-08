# Generated by Django 2.0.6 on 2018-10-31 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0122_auto_20181010_1230'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='testrating',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='testrating',
            name='content_type',
        ),
        migrations.AlterField(
            model_name='characterratings',
            name='chargrades',
            field=models.CharField(choices=[('UNSATISFACTORY / FAILED', 'U'), ('VERY GOOD', 'VG'), ('FAIR / PASSED', 'F'), ('NEEDS IMPROVEMENT', 'NI'), ('GOOD', 'G'), ('EXCELLENT', 'E')], default='EXCELLENT', help_text='Choose the appropriate grade', max_length=64, verbose_name='Character Rates'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('JUNIOR HIGH SCHOOL PROGRAM', 'Junior High School Program'), ('SENIOR HIGH SCHOOL PROGRAM', 'Senior High School Program'), ('CASA PROGRAM', 'CASA Program'), ('GRADE SCHOOL PROGRAM', 'Grade School Program'), ('SPED', 'Special Education Program')], default='CASA PROGRAM', help_text='Choose Application Program', max_length=64),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('SP', 'Single Parent'), ('W', 'Widowed'), ('M', 'Married'), ('D', 'Divorcee')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('M', 'Muslim'), ('C', 'Catholic'), ('B', 'Buddhist'), ('I', 'INC')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('AST', 'Asthma'), ('EPL', 'Epilepsy'), ('TP', 'Thyroid Problem'), ('GP', 'Gastrointestinal Problems'), ('MP', 'Metabolc Problem'), ('O', 'Others'), ('CV', 'Convulsion'), ('HT', 'Hypertension'), ('HP', 'Heart Problem'), ('LP', 'Lung Problem'), ('ANE', 'Anemia'), ('HMP', 'Hematologic Problem'), ('SZ', 'Seizures'), ('A', 'Allergy'), ('VP', 'Viral Infection'), ('DM', 'Diabetes Mellitus'), ('DP', 'Dermatology Problem'), ('EP', 'Ear Problems')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('F', 'FEVER'), ('V', 'VOMITING'), ('H', 'HEADACHE'), ('C', 'COLDS'), ('0', 'OTHERS'), ('CO', 'COUGH'), ('D', 'DIARRHEA'), ('S', 'STOMACH ACHE'), ('L', 'LBM')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='modeofpayment',
            field=models.CharField(choices=[('A', 'ANNUAL'), ('SA', 'SEMI-ANNUAL'), ('PLAN D', 'PLAN D - 6 MONTH PAYMENT'), ('QRT', 'QUARTERLY')], default='A', help_text='Choose Terms of Payment', max_length=64, verbose_name='Mode of Payment'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='grades',
            field=models.CharField(choices=[('92-96', 'A'), ('97-100', 'E'), ('77-81', 'D'), ('76', 'B'), ('82-86', 'AP'), ('87-91', 'P')], default='B', help_text='Choose appropriate marks', max_length=64, verbose_name='Grading System'),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('GRADE 1', 'G1'), ('GRADE 3', 'G3'), ('GRADE 6', 'G6'), ('CASA AFTERNOON 1:30', 'CA'), ('GRADE 8', 'G8'), ('TEACH AM', 'TEA'), ('GRADE 5', 'G5'), ('GRADE 9', 'G9'), ('TEACH PM GRADE 3', 'TEP-GR3'), ('TEACH PM', 'TEP'), ('TEACH PM GRADE 1', 'TEP=GR1'), ('GRADE 7', 'G7'), ('GRADE 2', 'G2'), ('TEACH PM GRADE 2', 'TEP-GR2'), ('GRADE 10', 'G10'), ('PLAY GROUP', 'PG'), ('GRADE 4', 'G4'), ('CASA AM', 'CM')], default='CASA AM', help_text='Choose Group for Students', max_length=64),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='rolegroup',
            field=models.CharField(blank=True, choices=[('F', 'FACULTY'), ('S', 'STAFF'), ('SH', 'SCHOOL HEAD')], default='F', help_text='Please choose Role / Duty', max_length=10),
        ),
        migrations.DeleteModel(
            name='TestRating',
        ),
    ]
