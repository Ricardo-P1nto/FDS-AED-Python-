class Aluno:
    def __init__(self, nome, idade, numero, password):
        # Validação de tipos na criação do objeto
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Nome do aluno tem de ser uma string não vazia.")
        if not isinstance(numero, int) or numero <= 0:
            raise ValueError("Número do aluno tem de ser um inteiro positivo.")
        if not isinstance(idade, int) or idade <= 0:
            raise ValueError("Idade tem de ser um inteiro positivo.")

        self.nome = nome
        self.idade = idade
        self.numero = numero
        self.password = str(password)  # Garante que a password é sempre string

    def menu_aluno(self, estado_aula):
        while True:
            print(f"\n--- PAINEL ALUNO: {self.nome} ---")
            print("1. Marcar Presença")
            print("0. Sair")

            opcao = input("Escolha: ").strip()

            if opcao == "1":
                if estado_aula['aberta']:
                    # Verifica se o aluno já marcou presença nesta aula
                    ja_marcou = any(p[0] == self.numero for p in estado_aula['presencas'])

                    if not ja_marcou:
                        estado_aula['presencas'].append((self.numero, self.nome))
                        print(f"✅ Presença registada com sucesso para {self.nome}!")
                    else:
                        print("⚠️ Já tens a presença marcada nesta aula.")
                else:
                    print("❌ Não existe nenhuma aula a decorrer no momento.")

            elif opcao == "0":
                print(f"Até logo, {self.nome}!")
                break  # Sai do loop e regressa ao menu principal

            else:
                print("❌ Opção inválida. Escolhe 1 ou 0.")
