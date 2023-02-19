from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Student
from .models import Teacher


# class ProfileInline(admin.StackedInline):
#     model = Student
#     can_delete = False
#     verbose_name_plural = 'Profile'
#     fk_name = 'user'

# class CustomUserAdmin(UserAdmin):
#     inlines = (ProfileInline, )

#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomUserAdmin, self).get_inline_instances(request, obj)

# # admin.site.unregister(User)
# admin.site.register(Student)
# # admin.site.unregister(Student)
# admin.site.register(User,CustomUserAdmin)
# admin.site.register(Teacher)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    # pass
   

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass