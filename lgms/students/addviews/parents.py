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
from .. models import CustomUser

from .. forms import ParentsSignUpForm

class ParentsView(CreateView):
    model = CustomUser
    form_class = ParentsSignUpForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'parents'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('students/parentspage.html') #this needs to be changed

######################
