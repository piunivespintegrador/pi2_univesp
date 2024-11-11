import json
import logging

from django.db import IntegrityError
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.http import JsonResponse

from .models import Cliente, Agendamento, Servico, TipoServico, TipoVeiculo

logger = logging.getLogger('django')

# Principal

def dashboard(request):
    return render(request, 'resources/home/dashboard.html')

# Health

def health(request):
    return JsonResponse({'health': f'alive'})

# Consultar

def manager_customer(request):
    clientes = Cliente.objects.all()
    # 8 clientes por página
    paginator = Paginator(clientes, 8)

    # Obter o número da página atual da URL
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    return render(request, 'resources/customer/manager_customer.html', {'page': page})

def manager_scheduling(request):
    agendamentos = Agendamento.objects.all()

    # Calcular a quantidade de horas trabalhadas para cada agendamento
    for agendamento in agendamentos:
        if agendamento.datetime_inicio and agendamento.datetime_fim:
            # Calculando a diferença entre as datas
            delta = agendamento.datetime_fim - agendamento.datetime_inicio
            # Convertendo a diferença para horas e minutos
            agendamento.duracao_horas = delta.total_seconds() / 3600  # total_seconds converte a diferença para segundos
            agendamento.duracao_horas = round(agendamento.duracao_horas, 2)  # Arredondar para 2 casas decimais
        else:
            agendamento.duracao_horas = 0  # Caso a data de início ou fim seja nula

    # 8 agendamentos por página
    paginator = Paginator(agendamentos, 8)

    # Obter o número da página atual da URL
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    return render(request, 'resources/scheduling/manager_scheduling.html', {'page': page})

def manager_service(request):
    services = Servico.objects.all()

    # 8 serviços por página
    paginator = Paginator(services, 8)

    # Obter o número da página atual da URL
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    return render(request, 'resources/service/manager_service.html', {'page': page})

def manager_type_service(request):
    tipos_service = TipoServico.objects.all()

    # 8 tipos de serviços por página
    paginator = Paginator(tipos_service, 8)

    # Obter o número da página atual da URL
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    return render(request, 'resources/type_service/manager_type_service.html', {'page': page})

def manager_type_vehicle(request):
    tipos_veiculo = TipoVeiculo.objects.all()

    # 8 tipos de veiculos por página
    paginator = Paginator(tipos_veiculo, 8)

    # Obter o número da página atual da URL
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    return render(request, 'resources/type_vehicle/manager_type_vehicle.html', {'page': page})

# Cadastrar

def register_customer(request):
    return render(request, 'resources/customer/register_customer.html')

def register_scheduling(request):
    if request.method == 'POST':
        try:
            # Carrega o corpo da requisição como JSON
            data = json.loads(request.body)

            start_data = data.get('start-data')
            end_data = data.get('end-data')

            if(start_data >= end_data):
                return JsonResponse({'success': False, 'message': f'A data de início do serviço não pode ser maior que a data final do serviço!'})

            agendamento = Agendamento.objects.using('mysql_db').create(
                datetime_inicio=start_data,
                datetime_fim=end_data,
                disponivel=True
            )

            # Verifique se o objeto foi criado com sucesso
            if not agendamento:
                return JsonResponse({'success': False, 'message': f'Falha ao tentar criar o agendamento - não foi possível criar objeto'})

            return JsonResponse({'success': True, 'message': f'Agendamento cadastrado com sucesso'})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Erro ao processar os dados.'})

        except IntegrityError as e:
            logger.error(repr(e))
            return JsonResponse({'success': False, 'message': f'Erro ao excluir o Cliente {customer_name} ({customer_id})\nPor favor, delete o(s) serviço(s) ou remova o cliente associado aos mesmos para continuar com a exclusão'})

        except Exception as e:
            logger.error(repr(e))
            return JsonResponse({'success': False, 'message': f'Erro crítico ao excluir o cliente {customer_name} ({customer_id})\nEntre em contato com o suporte'})

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

# Método POST para excluir cliente
def delete_customer(request):
    if request.method == 'POST':
        try:
            # Carrega o corpo da requisição como JSON
            data = json.loads(request.body)

            # Extrai o ID do cliente
            customer_id = data.get('id')

            # Tenta obter o cliente e excluir
            customer = Cliente.objects.get(id=customer_id)
            customer_name = customer.nome
            customer.delete()

            logger.info(f"cliente {customer_id} removido com sucesso")
            return JsonResponse({'success': True, 'message': f'Cliente {customer_name} ({customer_id}) excluído com sucesso.'})

        except Cliente.DoesNotExist:
            logger.error(repr(e))
            return JsonResponse({'success': False, 'message': f'Cliente {customer_name} ({customer_id}) não encontrado'})

        except IntegrityError as e:
            logger.error(repr(e))
            return JsonResponse({'success': False, 'message': f'Erro ao excluir o Cliente {customer_name} ({customer_id})\nPor favor, delete o(s) serviço(s) ou remova o cliente associado aos mesmos para continuar com a exclusão'})

        except Exception as e:
            logger.error(repr(e))
            return JsonResponse({'success': False, 'message': f'Erro crítico ao excluir o cliente {customer_name} ({customer_id})\nEntre em contato com o suporte'})

    return JsonResponse({'success': False, 'message': 'Method not allowed'})

