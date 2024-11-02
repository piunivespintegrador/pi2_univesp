import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.http import JsonResponse

from .models import Cliente

# Principal

def dashboard(request):
    return render(request, 'resources/home/dashboard.html')

# Consultar

def manager_customer(request):
    clientes = Cliente.objects.all()
    # 10 clientes por página
    paginator = Paginator(clientes, 8)

    # Obter o número da página atual da URL
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    return render(request, 'resources/customer/manager_customer.html',  {'page': page})

def manager_scheduling(request):
    return render(request, 'resources/scheduling/manager_scheduling.html')

def manager_service(request):
    return render(request, 'resources/service/manager_service.html')

def manager_type_service(request):
    return render(request, 'resources/type_service/register_type_service.html')

def manager_type_vehicle(request):
    return render(request, 'resources/type_vehicle/register_type_vehicle.html')

# Cadastrar

def register_customer(request):
    return render(request, 'resources/customer/register_customer.html')

def register_scheduling(request):
    return render(request, 'resources/scheduling/register_scheduling.html')

def register_service(request):
    return render(request, 'resources/service/register_service.html')

def register_type_service(request):
    return render(request, 'resources/type_service/register_type_service.html')

def register_type_vehicle(request):
    return render(request, 'resources/type_vehicle/register_type_vehicle.html')

# Editar

def edit_customer(request):
    return render(request, 'resources/customer/edit_customer.html')

def edit_scheduling(request):
    return render(request, 'resources/scheduling/edit_scheduling.html')

def edit_service(request):
    return render(request, 'resources/service/edit_service.html')

def edit_type_service(request):
    return render(request, 'resources/type_service/edit_type_service.html')

def edit_type_vehicle(request):
    return render(request, 'resources/type_vehicle/edit_type_vehicle.html')

# Excluir

# View para excluir cliente
@csrf_exempt
def delete_customer(request):
    if request.method == 'POST':
        try:
            # Carrega o corpo da requisição como JSON
            data = json.loads(request.body)

            # Extrai o ID do cliente
            customer_id = data.get('id')  

            # Tenta obter o cliente e excluir
            cliente = Cliente.objects.get(id=customer_id)
            cliente.delete()

            return JsonResponse({'success': True, 'message': f'Cliente {customer_id} excluído com sucesso.'})

        except Cliente.DoesNotExist:
            return JsonResponse({'success': False, 'message': f'Cliente {customer_id} não encontrado.'})
        
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Erro ao excluir o cliente {customer_id}.'})

    return JsonResponse({'success': False, 'message': 'Method not allowed'})

# Business Intelligence (BI)

def bi_report(request):
    return render(request, 'resources/business_intelligence/bi_report.html')

def bi_analysis(request):
    return render(request, 'resources/business_intelligence/bi_analysis.html')

# Site Edit

def site_edit(request):
    return render(request, 'resources/site/site_edit.html')