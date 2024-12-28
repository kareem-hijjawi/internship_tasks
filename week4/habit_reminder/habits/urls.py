from django.urls import path
from .views import HabitsListView

urlpatterns = [
    path('', HabitsListView.as_view(), name='index'),  
]
