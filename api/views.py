from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Project
import json

# Create your views here.

def index(request):
    return HttpResponse("you are in api")

@csrf_exempt
def add(request):
    if request.method == "GET":
        return HttpResponse("You have to post a json")

    elif request.method == "POST":
        payload = json.loads(request.body.decode())
        payload["contact_id"] = payload["ID"]; del payload["ID"]
        new_project = Project(**payload)
        new_project.save()
        return HttpResponse("successfuly added")
