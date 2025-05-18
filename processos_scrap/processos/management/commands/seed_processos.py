import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from processos.models import Advogado, Parte, Processo
from faker import Faker

fake = Faker('pt_BR')

class Command(BaseCommand):
    help = 'Popula o banco de dados com processos aleatórios'

    def handle(self, *args, **kwargs):
        self.stdout.write('Criando dados de exemplo...')

        # Criar advogados
        advogados = []
        for _ in range(10):
            nome = fake.name()
            advogado = Advogado.objects.create(nome=nome)
            advogados.append(advogado)

        # Criar partes
        partes = []
        for _ in range(20):
            nome = fake.name()
            parte = Parte.objects.create(nome=nome)
            partes.append(parte)

        # Criar processos
        for _ in range(50):
            numero = fake.bothify(text='########-##.####.#.##.####')
            vara = random.choice([
                "5ª Vara Criminal da Capital", 
                "1ª Vara da Comarca de Arapiraca", 
                "2ª Vara de Família de Maceió"
            ])
            comarca = random.choice(["Maceió", "Arapiraca", "Palmeira dos Índios"])
            tipo = random.choice([
                "Ação Penal - Procedimento Ordinário",
                "Cumprimento de sentença",
                "Ação Penal de Competência do Júri"
            ])
            data_recebimento = fake.date_between(start_date='-10y', end_date='today')
            advogado = random.choice(advogados)
            parte = random.choice(partes)

            Processo.objects.create(
                numero=numero,
                vara=vara,
                comarca=comarca,
                tipo=tipo,
                data_recebimento=data_recebimento,
                advogado=advogado,
                parte=parte
            )

        self.stdout.write(self.style.SUCCESS('Dados inseridos com sucesso!'))
