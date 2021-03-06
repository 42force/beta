# Generated by Django 2.1.2 on 2018-12-03 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0140_auto_20181130_1137'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='students',
            options={'verbose_name_plural': 'LGMS Students Information'},
        ),
        migrations.AlterModelOptions(
            name='subjects',
            options={'verbose_name_plural': 'LGMS Subject Lists'},
        ),
        migrations.RemoveField(
            model_name='students',
            name='subject',
        ),
        migrations.AddField(
            model_name='students',
            name='subjects',
            field=models.ManyToManyField(help_text='Choose list of subjects', to='students.Subjects'),
        ),
        migrations.AlterField(
            model_name='characterratings',
            name='chargrades',
            field=models.CharField(choices=[('NEEDS IMPROVEMENT', 'NI'), ('FAIR / PASSED', 'F'), ('GOOD', 'G'), ('VERY GOOD', 'VG'), ('UNSATISFACTORY / FAILED', 'U'), ('EXCELLENT', 'E')], default='EXCELLENT', help_text='Choose the appropriate grade', max_length=64, verbose_name='Character Rates'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='civilstatus',
            field=models.CharField(blank=True, choices=[('D', 'Divorcee'), ('M', 'Married'), ('SP', 'Single Parent'), ('W', 'Widowed')], default='M', help_text='Please select Civit Status', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='religion',
            field=models.CharField(blank=True, choices=[('B', 'Buddhist'), ('C', 'Catholic'), ('M', 'Muslim'), ('I', 'INC')], default='C', help_text='Please select Religion', max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=64, unique=True, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='rolegroup',
            field=models.CharField(blank=True, choices=[('SH', 'SCHOOL HEAD'), ('F', 'FACULTY'), ('S', 'STAFF')], default='F', help_text='Please choose Role / Duty', max_length=10),
        ),
        migrations.AlterField(
            model_name='illnessinfo',
            name='illnessinfo',
            field=models.CharField(choices=[('EPL', 'Epilepsy'), ('DP', 'Dermatology Problem'), ('LP', 'Lung Problem'), ('A', 'Allergy'), ('VP', 'Viral Infection'), ('HMP', 'Hematologic Problem'), ('CV', 'Convulsion'), ('TP', 'Thyroid Problem'), ('MP', 'Metabolc Problem'), ('GP', 'Gastrointestinal Problems'), ('O', 'Others'), ('DM', 'Diabetes Mellitus'), ('AST', 'Asthma'), ('SZ', 'Seizures'), ('EP', 'Ear Problems'), ('HP', 'Heart Problem'), ('ANE', 'Anemia'), ('HT', 'Hypertension')], default='A', max_length=64, verbose_name='Illness Information'),
        ),
        migrations.AlterField(
            model_name='presentcondition',
            name='currentcondition',
            field=models.CharField(choices=[('C', 'COLDS'), ('D', 'DIARRHEA'), ('L', 'LBM'), ('V', 'VOMITING'), ('F', 'FEVER'), ('H', 'HEADACHE'), ('0', 'OTHERS'), ('CO', 'COUGH'), ('S', 'STOMACH ACHE')], max_length=64, verbose_name='Current Medical Condition'),
        ),
        migrations.AlterField(
            model_name='statementaccount',
            name='modeofpayment',
            field=models.CharField(choices=[('QRT', 'QUARTERLY'), ('PLAN D', 'PLAN D - 6 MONTH PAYMENT'), ('A', 'ANNUAL'), ('SA', 'SEMI-ANNUAL')], default='A', help_text='Choose Terms of Payment', max_length=64, verbose_name='Mode of Payment'),
        ),
        migrations.AlterField(
            model_name='studentgrades',
            name='grades',
            field=models.CharField(choices=[('77-81', 'D'), ('76', 'B'), ('97-100', 'E'), ('87-91', 'P'), ('82-86', 'AP'), ('92-96', 'A')], default='B', help_text='Choose appropriate marks', max_length=64, verbose_name='Grading System'),
        ),
    ]
