"""platzigram views"""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
    """Return a greeting """
    now = datetime.now().strftime('%b %dth, %y -%H:%M hrs');
    return HttpResponse('Ho, hi! Current server time is {now}'.format(now=now));


# devulve pero esto es parte del reto
def hi2(request):
    """HI"""
    numbers = request.GET['numbers'];
    numbers = [int(n) for n in numbers.split(',')];

    asc = sorted(numbers);
    desc = sorted(numbers, reverse = True );

    return HttpResponse(

    	f"NUMEROS OBTENIDOS: {numbers} <br>Menor a mayor: {asc} <br>Mayor a menor: {desc}"

    )

# esta definicion es sobre el video 2
def sort_integeres(request):
	"""Return a JSON response with sorted integeres"""
	numbers = [int(i) for i in request.GET['numbers'].split(',')];
	sorted_ints = sorted(numbers);
	data = {
		'status': 'ok',
		'numbers': sorted_ints,
		'message': 'Integeres sorted successfully.'
	}

	return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

# esta def es para mandar nombre y edad
def say_hi(request, name, age):
	"""return a greeting"""
	if age < 12:
		message = 'Sorry {}, you are not allowed here'.format(name)
	else:
		message = 'Hello, {}: welcome to program Ing Fidel'.format(name)
 
	return HttpResponse(message)


# capitulo6_video_3_evidencias