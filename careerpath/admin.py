from django.contrib import admin

from .models import User, Course, UserCourses, UserMentor, Mentor

# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(UserCourses)
admin.site.register(UserMentor)
admin.site.register(Mentor)