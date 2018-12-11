from django.urls import path, include
#from students.views import StudentBioList, IllnessInfoCreate, IllnessInfoUpdate, IllnessInfoDelete, PresentConditionCreate, PresentConditionUpdate, PresentConditionDelete, HospitalInfoCreate, HospitalInfoUpdate, HospitalInfoDelete, AccidentInfoCreate, AccidentInfoUpdate, AccidentInfoDelete, ImmunisationInfoCreate, ImmunisationInfoUpdate, ImmunisationInfoDelete



from django.contrib.flatpages import views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

##this is where we add the views added

from .views import mainviews, parents, teachers


#name can be used for reverse function
# commented out from airline example
# path("<int:flight_id>", views.flight, name="flight"),
# path("<int:flight_id>/book", views.book, name="book")

# http://127.0.0.1:8000/home/8/

urlpatterns = [

    path('home', mainviews.home, name ='home'),
    path('home/<int:pk>/', mainviews.studentbioid, name="studentbioid"),
    path('home/<int:pk>/', mainviews.studentmedpccheck, name="studentmedpccheck"),




    path('teachers/', include(([
        path('testonlyteacher', teachers.TeachersInfoView.as_view(), name='teachers_page'),
        path('addsubjects/', teachers.SubjectsTaughtView.as_view(), name='subject_handled'),
    ], 'students'), namespace='teachers')),
    #
    #
    path('parents/', include(([
        path('', parents.StudentsInfoView.as_view(), name='students_info'),
        path('studentslist/<int:pk>/', parents.StudentsListView.as_view(), name='students_view'),
        path('students/<int:pk>/', parents.StudentsDetailView.as_view(), name='students_details'),
        path('add/', parents.StudentsCreateView.as_view(), name='kids_list'),
    ], 'students'), namespace='parents')),




    path('mainviews/', include(([

        #home link
        path('portal/', mainviews.studentbioid, name='studentbioid'),

        path('portal/<int:pk>/', mainviews.studentbioid, name='studentbioid'),
    #this is for editprofile
        path('editprofile/', mainviews.editprofile, name='editprofile'),

        path('medicalform/', mainviews.presentcondition, name='presentcondition'),
    #this is for editprofile
        path('changepassword/', mainviews.changepassword, name='changepassword'),
        #path('testlist/', StudentBioList.as_view(), name='studentbiolist'),

        #testing for MEDICAL CONDITION FORMs
        path('presentcondition/add/', mainviews.PresentConditionCreate.as_view(), name='presentcondition-add'),
        path('presentcondition/<int:pk>/', mainviews.PresentConditionUpdate.as_view(), name='presentcondition-update'),
        path('presentcondition/<int:pk>/delete/', mainviews.PresentConditionDelete.as_view(), name='presentcondition-delete'),

        #testing for IllnessForm
        path('illnessinfo/add/', mainviews.IllnessInfoCreate.as_view(), name='illnessinfo-add'),
        path('illnessinfo/<int:pk>/', mainviews.IllnessInfoUpdate.as_view(), name='illnessinfo-update'),
        path('illnessinfo/<int:pk>/delete/', mainviews.IllnessInfoDelete.as_view(), name='illnessinfo-delete'),

        #testing for Hospital Form
        path('hospitalinfo/add/', mainviews.HospitalInfoCreate.as_view(), name='hospitalinfo-add'),
        path('hospitalinfo/<int:pk>/', mainviews.HospitalInfoUpdate.as_view(), name='hospitalinfo-update'),
        path('hospitalinfo/<int:pk>/delete/', mainviews.HospitalInfoDelete.as_view(), name='hospitalinfo-delete'),

        #testing for AccidentInfo Form
        path('accidentinfo/add/', mainviews.AccidentInfoCreate.as_view(), name='accidentinfo-add'),
        path('accidentinfo/<int:pk>/', mainviews.AccidentInfoUpdate.as_view(), name='accidentinfo-update'),
        path('accidentinfo/<int:pk>/delete/', mainviews.AccidentInfoDelete.as_view(), name='accidentinfo-delete'),


        #testing for ImmuneInfo Form
        path('immunisationinfo/add/', mainviews.ImmunisationInfoCreate.as_view(), name='immunisationinfo-add'),
        path('immunisationinfo/<int:pk>/', mainviews.ImmunisationInfoUpdate.as_view(), name='immunisationinfo-update'),
        path('immunisationinfo/<int:pk>/delete/', mainviews.ImmunisationInfoDelete.as_view(), name='immunisationinfo-delete'),
    ], 'students'), namespace='mainviews')),

    #test for the downloadview
    #test for the downloadview
    #path('signup/', views.SignUp.as_view(), name='signup'),

    #experiment of putting login to home.html
    #path('accounts/login', auth_views.LoginView.as_view(template_name='students/home.html')),

    #this is a test for customising direction for login and signup form
    #path('home', views.login_form, name='login_form'),
    #path('home', views.signup_form, name='signup_form'),

    # path('signup/parents/', views.StudentSignupView.as_view(), name='signup_parents'),
    # path('signup/teachers/', views.TeachersSignupView.as_view(), name='signup_teachers'),
    #this is for flapages url start

    #this is for flapages url end
    #this is for the download part
    #this is for flapages url end

###this is a test for signup##########



######signup test####################




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
