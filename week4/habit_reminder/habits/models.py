from django.db import models

# Create your models here:

class Habit(models.Model):
    #habit/task name
    task_name = models.CharField(max_length=255)
    #time for the reminder
    reminder_time = models.TimeField()
    
    def __str__(self):
        return self.task_name
    
