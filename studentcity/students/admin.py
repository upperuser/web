from django.contrib import admin
from .models import Student, Group

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'middle_name', 'curs',
                    'record_book','group')
    list_display_links = ('id', 'last_name')
    search_fields = ('last_name', 'first_name')
    list_editable = ('curs',)
    list_filter = ('curs', 'group')
admin.site.register(Student, StudentAdmin)
admin.site.register(Group)



# Register your models here.
