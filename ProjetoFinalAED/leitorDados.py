import json
from classProfessor import Professor
from classAluno import Aluno

def carregar_dados():
    try:
        with open('database.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
            
            # Converter dicionários JSON em objetos Aluno
            lista_alunos = [
                Aluno(a['nome'], a['idade'], a['numero'], a['password']) 
                for a in dados['alunos']
            ]
            
            # Converter dicionários JSON em objetos Professor (Agora com ID)
            lista_profs = [
                Professor(p['nome'], p['senha'], p.get('id', 0)) # Usa 0 se não tiver ID
                for p in dados['professores']
            ]
            
            return lista_alunos, lista_profs
    except FileNotFoundError:
        print("Erro: Ficheiro database.json não encontrado.")
        return [], []

def guardar_dados(alunos, professores):
    dados = {
        "alunos": [vars(a) for a in alunos], # vars() transforma o objeto em dicionário
        "professores": [vars(p) for p in professores]
    }
    with open('database.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)