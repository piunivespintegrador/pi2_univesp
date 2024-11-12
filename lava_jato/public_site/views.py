import re
import json
import logging

from datetime import date

from django.shortcuts import render
from django.http import JsonResponse

from private_site.models import Cliente, Agendamento, Servico, TipoServico, TipoVeiculo, FormaContato, ServicoFormaContato

logger = logging.getLogger('django')

# Principal

def home(request):
    return render(request, 'resources/home/public_home.html')

# Health

def health(request):
    return JsonResponse({'health': f'alive'})

# Registro

def public_register_service(request):
    if request.method == 'POST':
        try:

            # Padrão: "forma-contato-" seguido de um número
            forma_contato_pattern = r"^forma-contato-\d+$"

            # Carrega o corpo da requisição como JSON
            data = json.loads(request.body)

            agendamento_id = data.get('agendamento-id')
            tipo_servico_id = data.get('tipo-servico-id')
            tipo_veiculo_id = data.get('tipo-veiculo-id')
            forma_contato_ids = []

            for string in data:
                if re.match(forma_contato_pattern, string):
                    forma_contato_ids.append(data.get(string))

            logger.info('Validando agendamento')

            agendamento = Agendamento.objects.using('mysql_db').filter(
                id=agendamento_id,
                disponivel=True,
            ).first()

            if not agendamento:
                return JsonResponse({'success': False, 'message': f'Data de agendamento selecionado não encontrado ou não esta mais disponível'})

            logger.info('Validando tipo serviço')

            tipo_servico = TipoServico.objects.using('mysql_db').filter(
                id=tipo_servico_id,
            ).first()

            if not tipo_servico:
                return JsonResponse({'success': False, 'message': f'Tipo de Serviço não encontrado'})

            logger.info('Validando tipo veiculo')

            tipo_veiculo = TipoServico.objects.using('mysql_db').filter(
                id=tipo_veiculo_id,
            ).first()

            if not tipo_veiculo:
                return JsonResponse({'success': False, 'message': f'Tipo de Veículo não encontrado'})

            logger.info('Obtendo formas de contato')

            forma_contatos = FormaContato.objects.using('mysql_db').filter(id__in=forma_contato_ids)

            # Campos obrigatórios
            nome_cliente = data.get('nome-cliente')
            placa_carro = data.get('placa-carro')
            telefone_1 = data.get('telefone-principal')
            email_1 = data.get('email-principal')

            # Campos opcionais
            telefone_2 = data.get('telefone-secundario', None)
            email_2 = data.get('email-secundario', None)

            logger.info('Validando dados de cadastramento do cliente')

            if  not nome_cliente or \
                not placa_carro or \
                not telefone_1 or \
                not email_1:
                return JsonResponse({'success': False, 'message': f'Existe(m) campo(s) obrigatório(s) que não foram preenchido(s)'})

            logger.info('Verificando existencia do cliente')

            # Verificar se já existe um cliente com a placa
            cliente = Cliente.objects.using('mysql_db').filter(
                placa_carro=placa_carro
            ).first()

            # Se não existir, criamos o cliente
            if not cliente:
                logger.info('Criando cliente')
                cliente = Cliente.objects.using('mysql_db').create(
                    nome=nome_cliente,
                    placa_carro=placa_carro,
                    email_contato_1=email_1,
                    email_contato_2=email_2,
                    telefone_contato_1=telefone_1,
                    telefone_contato_2=telefone_2
                )

                if not cliente:
                    return JsonResponse({'success': False, 'message': f'Existe(m) campo(s) obrigatório(s) que não foram preenchido(s)'})
            else:
                logger.info('Cliente já existe, atualizando dados de cadastro')

                cliente.nome = nome_cliente
                cliente.email_contato_1 = email_1
                cliente.email_contato_2 = email_2
                cliente.telefone_contato_1 = telefone_1
                cliente.telefone_contato_2 = telefone_2

                cliente.save()

            # Criamos o serviço

            logger.info('Criando serviço')

            mensagem = data.get('mensagem', '')

            servico = Servico.objects.using('mysql_db').create(
                agendamento_id=agendamento.id,
                cliente_id=cliente.id,
                tipo_servico_id=tipo_servico.id,
                tipo_veiculo_id=tipo_veiculo.id,
                mensagem=mensagem,
                valor_servico=tipo_servico.valor_servico,
                status=0
            )

            if not servico:
                return JsonResponse({'success': False, 'message': f'Não foi possível criar o serviço\nPor favor, tente novamente ou entre em contato com o suporte'})

            # Criamos a formas de contato

            logger.info('Criando forma de contato')

            for forma_contato in forma_contatos:
                ServicoFormaContato.objects.using('mysql_db').create(
                    servico_id=servico.id,
                    forma_contato_id=forma_contato.id
                )

            # Vamos dar o agendamento como indisponível
            logger.info('Modificando disponibilidade do agendamento')

            agendamento.disponivel = False
            agendamento.save()

            return JsonResponse({'success': True, 'message': f'Agendamento do serviço realizado com sucesso\nLogo mais entraremos em contato'})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Erro ao processar os dados.'})

        except Exception as e:
            logger.error(repr(e))
            return JsonResponse({'success': False, 'message': f'Erro crítico ao tentar criar agendamento\nPor favor, entre em contato com o suporte'})

    today = date.today()

    tipos_veiculo = TipoVeiculo.objects.all()
    tipos_servico = TipoServico.objects.all()
    formas_contato = FormaContato.objects.all()

    agendamentos = Agendamento.objects.using('mysql_db').filter(
        disponivel=True,
        datetime_inicio__gte=today
    )

    data = {
        'tipos_veiculo' : tipos_veiculo,
        'tipos_servico' : tipos_servico,
        'formas_contato' : formas_contato,
        'agendamentos' : agendamentos
    }

    return render(request, 'resources/service/public_register_service.html', {'data': data})
