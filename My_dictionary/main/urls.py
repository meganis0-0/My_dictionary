from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_word/', views.addnewword, name='addnewword'),
    path('add_word/<int:id>/', views.addnewword, name='editword'),  # Для редактирования
    path('words_list/', views.wordslist, name='wordslist'),
    path('delete_word/<int:id>/', views.deleteword, name='deleteword'),  # Для удаления
]