from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=50, blank=False, unique=True)
    meaning = models.TextField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'
        