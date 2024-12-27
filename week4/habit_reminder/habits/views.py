from django.shortcuts import render, redirect
from .models import Habit
from .forms import HabitForm

# Create your views here.
def index(request):
    #retrieve all habits from the database
    
    habits = Habit.objects.all()
    
    #create an empty form for the template
    form = HabitForm()
    
    
        
    
    #if statement:
    if request.method == 'POST': #if the user submits the form
        form = HabitForm(request.POST)
        if form.is_valid():
            form.save() #save the new habit to the database
            return redirect('index') #redirec to the same page
        
    return render(request, 'habits/index.html', {'habits': habits, 'form': form})

    
    
