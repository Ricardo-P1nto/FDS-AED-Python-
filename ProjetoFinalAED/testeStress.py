# testeStress.py
import random
import time
from algoritmos import PresencaBST, bubble_sort

def gerar_dados_teste(qtd):
    print(f"\n--- 🏁 CORRIDA DE ALGORITMOS: {qtd} Alunos ---")
    
    # 1. Gerar dados
    dados = []
    for _ in range(qtd):
        id_fake = random.randint(1000, 99999)
        dados.append((id_fake, f"Aluno_{id_fake}"))
    
    # 2. Teste Bubble Sort (O Lento)
    inicio = time.time()
    bubble_sort(dados)
    fim = time.time()
    tempo_bubble = fim - inicio
    print(f"🐢 Bubble Sort: {tempo_bubble:.5f} segundos")

    # 3. Teste BST (A Rápida)
    inicio = time.time()
    arvore = PresencaBST()
    for id_aluno, nome in dados:
        arvore.inserir(id_aluno, nome)
    arvore.obter_lista_ordenada()
    fim = time.time()
    tempo_bst = fim - inicio
    print(f"🐇 Tree Sort:   {tempo_bst:.5f} segundos")
    
    print("-" * 30)