from django import forms
from .models import Habit

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        #fields to display in the form
        fields = ['task_name', 'reminder_time']