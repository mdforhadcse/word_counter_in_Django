from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    text = request.GET.get('words')
    if text == None:
        text = ' '
    number_of_words = len(text.split())
    print(text)
    return render(request, 'base/index.html', {'number_of_words': number_of_words})
