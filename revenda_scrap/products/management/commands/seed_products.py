from django.core.management.base import BaseCommand
from products.models import Product
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Popula o banco com produtos de exemplo'

    def handle(self, *args, **kwargs):
        faker = Faker('pt_BR')
        categorias = ['Antiguidades', 'Eletrônicos', 'Roupas', 'Livros', 'Jogos', 'Casa', 'Esportes', 'Colecionáveis']
        base_image_url = 'https://picsum.photos/seed/{}/300/200'

        estados = ['Alagoas', 'Bahia', 'Pernambuco', 'Paraíba']
        cidades_por_estado = {
            'Alagoas': ['Maceió', 'Arapiraca', 'Palmeira dos Índios'],
            'Bahia': ['Salvador', 'Feira de Santana', 'Ilhéus'],
            'Pernambuco': ['Recife', 'Olinda', 'Caruaru'],
            'Paraíba': ['João Pessoa', 'Campina Grande', 'Santa Rita']
        }
        bairros_por_cidade = {
            'Maceió': ['Santos Dumont', 'Ponta Verde', 'Jatiúca'],
            'Arapiraca': ['Cacimbinhas', 'Centro', 'Brasília'],
            'Palmeira dos Índios': ['Centro', 'Santa Cruz', 'Benedito Bentes'],
            'Salvador': ['Barra', 'Ondina', 'Rio Vermelho'],
            'Feira de Santana': ['Centro', 'Tomba', 'Caseb'],
            'Ilhéus': ['Pontal', 'Olivença', 'Malhado'],
            'Recife': ['Boa Viagem', 'Aflitos', 'Casa Forte'],
            'Olinda': ['Bairro Novo', 'Peixinhos', 'Morro do Ceu'],
            'Caruaru': ['Centro', 'Vassoural', 'Boa Vista'],
            'João Pessoa': ['Tambau', 'Manaíra', 'Cabo Branco'],
            'Campina Grande': ['Centro', 'Bodocongó', 'Nova Brasília'],
            'Santa Rita': ['Centro', 'Bairro das Indústrias', 'Paratibe'],
        }

        for i in range(30):
            seed = faker.uuid4()
            estado = random.choice(estados)
            cidade = random.choice(cidades_por_estado[estado])
            bairro = random.choice(bairros_por_cidade.get(cidade, ['Centro']))
            categoria = random.choice(categorias)

            Product.objects.create(
                title=faker.sentence(nb_words=3),
                description=faker.text(max_nb_chars=200),
                price=round(random.uniform(10, 1000), 2),
                image_url=base_image_url.format(seed),
                estado_1=estado,
                estado_2=estado,
                categoria=categoria,
                cidade=cidade,
                bairro=bairro,
                pay_online=random.choice([True, False]),
                installment_available=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS('30 produtos criados com estado, cidade, bairro e categoria com lógica!'))
