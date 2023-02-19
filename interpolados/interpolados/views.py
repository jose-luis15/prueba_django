from django.shortcuts import render, redirect
from .models import CcMontos

# Create your views here.
#1. función para listar tareas
def list_tasks(request):
    cc = CcMontos.objects.all()
    return render(request,'list_tasks.html', {"cc": cc})

# from django.urls import path
# from ..interpolados.views import list_tasks

# urlpatterns = [
#     path('', list_tasks)
# ]