from django.shortcuts import render

# Create your views here.
def BASE (request):
    return render(request, 'base.html')

# def INNER (request):
#     return render(request, 'inner-page.html')