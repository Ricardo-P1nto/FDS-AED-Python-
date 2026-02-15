import testeStress

class Professor:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def abrir_aula():
        pass

    def fechar_aula():
        pass

    def exportar_relatorio():
        pass

    def menu_professor(self):
        senha = input("Senha de acesso: ")
        if senha != "admin123":
            print("Acesso Negado!")
            return

    while True:
        print("\n--- MODO PROFESSOR ---")
        print("1. Gerar Carga de Stress (Milhares de Registos)")
        
        testeStress.gerar_dados_teste(i)
        print("2. Ordenar e Analisar (BST vs QuickSort)")
        print("3. Exportar PDF/CSV")
        print("4. Abrir Aula")
        print("5. Sair")
        
        resposta: int = input("Escolha uma opção: ")

        if resposta == 1:
            i: int = int(input("Digite o número de registos a gerar: "))
            testeStress.gerar_dados_teste(i)

        elif resposta == 2:
            print("Ordenando e Analisando... (Funcionalidade em desenvolvimento)")

        elif resposta == 3:
            print("Exportando... (Funcionalidade em desenvolvimento)")

        elif resposta == 4:
            print("Aula Aberta! (Funcionalidade em desenvolvimento)")

        elif resposta == 5:
            break

        else:
            print("Opção inválida. Tente novamente.")

    
    
