import json
from classProfessor import Professor
from classAluno import Aluno

FICHEIRO_DB = 'database.json'

def carregar_dados():
    """Lê o ficheiro JSON e converte os dados em objetos."""
    try:
        with open(FICHEIRO_DB, 'r', encoding='utf-8') as f:
            dados = json.load(f)

            # Converter dicionários JSON em objetos Aluno
            lista_alunos = []
            for a in dados.get('alunos', []):
                try:
                    aluno = Aluno(
                        str(a['nome']),
                        int(a['idade']),
                        int(a['numero']),
                        str(a['password'])
                    )
                    lista_alunos.append(aluno)
                except (ValueError, KeyError) as e:
                    print(f"⚠️  Aluno ignorado por dados inválidos: {e}")

            # Converter dicionários JSON em objetos Professor
            lista_profs = []
            for p in dados.get('professores', []):
                try:
                    prof = Professor(
                        str(p['nome']),
                        str(p['senha']),
                        int(p.get('id', 0))
                    )
                    lista_profs.append(prof)
                except (ValueError, KeyError) as e:
                    print(f"⚠️  Professor ignorado por dados inválidos: {e}")

            return lista_alunos, lista_profs

    except FileNotFoundError:
        print(f"❌ Erro: Ficheiro '{FICHEIRO_DB}' não encontrado.")
        return [], []
    except json.JSONDecodeError:
        print(f"❌ Erro: O ficheiro '{FICHEIRO_DB}' está corrompido ou tem formato inválido.")
        return [], []


def guardar_dados(alunos, professores):
    dados = {
        "alunos": [
            {
                "nome": a.nome,
                "idade": a.idade,
                "numero": a.numero,
                "password": a.password
            }
            for a in alunos
        ],
        "professores": [
            {
                "nome": p.nome,
                "senha": p.senha,
                "id": p.id
            }
            for p in professores
        ]
    }
    try:
        with open(FICHEIRO_DB, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"❌ Erro ao guardar dados: {e}")
