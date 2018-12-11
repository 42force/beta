"""lgms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from students.admin import students_admin_site
#this is the views page additional
from students.views import mainviews, teachers, parents
#apps stay here for url

urlpatterns = [

    path('', TemplateView.as_view(template_name='flatpages/about.html'), name='about'),
    path('', TemplateView.as_view(template_name='flatpages/gallery.html'), name='gallery'),
    path('', TemplateView.as_view(template_name='flatpages/admission.html'), name='admission'),
    path('', TemplateView.as_view(template_name='flatpages/calendar.html'), name='calendar'),
    path('', TemplateView.as_view(template_name='flatpages/careers.html'), name='careers'),
    path('', TemplateView.as_view(template_name='flatpages/news.html'), name='news'),
    path('', TemplateView.as_view(template_name='flatpages/online.html'), name='online'),
    #path('', TemplateView.as_view(template_name='students/home.html'), name='home'), # new


    #path('', TemplateView.as_view(template_name='students/home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('students-admin', students_admin_site.urls),
    path('', include('students.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', mainviews.SignUpView.as_view(), name='signup'),
    path('accounts/signup/parents', parents.ParentsView.as_view(), name="parentsview" ),
    path('accounts/signup/teacher', teachers.TeachersView.as_view(), name="teachersview"),
    path('pages/', include('django.contrib.flatpages.urls')),


]

    #path('studentprofile/', TemplateView.as_view(template_name='studentprofile')),
