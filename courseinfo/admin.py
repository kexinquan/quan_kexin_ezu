from django.contrib import admin

# Register your models here.
from .models import Semester, Section, Course, Instructor, Registration, Period, Year, Student

admin.site.register(Semester)
admin.site.register(Section)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Registration)
admin.site.register(Period)
admin.site.register(Year)
admin.site.register(Student)