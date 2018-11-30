from django.urls import path, include

from students.views import StudentBioList, IllnessInfoCreate, IllnessInfoUpdate, IllnessInfoDelete, PresentConditionCreate, PresentConditionUpdate, PresentConditionDelete, HospitalInfoCreate, HospitalInfoUpdate, HospitalInfoDelete, AccidentInfoCreate, AccidentInfoUpdate, AccidentInfoDelete, ImmunisationInfoCreate, ImmunisationInfoUpdate, ImmunisationInfoDelete



from django.contrib.flatpages import views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

##this is where we add the views added
from . addviews import parents, teachers
#name can be used for reverse function
# commented out from airline example
# path("<int:flight_id>", views.flight, name="flight"),
# path("<int:flight_id>/book", views.book, name="book")

# http://127.0.0.1:8000/home/8/

urlpatterns = [

     path('teachers/', include(([
        path('', teachers.TeachersView.as_view(), name='teacherspage'),
    ], 'students'), namespace='teachers')),


    path('parents/', include(([
        path('', parents.ParentsView.as_view(), name="parentspage"),
    ], 'students'), namespace='parents')),

    #test for the downloadview
    #test for the downloadview
    path('signup/', views.SignUp.as_view(), name='signup'),

    #experiment of putting login to home.html
    #path('accounts/login', auth_views.LoginView.as_view(template_name='students/home.html')),

    #this is a test for customising direction for login and signup form
    #path('home', views.login_form, name='login_form'),
    #path('home', views.signup_form, name='signup_form'),

    # path('signup/parents/', views.StudentSignupView.as_view(), name='signup_parents'),
    # path('signup/teachers/', views.TeachersSignupView.as_view(), name='signup_teachers'),
    #this is for flapages url start
    path('home/', views.home, name="home"),
    path('news/', views.news, name="news"),
    path('admission/', views.admission, name="admission"),
    path('gallery/', views.gallery, name="gallery"),
    path('online/', views.online, name="online"),
    #this is for flapages url end
    #this is for the download part
    #this is for flapages url end

###this is a test for signup##########



######signup test####################

    path('portal/', views.studentbioid, name="studentbioid"),
    path('portal/<int:pk>/', views.studentbioid, name="studentbioid"),
#this is for editprofile
    path('editprofile/', views.editprofile, name='editprofile'),

    path('medicalform/', views.presentcondition, name='presentcondition'),
#this is for editprofile
    path('changepassword/', views.changepassword, name='changepassword'),
    path('testlist/', StudentBioList.as_view(), name='studentbiolist'),

    #testing for MEDICAL CONDITION FORMs
    path('presentcondition/add/', PresentConditionCreate.as_view(), name='presentcondition-add'),
    path('presentcondition/<int:pk>/', PresentConditionUpdate.as_view(), name='presentcondition-update'),
    path('presentcondition/<int:pk>/delete/', PresentConditionDelete.as_view(), name='presentcondition-delete'),

    #testing for IllnessForm
    path('illnessinfo/add/', IllnessInfoCreate.as_view(), name='illnessinfo-add'),
    path('illnessinfo/<int:pk>/', IllnessInfoUpdate.as_view(), name='illnessinfo-update'),
    path('illnessinfo/<int:pk>/delete/', IllnessInfoDelete.as_view(), name='illnessinfo-delete'),

    #testing for Hospital Form
    path('hospitalinfo/add/', HospitalInfoCreate.as_view(), name='hospitalinfo-add'),
    path('hospitalinfo/<int:pk>/', HospitalInfoUpdate.as_view(), name='hospitalinfo-update'),
    path('hospitalinfo/<int:pk>/delete/', HospitalInfoDelete.as_view(), name='hospitalinfo-delete'),

    #testing for AccidentInfo Form
    path('accidentinfo/add/', AccidentInfoCreate.as_view(), name='accidentinfo-add'),
    path('accidentinfo/<int:pk>/', AccidentInfoUpdate.as_view(), name='accidentinfo-update'),
    path('accidentinfo/<int:pk>/delete/', AccidentInfoDelete.as_view(), name='accidentinfo-delete'),


    #testing for ImmuneInfo Form
    path('immunisationinfo/add/', ImmunisationInfoCreate.as_view(), name='immunisationinfo-add'),
    path('immunisationinfo/<int:pk>/', ImmunisationInfoUpdate.as_view(), name='immunisationinfo-update'),
    path('immunisationinfo/<int:pk>/delete/', ImmunisationInfoDelete.as_view(), name='immunisationinfo-delete'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#this is for home
    #path("studentbio/<int:pk>", views.student, name="student"),

    #cheatsheet for getting primary key
    # path("<int:flight_id>", views.flight, name="flight"),
    # path("<int:flight_id>/book", views.book, name="book"),

    #not workin
    # path('home/', views.SubjectDetailView.as_view(), name="subject_detail_view"),

    #path('studentprofile/', StudentProfileView.as_view()),


    # path('studentprofile/', views.studentprofile, name='studentprofile'),

    #path('studentbioinfo/', views.DetailInfo.as_view()),
