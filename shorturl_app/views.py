from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.http import JsonResponse
import random
import string
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import ShortUrl, Statistics
import json

def generar_cadena_aleatoria():
    letras = string.ascii_letters  # Obtener todas las letras del alfabeto, mayúsculas y minúsculas
    return ''.join(random.choice(letras) for _ in range(6))  # Generar una cadena de 6 letras aleatorias




@csrf_exempt
def short_url(request):
    body = request.body.decode('utf-8')
    body = json.loads(body)
    if(request.method == 'POST'):
        try:
            if(body["url"] != ""):
                
                id_short = generar_cadena_aleatoria()
                short_url = f'https://localhost:8000/r/{id_short}'
                saveto = ShortUrl(url=body['url'], short_url=short_url, id_short=id_short)
                saveto.save()
                
                statics = Statistics(id_short=saveto)
                statics.save()
                
                
                
                data = {
                    "url": body["url"],
                    "short_url": short_url 
                }
                
                
            return JsonResponse(data=data, status=200)
        except:
            return JsonResponse({"Error": "Asegurate de mandar el campo url"}, status=400)
        
def redirects(request, short):
    if(request.method == 'GET'):
        shorted = ShortUrl.objects.get(id_short=short)
        visit = Statistics.objects.get(id_short=shorted)
        visit.number_visits += 1
        visit.save()
        return redirect(shorted.__str__())
        