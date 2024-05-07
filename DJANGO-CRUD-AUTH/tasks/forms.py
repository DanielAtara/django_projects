from django.forms import ModelForm
from .models import tasks

class tasksform(ModelForm):
    class Meta:
        model= tasks
        fields=['title', 'description', 'important']
