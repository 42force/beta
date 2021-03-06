# Generated by Django 2.0.6 on 2018-07-31 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0106_auto_20180731_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentbio',
            name='financialinfo',
            field=models.ForeignKey(blank=True, max_length=64, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.StatementAccount'),
        ),
        migrations.AlterField(
            model_name='characterratings',
            name='chargrades',
            field=models.CharField(choices=[('NEEDS IMPROVEMENT', 'NI'), ('FAIR / PASSED', 'F'), ('VERY GOOD', 'VG'), ('UNSATISFACTORY / FAILED', 'U'), ('GOOD', 'G'), ('EXCELLENT', 'E')], default='EXCELLENT', help_text='Choose the appropriate grade', max_length=6, verbose_name='Character Rates'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('SENIOR HIGH SCHOOL PROGRAM', 'Senior High School Program'), ('JUNIOR HIGH SCHOOL PROGRAM', 'Junior High School Program'), ('CASA PROGRAM', 'CASA Program'), ('SPED', 'Special Education Program'), ('GRADE SCHOOL PROGRAM', 'Grade School Program')], default='CASA PROGRAM', help_text='Choose Application Program', max_length=64),
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
            field=models.CharField(choices=[('DP', 'Dermatology Problem'), ('MP', 'Metabolc Problem'), ('HMP', 'Hematologic Problem'), ('VP', 'Viral Infection'), ('GP', 'Gastrointestinal Problems'), ('TP', 'Thyroid Problem'), ('ANE', 'Anemia'), ('HT', 'Hypertension'), ('A', 'Allergy'), ('LP', 'Lung Problem'), ('SZ', 'Seizures'), ('DM', 'Diabetes Mellitus'), ('CV', 'Convulsion'), ('O', 'Others'), ('EPL', 'Epilepsy'), ('AST', 'Asthma'), ('EP', 'Ear Problems'), ('HP', 'Heart Problem')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('S', 'STOMACH ACHE'), ('C', 'COLDS'), ('0', 'OTHERS'), ('D', 'DIARRHEA'), ('L', 'LBM'), ('F', 'FEVER'), ('V', 'VOMITING'), ('CO', 'COUGH'), ('H', 'HEADACHE')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='modeofpayment',
            field=models.CharField(choices=[('QRT', 'QUARTERLY'), ('A', 'ANNUAL'), ('SA', 'SEMI-ANNUAL')], default='A', help_text='Choose Terms of Payment', max_length=64, verbose_name='Mode of Payment'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='grades',
            field=models.CharField(choices=[('76', 'B'), ('92-96', 'A'), ('82-86', 'AP'), ('87-91', 'P'), ('97-100', 'E'), ('77-81', 'D')], default='B', help_text='Choose appropriate marks', max_length=64, verbose_name='Grading System'),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('CASA AM', 'CM'), ('TEACH AM', 'TEA'), ('GRADE 9', 'G9'), ('CASA AFTERNOON 1:30', 'CA'), ('GRADE 6', 'G6'), ('GRADE 10', 'G10'), ('GRADE 2', 'G2'), ('TEACH PM GRADE 2', 'TEP-GR2'), ('TEACH PM GRADE 3', 'TEP-GR3'), ('PLAY GROUP', 'PG'), ('GRADE 8', 'G8'), ('GRADE 3', 'G3'), ('TEACH PM', 'TEP'), ('GRADE 5', 'G5'), ('GRADE 1', 'G1'), ('TEACH PM GRADE 1', 'TEP=GR1'), ('GRADE 4', 'G4'), ('GRADE 7', 'G7')], default='CASA AM', help_text='Choose Group for Students', max_length=10),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='rolegroup',
            field=models.CharField(blank=True, choices=[('S', 'STAFF'), ('F', 'FACULTY'), ('SH', 'SCHOOL HEAD')], default='F', help_text='Please choose Role / Duty', max_length=10),
        ),
    ]
