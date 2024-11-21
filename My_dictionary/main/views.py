from django.shortcuts import redirect, render, get_object_or_404
from .models import Word
from .forms import WordForm
from django.http import JsonResponse
from django.db.models import Q

def index(request):
    return render(request, 'main/index.html')

def addnewword(request, id=None):
    error = ''
    if id:
        word = get_object_or_404(Word, id=id)
        form = WordForm(request.POST or None, instance=word)
    else:
        form = WordForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('wordslist')
        else:
            # Здесь мы не используем error, так как ошибки уже в форме
            error = 'Ошибка при добавлении слова. Проверьте введенные данные.'

    data = {
        'form': form,
        'error': error,
        'word': word if id else None
    }
    
    return render(request, 'main/addnewword.html', data)

def wordslist(request):
    search_query = request.GET.get('search', '')  # Получаем строку поиска
    sort_order = request.GET.get('sort', 'asc')  # Получаем порядок сортировки

    words = Word.objects.all()

    if search_query:
        words = words.filter(Q(word__icontains=search_query) | Q(meaning__icontains=search_query))

    # Сортировка по возрастанию или убыванию
    if sort_order == 'desc':
        words = words.order_by('-word')  # Сортировка по убыванию
    else:
        words = words.order_by('word')  # Сортировка по возрастанию

    return render(request, 'main/wordslist.html', {'words': words, 'search_query': search_query, 'sort_order': sort_order})

def deleteword(request, id):
    if request.method == 'POST':
        word = get_object_or_404(Word, id=id)
        word.delete()
        return JsonResponse({'success': True})  # Возвращаем JSON-ответ
    return JsonResponse({'success': False}, status=400)  # Если не POST