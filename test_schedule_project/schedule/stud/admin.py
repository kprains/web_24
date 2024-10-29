from django.contrib import admin
from .forms import ActivityForm, StudForm
from .models import StudySchedule, ExtracurricularActivity

class ActivityAdmin(admin.ModelAdmin):
    form = ActivityForm
    list_display = ('activity', 'day_of_week', 'start_time', 'end_time')
    list_filter = ('activity', 'day_of_week')
    search_fields = ['activity']

admin.site.register(ExtracurricularActivity, ActivityAdmin)

class ActivityStud(admin.ModelAdmin):
    form = StudForm
    list_display = ('subject', 'day_of_week', 'start_time', 'end_time')
    list_filter = ('subject', 'day_of_week')
    search_fields = ['activity']
admin.site.register(StudySchedule, ActivityStud)


# Register your models here.
