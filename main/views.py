from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306210115',
        'name': 'Arief Ridzki Darmawan',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