# Método POST para excluir agendamento
def delete_scheduling(request):
    if request.method == 'POST':
        try:
            # Carrega o corpo da requisição como JSON
            data = json.loads(request.body)

            # Extrai o ID do cliente
            scheduling_id = data.get('id')

            # Tenta obter o cliente e excluir
            scheduling = Agendamento.objects.get(id=scheduling_id)
            scheduling.delete()

            logger.info(f"agendamento {scheduling_id} removido com sucesso")
            return JsonResponse({'success': True, 'message': f'Agendamento ({scheduling_id}) excluído com sucesso.'})

        except Agendamento.DoesNotExist:
            logger.error(repr(e))
            return JsonResponse({'success': False, 'message': f'Agendamento ({scheduling_id}) não encontrado'})

        except IntegrityError as e:
            logger.error(repr(e))
            return JsonResponse({'success': False, 'message': f'Erro ao excluir o Agendamento ({scheduling_id})\nPor favor, delete o(s) serviço(s) ou remova o agendamento associado aos mesmos para continuar com a exclusão'})

        except Exception as e:
            logger.error(repr(e))
            return JsonResponse({'success': False, 'message': f'Erro crítico ao excluir o agendamento ({scheduling_id})\nEntre em contato com o suporte'})

    return JsonResponse({'success': False, 'message': 'Method not allowed'})


# Método POST para excluir serviço
def delete_service(request):
    if request.method == 'POST':
        try:
            # Carrega o corpo da requisição como JSON
            data = json.loads(request.body)

            # Extrai o ID do cliente
            service_id = data.get('id')

            # Tenta obter o cliente e excluir
            service = Servico.objects.get(id=service_id)

            # Coloca o agendamento como disponível
            service.agendamento.disponivel = True
            service.agendamento.save()

            service.delete()

            logger.info(f"serviço {service_id} removido com sucesso")
            return JsonResponse({'success': True, 'message': f'Serviço ({service_id}) excluído com sucesso.'})

        except Servico.DoesNotExist:
            logger.error(repr(e))
            return JsonResponse({'success': False, 'message': f'Serviço ({service_id}) não encontrado'})

        except IntegrityError as e:
            logger.error(repr(e))
            return JsonResponse({'success': False, 'message': f'Erro ao excluir o Serviço ({service_id})'})

        except Exception as e:
            logger.error(repr(e))
            return JsonResponse({'success': False, 'message': f'Erro crítico ao excluir o serviço ({service_id})\nEntre em contato com o suporte'})

    return JsonResponse({'success': False, 'message': 'Method not allowed'})

# Método POST para excluir tipo serviço
def delete_type_service(request):
    if request.method == 'POST':
        try:
            # Carrega o corpo da requisição como JSON
            data = json.loads(request.body)

            # Extrai o ID do cliente
            type_service_id = data.get('id')

            # Tenta obter o cliente e excluir
            type_service = TipoServico.objects.get(id=type_service_id)

            type_service.delete()

            logger.info(f"tipo serviço {type_service_id} removido com sucesso")
            return JsonResponse({'success': True, 'message': f'Tipo Serviço ({type_service_id}) excluído com sucesso.'})

        except TipoServico.DoesNotExist:
            logger.error(repr(e))
            return JsonResponse({'success': False, 'message': f'Tipo Serviço ({type_service_id}) não encontrado'})

        except IntegrityError as e:
            logger.error(repr(e))
            return JsonResponse({'success': False, 'message': f'Erro ao excluir o Tipo Serviço ({type_service_id})\nPor favor, delete o(s) tipo serviço ou remova o serviço associado aos mesmos para continuar com a exclusão'})
        except Exception as e:
            logger.error(repr(e))
            return JsonResponse({'success': False, 'message': f'Erro crítico ao excluir o serviço ({type_service_id})\nEntre em contato com o suporte'})

    return JsonResponse({'success': False, 'message': 'Method not allowed'})

# Método POST para excluir tipo veiculo
def delete_type_vehicle(request):
    if request.method == 'POST':
        try:
            # Carrega o corpo da requisição como JSON
            data = json.loads(request.body)

            # Extrai o ID do cliente
            type_vehicle_id = data.get('id')

            # Tenta obter o cliente e excluir
            type_vehicle = TipoVeiculo.objects.get(id=type_vehicle_id)

            type_vehicle.delete()

            logger.info(f"tipo veiculo {type_vehicle_id} removido com sucesso")
            return JsonResponse({'success': True, 'message': f'Tipo Veiculo ({type_vehicle_id}) excluído com sucesso.'})

        except TipoVeiculo.DoesNotExist:
            logger.error(repr(e))
            return JsonResponse({'success': False, 'message': f'Tipo Veiculo ({type_vehicle_id}) não encontrado'})

        except IntegrityError as e:
            logger.error(repr(e))
            return JsonResponse({'success': False, 'message': f'Erro ao excluir o Tipo Veiculo ({type_vehicle_id})\nPor favor, delete o(s) tipo veiculo ou remova o serviço associado aos mesmos para continuar com a exclusão'})
        except Exception as e:
            logger.error(repr(e))
            return JsonResponse({'success': False, 'message': f'Erro crítico ao excluir o tipo veiculo ({type_vehicle_id})\nEntre em contato com o suporte'})

    return JsonResponse({'success': False, 'message': 'Method not allowed'})

# Business Intelligence (BI)

def bi_report(request):
    return render(request, 'resources/business_intelligence/bi_report.html')

def bi_analysis(request):
    return render(request, 'resources/business_intelligence/bi_analysis.html')

# Site Edit

def site_edit(request):
    return render(request, 'resources/site/site_edit.html')