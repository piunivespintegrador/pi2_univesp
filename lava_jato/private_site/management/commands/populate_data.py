from django.core.management.base import BaseCommand

import sys
import os
import random

from faker import Faker
from datetime import timedelta
from django.utils import timezone

# Adiciona o caminho do diretório pai ao sistema de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from private_site.models import Cliente, FormaContato, TipoVeiculo, TipoServico, Agendamento, Servico, ServicoFormaContato

fake = Faker()

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados fake para teste'

    def handle(self, *args, **kwargs):
        self.create_forma_contato()
        self.create_tipo_veiculo()
        self.create_tipo_servico()
        self.create_clientes()
        self.create_agendamentos()
        self.create_servicos()
        self.stdout.write(self.style.SUCCESS('Dados fake gerados com sucesso!'))

    def create_forma_contato(self):
        formas = ['Email', 'Telefone', 'WhatsApp']

        self.stdout.write(self.style.NOTICE(f"Criando forma contato"))
        for forma in formas:
            forma_contato = FormaContato.objects.using('mysql_db').create(forma_nome=forma)
            self.stdout.write(f"\t{forma_contato}")

    def create_tipo_veiculo(self):
        veiculos = ['Carro', 'Moto', 'Caminhão']

        self.stdout.write(self.style.NOTICE(f"Criando tipo veiculo"))
        for veiculo in veiculos:
            tipo_veiculo = TipoVeiculo.objects.using('mysql_db').create(nome_veiculo=veiculo)
            self.stdout.write(f"\t{tipo_veiculo}")

    def create_tipo_servico(self):
        servicos = [
            {'tipo_servico': 'Lavagem Completa', 'valor_servico': 50.00},
            {'tipo_servico': 'Troca de Óleo', 'valor_servico': 120.00},
            {'tipo_servico': 'Polimento', 'valor_servico': 200.00},
        ]

        self.stdout.write(self.style.NOTICE(f"Criando tipo serviço"))
        for servico in servicos:
            tipo_servico = TipoServico.objects.using('mysql_db').create(**servico)
            self.stdout.write(f"\t{tipo_servico}")

    def create_clientes(self, n=10):
        self.stdout.write(self.style.NOTICE(f"Criando clientes"))
        for _ in range(n):
            cliente = Cliente.objects.using('mysql_db').create(
                nome=fake.name(),
                email_contato_1=fake.email(),
                email_contato_2=fake.email() if random.choice([True, False]) else None,
                telefone_contato_1=fake.phone_number()[:20],
                telefone_contato_2=fake.phone_number()[:20] if random.choice([True, False]) else None
            )
            self.stdout.write(f"\t{cliente}")

    def create_agendamentos(self, n=10):
        self.stdout.write(self.style.NOTICE(f"Criando agendamentos"))
        for _ in range(n):
            datetime_inicio = fake.date_time_this_year()
            # corrigindo o fuso horário
            datetime_inicio = timezone.make_aware(datetime_inicio)
            datetime_fim = datetime_inicio + timedelta(minutes=random.randint(30, 60))
            agendamento = Agendamento.objects.using('mysql_db').create(
                datetime_inicio=datetime_inicio,
                datetime_fim=datetime_fim,
                disponivel=random.choice([True, False])
            )
            self.stdout.write(f"\t{agendamento}")

    def create_servicos(self, n=10):
        clientes = list(Cliente.objects.using('mysql_db').values_list('id', flat=True))
        tipos_servico = list(TipoServico.objects.using('mysql_db').values_list('id', flat=True))
        tipos_veiculo = list(TipoVeiculo.objects.using('mysql_db').values_list('id', flat=True))
        formas_contato = list(FormaContato.objects.using('mysql_db').values_list('id', flat=True))
        agendamentos = list(Agendamento.objects.using('mysql_db').values_list('id', flat=True))


        self.stdout.write(f"\t{random.choice(agendamentos)}")


        self.stdout.write(self.style.NOTICE(f"Criando serviços"))
        for _ in range(n):
            servico = Servico.objects.using('mysql_db').create(
                agendamento_id=random.choice(agendamentos),
                cliente_id=random.choice(clientes),
                tipo_servico_id=random.choice(tipos_servico),
                tipo_veiculo_id=random.choice(tipos_veiculo),
                mensagem=fake.text(),
                valor_servico=random.uniform(50.00, 500.00)
            )
            self.stdout.write(f"\t{servico}")

            self.stdout.write(self.style.NOTICE(f"\t * Criando serviço forma contato para o servico {servico.id}"))
            for _ in range(random.randint(1, 2)):  # associa 1 ou 2 formas de contato ao serviço
                servico_forma_contato = ServicoFormaContato.objects.using('mysql_db').create(
                    servico_id=servico.id,
                    forma_contato_id=random.choice(formas_contato)
                )
                self.stdout.write(f"\t\t{servico_forma_contato}")