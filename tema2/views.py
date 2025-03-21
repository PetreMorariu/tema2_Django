import json

from django.http import HttpRequest,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

list_of_names = []

def home(request):
    return HttpResponse("OK")

@csrf_exempt
@require_http_methods(["POST"])
def name_list(request: HttpRequest):
    if request.method == "POST":
        try:
            list_of_names.clear()
            data = json.loads(request.body)
            list_of_names = data['list']
            print(list_of_names)
            return HttpResponse("List received!", status=201)
        except Exception as e:
            return HttpResponse(str(e), status=400)
