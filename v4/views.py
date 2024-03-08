from django.shortcuts import render
from datetime import datetime as dt

# Create your views here.
def indexV4(request):
    if request.method == "POST":
        targetdate = request.POST["targetdate"]
        td = dt.strptime(targetdate, '%Y-%m-%dT%H:%M')
        now = dt.now()

        if td > now:
            return render(request, "v4/output.html", {
                "td": targetdate
            })
        
        return render(request, "v4/error.html")
    
        # Todavia no, pero tengo que generar una view para cuando pare el countdown
    return render(request, "v4/input.html")
