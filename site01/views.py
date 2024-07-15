from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    if request.method == 'POST':
        opt1 = request.POST.get('combination')
        opt2 = request.POST.get('option2')
        opt3 = request.POST.get('option3')
        sequence = request.POST.get('selectionOrder')

        # Processar a combinação de opções
        if opt1 and opt2 and opt3:
            # Lógica para processar a combinação de opções
            combination = str(opt1 + opt2 + opt3)
        else:
            combination = None
        print(f'==========>{combination}')
        print(f'==========>{sequence}')


        if combination == "AZ2":
            return redirect('02')

        # Retornar uma resposta com base na combinação
        #return HttpResponse(f"Você selecionou a combinação: {combination}")

    return render(request, 'htmls/01.html')


def zerotwo(request):
    return render(request, 'htmls/02.html')
