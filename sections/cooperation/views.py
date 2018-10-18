from django.shortcuts import render


def index(request):
    return render(request, "cooperation/cooperation.html")