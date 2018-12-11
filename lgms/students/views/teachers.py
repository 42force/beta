from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, DetailView, ListView

#this is method decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib import messages

from django.db import transaction
from django.db.models import Avg, Count

from django.forms import inlineformset_factory

from django.shortcuts import get_object_or_404, redirect, render

from django.urls import reverse, reverse_lazy

from .. decorators import teacher_required
#THIS IS THE DATABASE INFORMATION
from .. models import CustomUser, Students, Subjects
from .. forms import TeacherSignUpForm, TeacherSignUpCreationForm

##################teachers sign up view end###########################

class TeachersView(CreateView):
    model = CustomUser
    form_class = TeacherSignUpCreationForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Teachers'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('teachers:teachers_page')

##################teacher sign up view end##########################

# @method_decorator([login_required, teacher_required], name='dispatch')
# class TeachersStudentsView(ListView)

# @method_decorator([login_required, teacher_required], name='dispatch')
class TeachersInfoView(ListView):
    model  = Students
    ordering = ('studentname')
    context_object_name = 'studentsprofile'
    template_name = 'classroom/teacherspage.html'

@method_decorator([login_required, teacher_required], name='dispatch')
class SubjectsTaughtView(ListView):
    model = Subjects
    ordering = ('subjectname')
    context_object_name = 'subjectname'
    template_name = 'classroom/teachers/subjecthandled.html'
