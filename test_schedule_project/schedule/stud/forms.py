from django import forms
from .models import ExtracurricularActivity, StudySchedule

class ActivityForm(forms.ModelForm):
    class Meta:
        model = ExtracurricularActivity
        fields = ['activity', 'day_of_week', 'start_time', 'end_time']
        widgets = {'start_time': forms.TimeInput(format='%H:%M', attrs={'type':'time'}),
                   'end_time': forms.TimeInput(format='%H:%M', attrs={'type':'time'}),
                   }

class StudForm(forms.ModelForm):
    class Meta:
        model = StudySchedule
        fields = ['subject', 'day_of_week', 'start_time', 'end_time']
        widgets = {'start_time': forms.TimeInput(format='%H:%M', attrs={'type':'time'}),
                   'end_time': forms.TimeInput(format='%H:%M', attrs={'type':'time'}),
                   }