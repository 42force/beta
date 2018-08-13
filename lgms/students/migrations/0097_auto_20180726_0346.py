# Generated by Django 2.0.6 on 2018-07-26 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0096_auto_20180726_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='applicationtype',
            field=models.CharField(blank=True, choices=[('JUNIOR HIGH SCHOOL PROGRAM', 'Junior High School Program'), ('SPED', 'Special Education Program'), ('GRADE SCHOOL PROGRAM', 'Grade School Program'), ('SENIOR HIGH SCHOOL PROGRAM', 'Senior High School Program'), ('CASA PROGRAM', 'CASA Program')], default='CASA PROGRAM', help_text='Choose Application Program', max_length=64),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('SP', 'Single Parent'), ('M', 'Married'), ('D', 'Divorcee'), ('W', 'Widowed')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('I', 'INC'), ('B', 'Buddhist'), ('M', 'Muslim'), ('C', 'Catholic')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('HT', 'Hypertension'), ('HMP', 'Hematologic Problem'), ('LP', 'Lung Problem'), ('GP', 'Gastrointestinal Problems'), ('O', 'Others'), ('SZ', 'Seizures'), ('EPL', 'Epilepsy'), ('A', 'Allergy'), ('EP', 'Ear Problems'), ('TP', 'Thyroid Problem'), ('HP', 'Heart Problem'), ('VP', 'Viral Infection'), ('ANE', 'Anemia'), ('DM', 'Diabetes Mellitus'), ('AST', 'Asthma'), ('MP', 'Metabolc Problem'), ('CV', 'Convulsion'), ('DP', 'Dermatology Problem')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('C', 'COLDS'), ('D', 'DIARRHEA'), ('H', 'HEADACHE'), ('0', 'OTHERS'), ('S', 'STOMACH ACHE'), ('L', 'LBM'), ('F', 'FEVER'), ('CO', 'COUGH'), ('V', 'VOMITING')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='grades',
            field=models.CharField(choices=[('76', 'B'), ('87-91', 'P'), ('92-96', 'A'), ('82-86', 'AP'), ('77-81', 'D'), ('97-100', 'E')], default='B', help_text='Choose appropriate marks', max_length=64, verbose_name='Grading System'),
        ),
        migrations.AlterField(
            model_name='students',
            name='groupinfo',
            field=models.CharField(blank=True, choices=[('TEA', 'TEACH AM'), ('CA', 'CASA AFTERNOON 1:30'), ('TEP-GR2', 'TEACH PM GRADE 2'), ('G4', 'GRADE 4'), ('G9', 'GRADE 9'), ('G6', 'GRADE 6'), ('G1', 'GRADE 1'), ('G10', 'GRADE 10'), ('TEP-GR2', 'TEACH PM GRADE 3'), ('TEP-GR1', 'TEACH PM GRADE 1'), ('CM', 'CASA AM'), ('G3', 'GRADE 3'), ('G8', 'GRADE 8'), ('G7', 'GRADE 7'), ('PG', 'PLAY GROUP'), ('TEP', 'TEACH PM'), ('G2', 'GRADE 2'), ('G5', 'GRADE 5')], default='CM', help_text='Choose Group for Students', max_length=10),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='rolegroup',
            field=models.CharField(blank=True, choices=[('F', 'FACULTY'), ('SH', 'SCHOOL HEAD'), ('S', 'STAFF')], default='F', help_text='Please choose Role / Duty', max_length=10),
        ),
    ]