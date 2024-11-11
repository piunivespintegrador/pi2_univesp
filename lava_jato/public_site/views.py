from django.shortcuts import render
from django.http import JsonResponse

# Home
def home(request):
    return render(request, 'resources/home.html')

# Health
def health(request):
    return JsonResponse({'health': f'alive'})