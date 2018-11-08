from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import AdminSite

#this is for the sum computation



from django.db.models import Avg, Max, Sum, Min
#for flatpage

# from django.contrib.flatpages.admin import FlatPageAdmin
# from django.contrib.flatpages.models import FlatPage
# from django.utils.translation import gettext_lazy as _

## end of flatpagetest
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,Faculty, GradeYear, Subjects, CharacterBuildingActivities, StudentBio, Students, ParentsInfo, PresentCondition, IllnessInfo, HospitalInfo,AccidentInfo, ImmunisationInfo, StudentGrades, ObservationLists, CharacterObservation, StatementAccount, Compute
# Register your models here.

admin.site.site_header = 'Learning Garden Montessori Administration'



#this goes to a different path - students-admin
class StudentsAdminSite(AdminSite):
    site_header = "Learning Garden Montessori Admin"
    site_title = 'LGMS Admin Portal'
    index_tite = 'Welcome to LGMS Admin Portal'

students_admin_site = StudentsAdminSite(name = 'students_admin')

#FOR USERS
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'name','fathersname', 'guardiansname', 'address', 'childsname', 'dateofbirth', 'dateuserjoined', 'mobilenumber', 'homenumber','civilstatus', 'religion', 'studentname', 'applicationtype', 'studentbioidinfo']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'mobilenumber', 'address', 'dateofbirth', 'dateuserjoined', 'civilstatus', 'religion', 'studentname', 'applicationtype', 'profilepic',  'studentbioidinfo')}),
    )
    search_fields = ('username',)
    ordering = ('email',)
    filter_horizontal = ()

UserAdmin.add_fieldsets = (

        (None, {
        'classes': ('wide', 'extrapretty'),
        'fields': ('email', 'username', 'password1', 'password2', 'name', 'address', 'mobilenumber', 'homenumber',)
        }),
            #
            # 'classes': ('wide',),
            # 'fields' : ('email', 'password', 'username', 'name', 'address', 'dateofbirth', 'dateuserjoined', 'mobilenumber', 'civilstatus', 'religion', 'childsname')
    )

# FOR STUDENT BIO IN PROFILE
class StudentBioAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'studentname','momsname', 'popsname', 'guardiansname', 'gradeyear', 'financialinfo', 'profilepic']
    search_fields = ['studentname__studentname']
    list_filter = ['gradeyear']
    #fields = ['user','studentname', 'momsname', 'popsname', 'guardiansname', 'gradeyear', 'teachersname', 'subjects', 'charactersets']
    filter_horizontal = [ 'facultyname', 'subjects','charactersets']
    #this has been added to test if we can edit the field
    fieldsets = (
        (None, {
        'classes': ('wide', 'extrapretty'),
        'fields': ('user', 'studentname','momsname', 'popsname', 'guardiansname', 'gradeyear', 'teachersname', 'subjects', 'charactersets', 'financialinfo', 'profilepic'),
        }),
    )

class ParentsInfoAdmin(admin.ModelAdmin):
    list_display = ['mothersname', 'fathersname', 'guardiansname', 'address', 'email', 'mobilenumber' ]
    search_fields = ['mothersname__mothersname']
    list_filter = ['email']
    fields = ['mothersname', 'fathersname', 'guardiansname', 'address', 'email', 'mobilenumber' ]


class FacultyAdmin(admin.ModelAdmin):
    list_display = ['facultyname', 'email', 'faculty_id', 'birthday', 'rolegroup']

class StudentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'studentname', 'student_id', 'birthday', 'lrn_no', 'groupinfo']
    search_fields = ['studentname__studentname']

class StudentGradesAdmin(admin.ModelAdmin):
    list_display = ['studentname', 'facultyname', 'subjectname', 'grades', 'dateperiod']
    fields  = ['studentname', 'facultyname', 'subjectname', 'grades', 'dateperiod']
    search_fields = ['studentname__studentname']
    list_filter = ['studentname']

# class CharacterRatingsAdmin(admin.ModelAdmin):
#     list_display = ['studentname', 'charactersets', 'chargrades', 'dateadded']
#     fields = ['studentname', 'charactersets', 'chargrades', 'dateadded']
#     search_fields = ['studentname__studentname']
#     list_filter = ['chargrades']


class CharacterObservationAdmin(admin.ModelAdmin):
    list_display = ['studentname', 'observationsets', 'observegrades', 'dateadded']
    fields = ['studentname', 'observationsets', 'observegrades', 'dateadded']
    search_fields = ['studentname__studentname']
    list_filter = ['observegrades']

