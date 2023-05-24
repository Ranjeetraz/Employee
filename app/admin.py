from django.contrib import admin
from app.models import CustomUser, EmployeeDetail


# Register your models here.
admin.site.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'email']
    fields = ['first_name', 'last_name', 'phone_number',  'email']

admin.site.register(EmployeeDetail) 
class EmployeeDetailAdmin(admin.ModelAdmin):
    list_display = ['emo_name', 'emp_role', 'salary', 'gender', 'emp_code', 'joined_date']   
    fields = ['emo_name', 'emp_role', 'salary', 'gender', 'emp_code']