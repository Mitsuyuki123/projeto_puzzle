from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    if request.method == 'POST':

        order = request.POST.get('order')

        print(f'==========>{order}')

        if order == "A,B,C":
            return redirect('02')

    return render(request, 'htmls/01.html')


def zerotwo(request):
    return render(request, 'htmls/02.html')
