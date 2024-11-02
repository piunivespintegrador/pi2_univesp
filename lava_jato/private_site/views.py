from django.shortcuts import render

# Principal

def dashboard(request):
    return render(request, 'resources/dashboard.html')

# Consultar

def manager_customer(request):
    return render(request, 'resources/manager_customer.html')

def manager_scheduling(request):
    return render(request, 'resources/manager_scheduling.html')

def manager_service(request):
    return render(request, 'resources/manager_service.html')

def manager_type_service(request):
    return render(request, 'resources/register_type_service.html')

def manager_type_vehicle(request):
    return render(request, 'resources/register_type_vehicle.html')

# Cadastrar

def register_customer(request):
    return render(request, 'resources/register_customer.html')

def register_scheduling(request):
    return render(request, 'resources/register_scheduling.html')

def register_service(request):
    return render(request, 'resources/register_service.html')

def register_type_service(request):
    return render(request, 'resources/register_type_service.html')

def register_type_vehicle(request):
    return render(request, 'resources/register_type_vehicle.html')

# Editar
# Ess

def edit_customer(request):
    return render(request, 'resources/edit_customer.html')

def edit_scheduling(request):
    return render(request, 'resources/edit_scheduling.html')

def edit_service(request):
    return render(request, 'resources/edit_service.html')

def edit_type_service(request):
    return render(request, 'resources/edit_type_service.html')

def edit_type_vehicle(request):
    return render(request, 'resources/edit_type_vehicle.html')

# Business Intelligence (BI)

def bi_report(request):
    return render(request, 'resources/bi_report.html')

def bi_analysis(request):
    return render(request, 'resources/bi_analysis.html')

# Site Edit

def site_edit(request):
    return render(request, 'resources/site_edit.html')