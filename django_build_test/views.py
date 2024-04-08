from django.shortcuts import render

def hello_world(request, name):
    return render(request, 'hello_world.html')