# testeStress.py
import random
import time
from algoritmos import PresencaBST, bubble_sort


def gerar_dados_teste(qtd):
    """
    Gera 'qtd' registos aleatórios únicos e compara o desempenho do
    Bubble Sort (O(n²)) com o Tree Sort via BST (O(n log n) em média).
    
    CORREÇÃO: uso de random.sample() para garantir IDs únicos,
    evitando que a BST ignore duplicatas e torne o teste impreciso.
    """
    print(f"\n--- 🏁 CORRIDA DE ALGORITMOS: {qtd} Alunos ---")

    # Verificar se é possível gerar IDs únicos suficientes
    universo = 99999 - 1000 + 1  # Range disponível: 1000 a 99999
    if qtd > universo:
        print(f"⚠️  Máximo de IDs únicos disponíveis: {universo}. A ajustar para {universo}.")
        qtd = universo

    # CORREÇÃO: random.sample garante que não há IDs repetidos
    # Isto é importante para a BST, que ignora duplicatas silenciosamente
    ids_unicos = random.sample(range(1000, 100000), qtd)
    dados = [(id_fake, f"Aluno_{id_fake}") for id_fake in ids_unicos]

    # --- Teste Bubble Sort: O(n²) ---
    # Faz uma cópia para não alterar os dados originais
    dados_para_bubble = dados.copy()
    inicio = time.time()
    bubble_sort(dados_para_bubble)
    fim = time.time()
    tempo_bubble = fim - inicio
    print(f"🐢 Bubble Sort [O(n²)]:   {tempo_bubble:.5f} segundos")

    # --- Teste Tree Sort via BST: O(n log n) em média ---
    inicio = time.time()
    arvore = PresencaBST()
    for id_aluno, nome in dados:
        arvore.inserir(id_aluno, nome)
    arvore.obter_lista_ordenada()
    fim = time.time()
    tempo_bst = fim - inicio
    print(f"🐇 Tree Sort  [O(n log n)]: {tempo_bst:.5f} segundos")

    # Conclusão comparativa
    print("-" * 40)
    if tempo_bubble > 0 and tempo_bst > 0:
        if tempo_bst < tempo_bubble:
            fator = tempo_bubble / tempo_bst
            print(f"✅ Tree Sort foi {fator:.1f}x mais rápido que Bubble Sort.")
        else:
            print("ℹ️  Para esta dimensão, os tempos são semelhantes.")
    print("-" * 40)
