from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from .. models import CustomUser
from .. forms import TeacherSignUpForm

##################teachers sign up view end###########################

class TeachersView(CreateView):
    model = CustomUser
    form_class = TeacherSignUpForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('students/teacherspage.html')

##################teacher sign up view end##########################
