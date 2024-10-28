from django.shortcuts import render

def dashboard(request):
    return render(request, 'resources/dashboard.html')

def manage_scheduling(request):
    return render(request, 'resources/manage_scheduling.html')

def make_scheduling(request):
    return render(request, 'resources/make_scheduling.html')

def report(request):
    return render(request, 'resources/report.html')

def site_edit(request):
    return render(request, 'resources/site_edit.html')