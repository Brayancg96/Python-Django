from django import forms

class CreateNewTasks(forms.Form):

    id = forms.CharField(label="Id del proyecto", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    title = forms.CharField(label="Titulo de tarea", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label="Descripcion de la tarea", widget=forms.Textarea(attrs={'class': 'input'}))

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))