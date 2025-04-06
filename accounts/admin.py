from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import UserManagementModel, StudentModel, StaffModel
from django.contrib.auth.models import Group


admin.site.unregister(Group)
admin.site.site_header = 'NICAS'
admin.site.site_title = 'NICAS Admin Portal'

class UserManagementAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'address', 'district', 'state', 'created_at', 'updated_at')
    search_fields = ('username',)

    fieldsets = (
        (None, {
            'fields': ('username', 'is_staff', 'phone', 'district', 'state', 'email', 'password', 'profile_pic'),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone', 'district', 'state', 'password1', 'password2', 'pincode', 'profile_pic'),
        }),
    )

    ordering = ('username',)

    def save_model(self, request, obj, form, change):
        obj.is_staff = True
        obj.save()
        super().save_model(request, obj, form, change)


class StaffModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'rollno', 'department', 'designation', 'created_at', 'updated_at')
    search_fields = ('user__username', 'user__email', 'rollno', 'department', 'designation')

    
    fieldsets = (
        (None, {
            'fields': ('user', 'department', 'designation'),
        }),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'department', 'designation')
        }),
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Filter the user dropdown to only show users with is_staff=True."""
        if db_field.name == "user":
            kwargs["queryset"] = UserManagementModel.objects.filter(is_staff=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class StudentModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'rollno', 'course', 'semester', 'created_at', 'updated_at')
    search_fields = ('user__username', 'user__email', 'rollno', 'course', 'semester')

    fieldsets = (
        (None, {
            'fields': ('user', 'course', 'semester',
                       'academic_fee', 'exam_fee', 'hostel_fee', 
                       'transport_fee', 'other_fee', 'balance_fee'),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'course', 'semester', 
                       'academic_fee', 'exam_fee', 'hostel_fee', 
                       'transport_fee', 'other_fee', 'balance_fee'),
        }),
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Filter the user dropdown to only show users with is_staff=False."""
        if db_field.name == "user":
            kwargs["queryset"] = UserManagementModel.objects.filter(is_staff=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def has_add_permission(self, request):
        """Prevent adding new students."""
        return False

    # def has_delete_permission(self, request, obj=None):
    #     """Prevent deleting students."""
    #     return False


admin.site.register(StaffModel, StaffModelAdmin)
admin.site.register(UserManagementModel, UserManagementAdmin)
admin.site.register(StudentModel, StudentModelAdmin)
