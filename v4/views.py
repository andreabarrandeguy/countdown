from django.shortcuts import render, redirect
from datetime import datetime as dt

# Create your views here.
def indexV4(request):
    if request.method == "POST":
        targetdate = request.POST["targetdate"]
        title = request.POST["title"]

        if targetdate and title:
            td = dt.strptime(targetdate, '%Y-%m-%dT%H:%M')
            now = dt.now()

            if td > now:
                # Obtener los componentes de fecha y hora
                year = td.year
                month = td.month
                day = td.day
                hour = td.hour
                minute = td.minute
                title = title
                
                # Redirigir al usuario a la página con la ruta dinámica
                return redirect('dynamic', Y=year, m=month, d=day, H=hour, M=minute, title=title)
            
            return render(request, "v4/error.html", {
            "error": "Please enter a date in the future"
            })
        
        return render(request, "v4/error.html", {
            "error": "Please enter a title and date"
        })
    
        # Todavia no, pero tengo que generar una view para cuando pare el countdown
    return render(request, "v4/input.html")


def dynamic(request, Y, m, d, H, M, title):
    return render(request, "v4/output.html", {
        "Y": Y,
        "m": m,
        "d": d,
        "H": H,
        "M": M,
        "title": title
    })