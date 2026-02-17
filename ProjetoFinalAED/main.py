import leitorDados

# --- ESTADO GLOBAL DA AULA ---
# Dicionário partilhado entre Professor e Aluno para manter o estado da aula
estado_aula = {
    'aberta': False,
    'inicio': 0.0,
    'presencas': []  # Lista de tuplos (numero, nome)
}


def autenticar_usuario(tipo, db_alunos, db_profs):
    """
    Função genérica de login.
    Recebe o tipo ('Aluno' ou 'Professor') e as listas da base de dados.
    Devolve o objeto autenticado ou None se as credenciais forem inválidas.
    """
    try:
        id_input = int(input(f"Digite o ID/Número de {tipo}: "))
        senha_input = input("Digite a Senha: ")
    except ValueError:
        print("❌ Erro: O ID/Número deve ser numérico.")
        return None

    if tipo == "Aluno":
        for aluno in db_alunos:
            # Compara numero (int) e password (ambos string após sanitização)
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
    # Carregar dados uma única vez ao iniciar o programa
    lista_alunos, lista_profs = leitorDados.carregar_dados()

    if not lista_alunos and not lista_profs:
        print("❌ Não foi possível carregar dados. Verifica o ficheiro database.json.")
        return

    print("✅ Sistema iniciado com sucesso!")

    while True:
        print("\n=== SISTEMA DE GESTÃO DE AULAS ===")
        print("1. Login Aluno")
        print("2. Login Professor")
        print("0. Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            aluno_logado = autenticar_usuario("Aluno", lista_alunos, lista_profs)
            if aluno_logado:
                aluno_logado.menu_aluno(estado_aula)

        elif opcao == "2":
            prof_logado = autenticar_usuario("Professor", lista_alunos, lista_profs)
            if prof_logado:
                prof_logado.menu_professor(estado_aula)

        elif opcao == "0":
            # CORREÇÃO: guardar dados ao sair para persistir qualquer alteração feita
            leitorDados.guardar_dados(lista_alunos, lista_profs)
            print("💾 Dados guardados. A sair do sistema...")
            break

        else:
            print("❌ Opção inválida. Escolhe 0, 1 ou 2.")


if __name__ == "__main__":
    main()