class StatementAccountAdmin(admin.ModelAdmin):
    list_display =['studentname', 'gradeyear', 'modeofpayment', 'modeofpaymentprice', 'modeofpaymenttotal', 'musicclassprice', 'bookspricetotal', 'notebooks', 'uniforms', 'other', 'totalprice', 'reservationfee', 'discount', 'gtotal']
    fields =['studentname', 'gradeyear', 'modeofpayment',  'modeofpaymentprice', 'modeofpaymenttotal', 'musicclassprice', 'bookspricetotal', 'notebooks', 'uniforms', 'other','totalprice', 'reservationfee', 'discount','gtotal']
    search_fields = ['studentname__studentname']
    list_filter = ['studentname',]
    list_summary = ('Total price', Sum('musicclassprice', 'booksprice', 'uniforms', 'notebooks','other', 'reservationfee'))

    # def get_queryset(self, request):
    #     return super(StatementAccountAdmin, self).get_queryset(request).annotate(
    #     musicclassprice=Sum('music_price'),
    #     bookspricetotal=Sum('books_price'))

        #totaltest = StatementAccount.objects.all().aggregate(Sum("Total Price", gtotal=IntegerField()))


    # @easy.smart(short_description="Total Price Sum", admin_order_field='musicclassprice', allow_tags=True)
    # def gtotal(self, obj):
    #     sum_result = obj.musicclassprice + obj.bookspricetotal + obj.notebooks + obj.uniforms + obj.other
    #     + obj.reservationfee + obj.discount
    #     return '<b>%s</b>' % sum_result



class ComputeAdmin(admin.ModelAdmin):
    list_display = ['studentname', 'testpayment1', 'testpayment2' ]


class PresentConditionAdmin(admin.ModelAdmin):
    list_display = ['user','name', 'currentcondition', 'conditiondetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']
    fields = ['user', 'name', 'currentcondition', 'conditiondetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']
    search_fields = ['name__name']
    list_filter = ['name', ]


class IllnessInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'illnessinfo', 'illnessdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']
    fields = ['name', 'illnessinfo', 'illnessdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']
    search_fields = ['name__name']
    list_filter = ['name',]


class HospitalInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'reasonforhospital', 'hospitalisationdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']
    fields = ['name', 'reasonforhospital', 'hospitalisationdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']
    search_fields = ['name__name']
    list_filter = ['name',]


class AccidentInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'accidentdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']
    fields = ['name', 'accidentdetails', 'treatmentdetails', 'startperiodofillness', 'endperiodillness']
    search_fields = ['name__name']
    list_filter = ['name',]


class ImmunisationInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'immunedetails', 'treatmentdetails', 'startperiodofimmune', 'endperiodimmune']
    fields = ['name', 'immunedetails', 'treatmentdetails', 'startperiodofimmune', 'endperiodimmune']
    search_fields = ['name__name']
    list_filter = ['name',]

# admin.site.unregister(FlatPage)
# admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(Compute, ComputeAdmin)
admin.site.register(StatementAccount, StatementAccountAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ParentsInfo, ParentsInfoAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(GradeYear)
admin.site.register(Subjects)
admin.site.register(CharacterBuildingActivities)

# admin.site.register(MedicalRecords, MedicalRecordsAdmin)
admin.site.register(StudentBio, StudentBioAdmin)
admin.site.register(Students, StudentsAdmin)
admin.site.register(PresentCondition, PresentConditionAdmin)
admin.site.register(IllnessInfo, IllnessInfoAdmin)
admin.site.register(HospitalInfo, HospitalInfoAdmin)
admin.site.register(AccidentInfo, AccidentInfoAdmin)
admin.site.register(ImmunisationInfo, ImmunisationInfoAdmin)
admin.site.register(StudentGrades, StudentGradesAdmin)
# admin.site.register(CharacterRatings, CharacterRatingsAdmin)
admin.site.register(ObservationLists)
admin.site.register(CharacterObservation, CharacterObservationAdmin)
# admin.site.register(AssessmentStudents)


#admin.site.register(GuidelinesTraits)
#admin.site.register(Children)
# admin.site.register(StudentBio)


#test for adding subjects in line
# class SubjectsInline(admin.StackedInline):
#     model = StudentBio.subjects.through
#
# class StudentBioAdmin(admin.ModelAdmin):
#     inlines = [
#         SubjectsInline,
#     ]
#
# class StudentBioAdmin(admin.ModelAdmin):
#     inlines =[
#         SubjectsInline,
#     ]
#
# class CharactersetsInline(admin.StackedInline):
#     model = StudentBio.charactersets.through

#test for adding subjects in line


# class FlatPageAdmin(FlatPageAdmin):
#     fieldsets = (
#         (None, {'fields' : ('url', 'title', 'content', 'sites')})
#         (_('Advanced options'),{
#             'classes': ('collapse',),
#             'fields':(
#                 'enable_comments',
#                 'registration_required',
#                 'template_name',
#             ),
#         }),
#     )
