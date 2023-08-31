from django.contrib import admin
from .models import Emp, Testimonials

# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display = ('name','empId', 'phone', 'working')
    list_editable = ('working',)
    search_fields = ('name',)
    # list_filter=('working',)

admin.site.register(Emp, EmpAdmin)
admin.site.register(Testimonials)
