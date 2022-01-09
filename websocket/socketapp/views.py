# Импортировать модуль рендеринга из Django
from django.shortcuts import render

# Создать функцию индекса для отображения HTML-файла в браузере
def index(request):
    return render(request, "index.html", context={'text': 'AndreyEx'})