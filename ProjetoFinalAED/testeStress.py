import random
import time

def gerar_dados_teste(n_registos):
    print(f"--- Iniciando Simulação de Carga: {n_registos} registos ---")
    
    # 1. Registar o tempo de início (Alta precisão)
    inicio = time.perf_counter()
    
    dados = []
    for _ in range(n_registos):
        id_fake = random.randint(1000, 99999)
        nome_fake = f"Aluno_{id_fake}"
        dados.append((id_fake, nome_fake))
    
    # 2. Registar o tempo de fim
    fim = time.perf_counter()
    
    # 3. Calcular a diferença
    tempo_total = fim - inicio
    
    print(f"✅ Concluído!")
    print(f"⏱️ Tempo de execução: {tempo_total:.4f} segundos")
    print("-" * 40)
    
    return dados

# --- Exemplo de Uso para o Passo 3 do teu Projeto ---
# Podes testar o crescimento da complexidade aqui
n_testes = [1000, 10000, 100000]

for n in n_testes:
    gerar_dados_teste(n)