from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import random


def index(request):
    return render(request, 'index.html')


@csrf_exempt
@api_view(['POST'])
def name_drawer(request):
    lista = request.data.get('text', '')
    lista = str(lista).split(',')

    nome_sorteado = random.choice(lista)

    return Response({
        'nomes': lista,
        'sorteado': nome_sorteado
    })


@csrf_exempt
@api_view(['POST'])
def number_drawer(request):
    primeiro_n = int(request.data.get('n1', 0))
    segundo_n = int(request.data.get('n2', 0))

    menor = min(primeiro_n, segundo_n)
    maior = max(primeiro_n, segundo_n)

    numero_sorteado = random.randint(menor, maior)

    return Response({
        'numero1': primeiro_n,
        'numero2': segundo_n,
        'menor_intervalo': menor,
        'maior_intervalo': maior,
        'sorteado': numero_sorteado
    })
