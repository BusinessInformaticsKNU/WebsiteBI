from django.shortcuts import render
import BLL.collective

def index(request):
    title = 'Collective BI'
    _list = BLL.collective.get_students_list()
    return render(request, "collective/collective.html",
                  {'title': title,'list': _list })
def teachers(request):
    title = 'Collective BI (teachers)'
    return render(request, "collective/collective.html",
                  {'title': title, })
def administration(request):
    title = 'Collective BI (administration) '
    return render(request, "collective/collective.html",
                  {'title': title, })
def students(request):
    title = 'Collective BI (students)'
    return render(request, "collective/collective.html",
                  {'title': title, })
def postgraduate(request):
    title = 'Collective BI (students)'
    return render(request, "collective/collective.html",
                  {'title': title, })