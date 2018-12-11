from django.contrib import messages

from django.contrib.auth import login

from django.contrib.auth.decorators import login_required

from django.db import transaction

from django.db.models import Avg, Count
from django.forms import inlineformset_factory

from django.shortcuts import get_object_or_404, redirect

from django.urls import reverse_lazy, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView

from .. decorators import parents_required
from .. models import CustomUser, Students

from .. forms import ParentsSignUpForm, ParentsSignUpCreationForm

class ParentsView(CreateView):
    model = CustomUser
    form_class = ParentsSignUpCreationForm #changed the form
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Parents'
        return super().get_context_data(**kwargs)


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('parents:students_info') #this needs to be changed

######################
@method_decorator([login_required, parents_required], name='dispatch')
class StudentsInfoView(ListView):
    model  = Students
    ordering = ('studentname')
    context_object_name = 'studentlists'
    template_name = 'classroom/home.html'

    def get_queryset(self):
        queryset = self.request.user.studentlists\
        .select_related('owner')\
        .annotate(students_count=Count('studentname', distinct=True))
        return queryset


#this is for viewing the student reference to owner / user
class StudentsListView(ListView):
    model = Students
    ordering = ('studentname',)
    context_object_name = 'mykids'
    template_name = 'classroom/home.html'

    def student_detail_view(request, primary_key):
        student = get_object_or_404(Students, pk=primary_key)
        return render(request, 'classroom/home.html', context={'student' : student})


class StudentsDetailView(DetailView):
    model = Students

    def student_detail_view(request, primary_key):
        student = get_object_or_404(Students, pk=primary_key)
        return render(request, 'classroom/home.html', context={'student' : student})


# def get_queryset(self):
#         student = self.request.user.student
#         student_interests = student.interests.values_list('pk', flat=True)
#         taken_quizzes = student.quizzes.values_list('pk', flat=True)
#         queryset = Quiz.objects.filter(subject__in=student_interests) \
#             .exclude(pk__in=taken_quizzes) \
#             .annotate(questions_count=Count('questions')) \
#             .filter(questions_count__gt=0)
#         return queryset

# @method_decorator ([login_required, parents_required], name='dispatch')
class StudentsCreateView(CreateView):
    model = Students
    fields = ('studentname', 'birthday', 'profilepic', 'groupinfo' )
    template_name = 'classroom/parents/students_add_list.html'


    def form_valid(self, form):
        student = form.save(commit=False)
        student.owner = self.request.user
        student.save()
        messages.success(self.request, 'Your kids was created with success! Go ahead and view your profile.')
        return redirect('home')


##our guide##

# @method_decorator([login_required, teacher_required], name='dispatch')
# class QuizCreateView(CreateView):
#     model = Quiz
#     fields = ('name', 'subject', )
#     template_name = 'classroom/teachers/quiz_add_form.html'
#
#     def form_valid(self, form):
#         quiz = form.save(commit=False)
#         quiz.owner = self.request.user
#         quiz.save()
#         messages.success(self.request, 'The quiz was created with success! Go ahead and add some questions now.')
#         return redirect('teachers:quiz_change', quiz.pk)
##our guide##

class StudentUpdateView(UpdateView):
    model = Students
    fields = ('studentname', 'gradegroup',)
    context_object_name = 'student'
    template_name = 'classroom/parents/student_change_form.html'
