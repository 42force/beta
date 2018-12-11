from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, PresentCondition, IllnessInfo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django.forms.widgets import CheckboxSelectMultiple
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import transaction


####this is where we add another form######

class ParentsSignUpCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'address', 'dateofbirth', 'mobilenumber', 'civilstatus', 'religion')

        fieldsets = (
            (None, {'fields': ('email', 'password')}),
            ('Personal info', {'email': ('first_name',)}),
        )

        @transaction.atomic
        def save(self):
            user = super().save(commit=False)
            user.is_parent = True
            if commit:
                user.save()
            return user

class ParentsSignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'last_name', 'address', 'dateofbirth', 'dateupdatedbio', 'mobilenumber', 'homenumber', 'civilstatus', 'religion')


class ParentsSignUpChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'email', 'address')



class EditProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'last_name', 'address', 'dateofbirth', 'dateupdatedbio', 'mobilenumber', 'homenumber', 'civilstatus', 'religion')



####this is where we add another form for parents##########




##########teachers sign up form###############

class TeacherSignUpCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'address', 'dateofbirth', 'mobilenumber', 'civilstatus', 'religion')

        fieldsets = (
            (None, {'fields': ('email', 'password')}),
            ('Personal info', {'email': ('first_name',)}),
        )


        def save(self, commit=True):
            user = super().save(commit=False)
            user.is_teacher = True
            if commit:
                user.save()
            return user


class TeacherSignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'last_name', 'address', 'dateofbirth', 'dateupdatedbio', 'mobilenumber', 'homenumber', 'civilstatus', 'religion')


class TeacherSignUpChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'email', 'address')



############teachers sign up forms############

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'profilepic','last_name', 'address', 'dateofbirth', 'dateupdatedbio', 'mobilenumber', 'homenumber', 'civilstatus', 'religion')

        fieldsets = (
            (None, {'fields': ('email', 'password')}),
            ('Personal info', {'email': ('password',)}),
        )


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password',)




class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'email', 'address')



class EditProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'dateofbirth', 'address', 'profilepic',  'dateuserjoined', 'mobilenumber', 'religion')


class PresentConditionForm(ModelForm):
    class Meta:
        model = PresentCondition
        fields = ('currentcondition', 'conditiondetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness' )


class IllnessInfoForm(ModelForm):
    class Meta:
        model = IllnessInfo
        fields = ('illnessinfo', 'illnessdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness')



###########################

###########################
