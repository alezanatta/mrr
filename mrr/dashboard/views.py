from django.http import HttpResponseNotAllowed
from django.shortcuts import render

import datetime
# Create your views here.

from .forms import PeriodoForm

from .models import FatoMrr


def index(request):

    context = {}

    if request.method == "GET":
        dt_fim = datetime.date.today()
        primeiro = dt_fim.replace(day=1)
        dt_inicio = str(primeiro - datetime.timedelta(days=1825))

        FatoMrr.get_dashboard(dt_inicio)        

    elif request.method == "POST":
        form = PeriodoForm(request.POST)
        if form.is_valid():
            dt_inicio = form.cleaned_data["dt_inicio"]
            dt_fim = form.cleaned_data["dt_fim"]
            FatoMrr.get_dashboard(str(dt_inicio), str(dt_fim))
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
    
    form = PeriodoForm(initial={
        "dt_inicio":str(dt_inicio),
        "dt_fim":str(dt_fim)
    })
    context["form"] = form

    return render(request, "dashboard/dashboard.html", context)
