from leitorDados import carregar_dados

class Aluno:
    alunos_db, profs_db = carregar_dados()

    def __init__(self, nome, idade, numero, password):
        self.nome = nome
        self.idade = idade
        self.numero = numero
        self.password = password

    def marcar_presenca():
        pass

    def menu_aluno(self, lista_presencas):
        print("\n--- REGISTO DE PRESENÇA ---")
        try:
            id_aluno = int(input("Número de Aluno: "))
            nome = input("Nome do Aluno: ")
            lista_presencas.append((id_aluno, nome))
            print("Presença registada!")
        except ValueError:
            print("Erro: O ID deve ser um número inteiro.")

    def login_aluno(self):
        num = int(input("Número de aluno: "))
        pw = input("Password: ")
        
        # Procura o aluno na "base de dados" carregada
        aluno_encontrado = next((a for a in Aluno.alunos_db if a.numero == num and a.password == pw), None)
        
        if aluno_encontrado:
            print(f"Bem-vindo, {aluno_encontrado.nome}!")
            # aluno_encontrado.marcar_presenca() -> Lógica de adicionar à lista da aula
        else:
            print("Credenciais inválidas.")
    