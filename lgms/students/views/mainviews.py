from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView
from django.views import generic
from django.template import loader
from django.db import transaction
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
#for session
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.decorators import login_required

from django.contrib.auth import login
from django.contrib.auth.models import User
from ..models import Students, CustomUser, IllnessInfo, PresentCondition, HospitalInfo, ImmunisationInfo, AccidentInfo, Document
from ..forms import CustomUserCreationForm, EditProfileForm, CustomUserChangeForm, PresentConditionForm, CustomUserForm, ParentsSignUpForm, TeacherSignUpForm

from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'



def home(request):
    if request.user.is_authenticated:
        if request.user.is_parent:
            return render(request, 'classroom/home.html')
        else:
            #this goes to parents view
            return render(request, 'classroom/home.html')
    #return render(request, 'classroom/home.html')

#############################################

#november 30 2018 modified this to separate the page
# def home(request):
#     if request.user.is_authenticated:
#         if request.user.is_teacher:
#             return redirect('students/parents/students_add_list.html')
#         else:
#             return redirect('students/teachers/teacherspage.html')
#     return render(request, 'students/home.html')

# def home(request):
#     return render(request, "students/home.html")
##############flat pages url views code###############################
##############flat pages url views code###############################

def slist(request):

    context = {
        "studentbios": StudentBio.objects.all()
    }
    return render(request, "students/home.html", context)


def ucheck(request):

    context = {
        "userbio": Users.objects.all()
    }
    return render(request, "students/home.html", context)

    #original
    #return render(request, "students/studentbio.html", context)
#studentbio id is the variable
#
# def medicalcheck():
#
#     try:
#         studentmed = medical


def studentbioid(request, pk):
    try:
        studentcheck = Students.objects.get(pk=pk)
        subjectlist = Students.objects.filter(subjects__pk=pk)
        studentowner = Students.objects.filter(owner__pk=pk)

    except Students.DoesNotExist:
        raise Http404("Student does not exist")
    context = {
        "studentcheck" : studentcheck,
        "subjectlist" : subjectlist,
        "studentowner" : studentowner
         #need to remember to make it visible in urls.py
    }
    #return render(request, "students/.html", context)
    #original code
    return render(request, "classroom/home.html", context)


def studentmedpccheck(request, pk):
    try:
        studentmedpc = PresentCondition.objects.filter(owner__pk=pk)

    except PresentCondition.DoesNotExist:
        raise Http404("No Medical Reports")
        
    context = {
        "studentmedpc" : studentmedpc
    }
    return render(request, "classroom/home.html", context)

# class SignUp(generic.CreateView):
#     form_class = CustomUserCreationForm
#     #this is previously login.html but just a test
#     #will check if we can customise the login.html
#     #success_url = reverse_lazy('login') # nov.30, 2018 i removed the reverse_lazy for the meantime
#     ##originally signup.html changed to home.html
#     template_name = 'signup.html'





#this signup_form and login_form not working
# def signup_form(request):
#     registrationform = CustomUserCreationForm
#     return render(request, 'students/home.html', {'registrationform': registrationform})
#     success_url = reverse_lazy('students/home')


# def login_form(request):
#     loginform = CustomUserForm()
#     return render(request, 'students/home.html', {'loginform': loginform})
#     success_url = reverse_lazy('students/home')

#@login_required
# class StudentBioList(ListView):
#     model = Students
#     paginate_by = 10


############################## MEDICAL FORM ####################################


class PresentConditionCreate(CreateView):
    model = PresentCondition
    fields = ['owner', 'studentname', 'currentcondition', 'conditiondetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']


class PresentConditionUpdate(UpdateView):
    model = PresentCondition
    fields = ['owner', 'studentname', 'currentcondition', 'conditiondetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']


class PresentConditionDelete(DeleteView):
    model = PresentCondition
    fields = ['owner', 'studentname', 'currentcondition', 'conditiondetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']
    success_url = "/studentmedpccheck/{<int:pk>}/"


##############################ILLNESS FORM ####################################
class IllnessInfoCreate(CreateView):
    model = IllnessInfo
    fields = ['user', 'name', 'illnessinfo', 'illnessdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']

class IllnessInfoUpdate(UpdateView):
    model = IllnessInfo
    fields = ['user', 'name', 'illnessinfo', 'illnessdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']

class IllnessInfoDelete(DeleteView):
    model = IllnessInfo
    fields = ['user', 'name', 'illnessinfo', 'illnessdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']
    success_url = reverse_lazy('students/home')

##############################ILLNESS FORM ####################################


##############################HOSPITAL FORM ####################################

class HospitalInfoCreate(CreateView):
    model = HospitalInfo
    fields = ['user', 'name', 'reasonforhospital', 'hospitalisationdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']

class HospitalInfoUpdate(UpdateView):
    model = HospitalInfo
    fields = ['user', 'name', 'reasonforhospital', 'hospitalisationdetails', 'treatmentdetails',  'startperiodofillness', 'endperiodillness']

class HospitalInfoDelete(DeleteView):
    model = HospitalInfo
    fields = ['user', 'name', 'reasonforhospital', 'hospitalisationdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']
    success_url = reverse_lazy('students/home')

##############################HOSPITAL FORM ####################################

##############################ACCIDENT FORM ####################################

class AccidentInfoCreate(CreateView):
    model = AccidentInfo
    fields = ['user', 'name', 'accidentdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']

class AccidentInfoUpdate(UpdateView):
    model = AccidentInfo
    fields = ['user', 'name', 'accidentdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']

class AccidentInfoDelete(DeleteView):
    model = HospitalInfo
    fields = ['user', 'name', 'accidentdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']
    success_url = reverse_lazy ('students/home')

