from django import forms
from django.forms import ModelForm
from django.forms import ModelForm, TextInput
from .models import Word
import re

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
        
    def clean_word(self):
        word = self.cleaned_data.get('word')
        # Регулярное выражение для проверки на наличие цифр или специальных символов
        if not re.match("^[A-Za-zА-Яа-яЁё]+$", word):  # Позволяет только буквы
            raise forms.ValidationError("Слово не должно содержать цифры или специальные знаки.")
        return word
    
    def clean_meaning(self):
        meaning = self.cleaned_data.get('meaning')
        # Регулярное выражение для проверки на наличие цифр или специальных символов
        if not re.match("^[A-Za-zА-Яа-яЁё\s]+$", meaning):  # Позволяет только буквы и пробелы
            raise forms.ValidationError("Значение не должно содержать цифры или специальные знаки.")
        return meaning