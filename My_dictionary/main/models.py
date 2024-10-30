from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=50)
    meaning = models.TextField()

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'
        