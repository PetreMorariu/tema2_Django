import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

list_of_names = []
list_of_ages = []
list_combined = []
list_of_18 = []

def home(request):
    return HttpResponse("OK")

@csrf_exempt
@require_http_methods(["POST"])
def name_list(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            names = data.get('list', [])
            list_of_names.clear()
            list_of_names.extend(names)
            print(list_of_names)
            return HttpResponse("List of names received!", status=201)
        except Exception as e:
            return HttpResponse(str(e), status=400)

@csrf_exempt
@require_http_methods(["POST"])
def age_list(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            ages = data.get('list_age', [])
            list_of_ages.clear()
            list_of_ages.extend(ages)
            print(list_of_ages)
            return HttpResponse("List of ages received!", status=201)
        except Exception as e:
            return HttpResponse(str(e), status=400)

@csrf_exempt
@require_http_methods(["GET"])
def combine_name_with_age(request):
    if request.method == 'GET':
        if len(list_of_names) == len(list_of_ages):
            try:
                list_combined.clear()
                for name, age in zip(list_of_names, list_of_ages):
                    my_dict = {'name': name, 'age': age}
                    list_combined.append(my_dict)
                return JsonResponse(list_combined, safe=False)
            except Exception as e:
                return HttpResponse(str(e), status=400)
        else:
            return HttpResponse("The received list for name and age do not have the same number of elements!")


@csrf_exempt
@require_http_methods(["GET"])
def person_of_age(request):
    if request.method == 'GET':
        try:
            list_of_18.clear()
            list_of_18.extend([
                {'name': p['name'], 'age': p['age']}
                for p in list_combined if p['age'] >= 18
            ])
            return JsonResponse(list_of_18, safe=False)
        except Exception as e:
            return HttpResponse(str(e), status=400)