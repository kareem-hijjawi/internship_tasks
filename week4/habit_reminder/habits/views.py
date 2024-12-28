from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django.shortcuts import redirect
from .models import Habit
from .forms import HabitForm

class HabitsListView(FormMixin, ListView):
    model = Habit
    template_name = 'habits/index.html'  # Template to render
    context_object_name = 'habits'  # Name of the list passed to the template
    form_class = HabitForm  # Form for adding habits

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()  # Pass the form to the template
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the same page
        return self.get(request, *args, **kwargs)  # Show the page with errors
