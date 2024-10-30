from django.forms import ModelForm, TextInput
from .models import Word

class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'meaning']
        
        widgets = {
            'word': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите слово',
            }),
            'meaning': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите значение',
            })
        }