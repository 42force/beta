# Generated by Django 2.0.6 on 2018-07-30 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0101_auto_20180729_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterratings',
            name='chargrades',
            field=models.CharField(choices=[('VERY GOOD', 'VG'), ('UNSATISFACTORY / FAILED', 'U'), ('FAIR / PASSED', 'F'), ('EXCELLENT', 'E'), ('NEEDS IMPROVEMENT', 'NI'), ('GOOD', 'G')], default='EXCELLENT', help_text='Choose the appropriate grade', max_length=10, verbose_name='Character Rates'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('GRADE SCHOOL PROGRAM', 'Grade School Program'), ('SENIOR HIGH SCHOOL PROGRAM', 'Senior High School Program'), ('CASA PROGRAM', 'CASA Program'), ('SPED', 'Special Education Program'), ('JUNIOR HIGH SCHOOL PROGRAM', 'Junior High School Program')], default='CASA PROGRAM', help_text='Choose Application Program', max_length=64),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('W', 'Widowed'), ('M', 'Married'), ('SP', 'Single Parent'), ('D', 'Divorcee')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('B', 'Buddhist'), ('M', 'Muslim'), ('C', 'Catholic'), ('I', 'INC')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('EPL', 'Epilepsy'), ('ANE', 'Anemia'), ('DP', 'Dermatology Problem'), ('EP', 'Ear Problems'), ('GP', 'Gastrointestinal Problems'), ('MP', 'Metabolc Problem'), ('DM', 'Diabetes Mellitus'), ('VP', 'Viral Infection'), ('O', 'Others'), ('AST', 'Asthma'), ('HT', 'Hypertension'), ('CV', 'Convulsion'), ('A', 'Allergy'), ('HMP', 'Hematologic Problem'), ('SZ', 'Seizures'), ('LP', 'Lung Problem'), ('HP', 'Heart Problem'), ('TP', 'Thyroid Problem')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('C', 'COLDS'), ('0', 'OTHERS'), ('H', 'HEADACHE'), ('F', 'FEVER'), ('V', 'VOMITING'), ('L', 'LBM'), ('S', 'STOMACH ACHE'), ('CO', 'COUGH'), ('D', 'DIARRHEA')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='modeofpayment',
            field=models.CharField(choices=[('SA', 'SEMI-ANNUAL'), ('QRT', 'QUARTERLY'), ('A', 'ANNUAL')], default='A', help_text='Choose Terms of Payment', max_length=64, verbose_name='Mode of Payment'),
        ),
        migrations.AlterField(
            model_name='studentbio',
            name='subjects',
            field=models.ManyToManyField(related_name='subjectslist', to='students.Subjects', verbose_name='List of Subjects'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='grades',
            field=models.CharField(choices=[('97-100', 'E'), ('87-91', 'P'), ('76', 'B'), ('82-86', 'AP'), ('77-81', 'D'), ('92-96', 'A')], default='B', help_text='Choose appropriate marks', max_length=64, verbose_name='Grading System'),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('TEACH PM GRADE 1', 'TEP=GR1'), ('TEACH PM GRADE 2', 'TEP-GR2'), ('TEACH PM', 'TEP'), ('CASA AFTERNOON 1:30', 'CA'), ('GRADE 7', 'G7'), ('GRADE 9', 'G9'), ('TEACH AM', 'TEA'), ('GRADE 3', 'G3'), ('GRADE 8', 'G8'), ('CASA AM', 'CM'), ('GRADE 1', 'G1'), ('PLAY GROUP', 'PG'), ('GRADE 10', 'G10'), ('GRADE 6', 'G6'), ('TEACH PM GRADE 3', 'TEP-GR3'), ('GRADE 2', 'G2'), ('GRADE 4', 'G4'), ('GRADE 5', 'G5')], default='CASA AM', help_text='Choose Group for Students', max_length=10),
        ),
    ]
