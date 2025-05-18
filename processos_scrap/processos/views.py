from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Processo
from django.shortcuts import get_object_or_404

def lista_processos(request):
    processos_list = Processo.objects.select_related('advogado', 'parte').order_by('-data_recebimento')
    paginator = Paginator(processos_list, 5)  # 5 processos por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'processos/processos_list.html', {'page_obj': page_obj})

def detalhe_processo(request, processo_id):
    processo = get_object_or_404(Processo.objects.select_related('advogado', 'parte'), pk=processo_id)
    # Se tiver relações com outras tabelas (movimentações, partes, etc), pode buscar aqui também
    
    # Exemplo: se houver um relacionamento de movimentações (processo.movimentacao_set)

    context = {
        'processo': processo,
    }
    return render(request, 'processos/processo_detalhe.html', context)
