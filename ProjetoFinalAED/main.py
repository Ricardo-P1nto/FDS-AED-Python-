import classProfessor
import classAluno

presencas_aula = []
while True:
    print("\n=== SISTEMA DE PRESENÇAS ===")
    print("1. Sou Aluno")
    print("2. Sou Professor")
    print("0. Sair")
    opcao = input("Escolha: ")
    
    if opcao == "1": classAluno.menu_aluno(presencas_aula)
    elif opcao == "2": classProfessor.menu_professor()
    elif opcao == "0": break

    