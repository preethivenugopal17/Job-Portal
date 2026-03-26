from django.contrib import admin
from .models import Job, Application
# Register your models here.
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title','company','location','job_type','posted_at')
    list_filter = ('job_type',)
    search_fields = ('title','comapny','location')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display  = ('applicant', 'job', 'applied_at')
    list_filter   = ('job',)
    search_fields = ('applicant__username', 'job__title')
