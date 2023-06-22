from django.shortcuts import render

# Create your views here.
def MenuAdmin(request):
    return render(request, 'MenuAdmin.html')