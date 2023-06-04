from django import forms
from .models import task
from tempus_dominus.widgets import DateTimePicker
from django.utils.translation import gettext_lazy as _

class Task_Form(forms.ModelForm):
    class Meta:
        model = task
        fields = ('task_name','task_date')
        widgets = {
            'task_name': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'Placeholder': 'Um título de sua tarefa'
                
                }
                
            ),
            'task_date': DateTimePicker(
                options={
                    'useCurrent': True,
                    'collapse': True,
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                    'Placeholder': 'Escolha...'
                },
            ),
        }
        labels = {
            "task_name": _("Título da Tarefa"),
            "task_date": _("Data")
        }