##############################ACCIDENT FORM ####################################


##############################IMMUNE FORM ####################################
class ImmunisationInfoCreate(CreateView):
    model = ImmunisationInfo
    fields = ['user','name', 'immunedetails', 'treatmentdetails', 'startperiodofimmune', 'endperiodimmune']

class ImmunisationInfoUpdate(UpdateView):
    model = ImmunisationInfo
    fields = ['user', 'name', 'immunedetails', 'treatmentdetails', 'startperiodofimmune', 'endperiodimmune']

class ImmunisationInfoDelete(DeleteView):
    model = ImmunisationInfo
    fields = ['user', 'name', 'immunedetails', 'treatmentdetails', 'startperiodofimmune', 'endperiodimmune']
    success_url = reverse_lazy ('students/home')



##############################IMMUNE FORM ####################################
class DetailView(generic.DetailView):
    model = Students
    template_name = 'students/studentbiodetail.html'

class ResultsView(generic.DetailView):
    model = Students
    temaplate_name = 'students/studentbioresults.html'


def editprofile(request):
    try:
        profile = request.user.id
    except User.DoesNotExist:
        profile = CustomUser(user=request.user)
    if request.method == 'POST':
        profileform = EditProfileForm(request.POST, instance=request.user)
        if profileform.is_valid():
            profileform.save()
            update_session_auth_hash(request, form.users)
            return redirect('')
        else:
            message.error(request, ('ERROR ON UPDATING PROFILE!'))
    else:
        profileform = EditProfileForm(instance=request.user)
        return render (request, 'students/editprofile.html', {'profileform': profileform})


##############################PRESENT CONDITION FORM####################################
def presentcondition(request):
    try:
        profile = request.user.id
    except User.DoesNotExist:
        profile = CustomUser(user=request.user)
    if request.method == 'POST':
        medicalform = PresentConditionForm(request.POST, user=request.user)
        if medicalform.is_valid():
            medicalform.save()
            update_session_auth_hash(request, form.users)
            return redirect('')
        else:
            message.error(request, ('FORM INCOMPLETE'))
    else:
        medicalform = PresentConditionForm(instance=request.user)
        return render (request, 'students/medicalform.html', {'medicalform' : medicalform })




##############################CHANGE PASSWORD####################################
def changepassword(request):
    try:
        passwordprofile = request.user.id
    except User.DoesNotExist:
        passwordprofile = CustomUser(user=request.user)
    if request.method == 'POST':
        passwordchangeform = PasswordChangeForm(data=request.POST, user=request.user)

        if passwordchangeform.is_valid():
           passwordchangeform.save()
           update_session_auth_hash(request, passwordchangeform.user)
           return redirect('')

        else:
           messages.error(request, ('ERROR IN CHANGING YOUR PASSWORD!'))
    else:
        passwordchangeform = PasswordChangeForm(user=request.user)
        return render(request, 'students/changepassword.html', {'passwordchangeform' : passwordchangeform})





def latestsubjects(request):

    latest_subjects = Subjects.objects.order_by('id')
    context = { 'latest_subjects': latest_subjects }
    return render(request, 'students/latestsubjects.html', context)


##########for lgms email##############

def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['receiver@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('home.html')



#############for lgms email###############


#! remember ! this is the code I based for the editprofile to work - will get back into this.
# try:
#         profile = request.user.profile
#     except Profile.DoesNotExist:
#         profile = Profile(user=request.user)
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(
#             request.POST or None, instance=profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(
#                 request, ('your profile was successfully updated!'))
#             return redirect('products:profile')
#         else:
#             messages.error(
#                 request, ('There was an error updating your profile'))
#     else:s
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'dashboard/company/profile.html', {'user_form': user_form, 'profile_form': profile_form})






    # def flight(request, flight_id):
    #     try:
    #         flight = Flight.objects.get(pk=flight_id)
    #     except Flight.DoesNotExist:
    #         raise Http404("Flight does not exist")
    #     context = {
    #         "flight": flight,
    #         "passengers": flight.passengers.all(),
    #         "non_passengers": Passenger.objects.exclude(flights=flight).all()
    #     }
    #     return render(request, "flights/flight.html", context)

#
# class StudentBioView(TemplateView):
#     model = StudentBio
#     template_name = '.html'
#
# #getting records
#     def get(self, request):
#         studentrecords = StudentBio.objects.all()
#         print(studentrecords)
#         args = {'studentrecords' : studentrecords}
#         return render(request, self.template_name, args)


# class MedicalRecordsView(TemplateView):
#     template_name = '.html'
#
#     def get_info(self, request):
#         if request.method == 'POST':
#             form = MedicalForm(request.POST)
#             if form.is_valid():
#                 text = form.cleaned_data['post_info']
#                 return HttpResponseRedirect('.html')
#         else:
#             form = MedicalForm()
#         args = {'form': form, 'text' : text}
#         return render(request, self.template_name, args)


#
# def login_view():
#     if request.method == 'POST':
#                 #what is this form?? but noramlly you put UserCreationForm or whatever form you did.
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#         return redirect('')
#     else:
#         form = AuthenticationForm()
#

#medical form -- test
# from students.forms import PresentConditionForm

# Create your views here.

##testing of students

# class View(g)
#
# view profile with primary key



#
# class SubjectDetailView(generic.DetailView):
#     model = StudentBio
#     template_name = '.html'


# ###this is a test for studentview lists...
# def studentprofile(request):
#     args = {'studentbio': request.studentbio.id }
#     return render(request, 'studentprofileview.html', args)

#edit profile not working
#this worked code - will check!
#from user(blue parameters - i changed it to CustomUser and it worked)
#i also experimented to change the form name to profile form then change the name in html template
