from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, PresentCondition, IllnessInfo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django.forms.widgets import CheckboxSelectMultiple
from django.contrib.auth.models import User
from django.forms import ModelForm

####this is where we add another form######

class ParentsSignUpCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'password')

        fieldsets = (
            (None, {'fields': ('email', 'password')}),
            ('Personal info', {'email': ('studentname',)}),
        )


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
        fields = ('email', 'password', 'first_name', 'last_name', 'address', 'dateofbirth', 'dateupdatedbio', 'mobilenumber', 'homenumber', 'civilstatus', 'religion')

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
        fields = ('email', 'first_name', 'last_name', 'dateofbirth', 'address', 'dateuserjoined', 'mobilenumber', 'religion')


class PresentConditionForm(ModelForm):
    class Meta:
        model = PresentCondition
        fields = ('user', 'name', 'currentcondition', 'conditiondetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness' )


class IllnessInfoForm(ModelForm):
    class Meta:
        model = IllnessInfo
        fields = ('user', 'name', 'illnessinfo', 'illnessdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness')



###########################

###########################
