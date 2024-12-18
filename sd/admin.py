from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ['id','NAME', 'QUALIFICATION', 'GENDER', 'YOP', 'AGE', 'SKILLS', 'DOB', 'ADDRESS', 'MOCK_RATING', 'DEPARTMENT']
    list_display_links = ['NAME']
