import leitorDados

# --- ESTADO GLOBAL DA AULA ---
# Dicionário que será partilhado entre Professor e Aluno para manter o estado
estado_aula = {
    'aberta': False,
    'inicio': 0.0,
    'presencas': [] # Lista de tuplos (id, nome)
}

def autenticar_usuario(tipo, db_alunos, db_profs):
    """Função genérica para login"""
    try:
        id_input = int(input(f"Digite o ID/Número de {tipo}: "))
        senha_input = input("Digite a Senha: ")
    except ValueError:
        print("Erro: O ID deve ser numérico.")
        return None

    if tipo == "Aluno":
        for aluno in db_alunos:
            if aluno.numero == id_input and aluno.password == senha_input:
                return aluno
    elif tipo == "Professor":
        for prof in db_profs:
            if prof.id == id_input and prof.senha == senha_input:
                return prof
    
    print("❌ Credenciais Inválidas!")
    return None

# --- LOOP PRINCIPAL ---
def main():
    # Carregar dados uma única vez ao iniciar
    lista_alunos, lista_profs = leitorDados.carregar_dados()
    
    while True:
        print("\n=== SISTEMA DE GESTÃO DE AULAS ===")
        print("1. Login Aluno")
        print("2. Login Professor")
        print("0. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            aluno_logado = autenticar_usuario("Aluno", lista_alunos, lista_profs)
            if aluno_logado:
                # Passamos o estado da aula para o aluno poder marcar presença
                aluno_logado.menu_aluno(estado_aula)

        elif opcao == "2":
            prof_logado = autenticar_usuario("Professor", lista_alunos, lista_profs)
            if prof_logado:
                # Passamos o estado da aula para o professor gerir
                prof_logado.menu_professor(estado_aula)

        elif opcao == "0":
            print("A sair do sistema...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()