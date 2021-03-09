from django.contrib import admin
from testapp.models import student_register
# Register your models here.
class Student_SignupAdmin(admin.ModelAdmin):
	list_display=['user','location','type_of_user']
admin.site.register(student_register,Student_SignupAdmin)
