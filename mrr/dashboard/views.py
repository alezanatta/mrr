from django.shortcuts import render

import datetime
# Create your views here.

from .models import FatoMrr


def index(request):

    if request.method == "GET":
        hoje = datetime.date.today()
        primeiro = hoje.replace(day=1)
        ano_passado = str(primeiro - datetime.timedelta(days=1825))
        print(ano_passado)
        FatoMrr.get_dashboard(ano_passado)

    return render(request, "dashboard/dashboard.html", {})
