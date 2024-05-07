from django import forms

class createNewTask(forms.Form):
    title=forms.CharField(label="titulo de la tarea", max_length=200,widget=forms.TextInput({'class':'input'}))
    description=forms.CharField(label="descripcion de la tarea" ,widget=forms.Textarea({'class':'input'}))

class createNewProject(forms.Form):
    name=forms.CharField(label="titulo del proyecto", max_length=200)
