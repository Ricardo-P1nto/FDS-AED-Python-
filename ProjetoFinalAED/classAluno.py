class Aluno:
    def __init__(self, nome, idade, numero, password):
        self.nome = nome
        self.idade = idade
        self.numero = numero
        self.password = password

    def menu_aluno(self, estado_aula):
        print(f"\n--- PAINEL ALUNO: {self.nome} ---")
        print("1. Marcar Presença")
        print("0. Sair")
        
        opcao = input("Escolha: ")
        
        if opcao == "1":
            if estado_aula['aberta']:
                # Verifica se já não marcou
                ja_marcou = False
                for p in estado_aula['presencas']:
                    if p[0] == self.numero:
                        ja_marcou = True
                        break
                
                if not ja_marcou:
                    estado_aula['presencas'].append((self.numero, self.nome))
                    print(f"✅ Presença registada com sucesso para {self.nome}!")
                else:
                    print("⚠️ Já tens a presença marcada nesta aula.")
            else:
                print("❌ Não existe nenhuma aula a decorrer no momento.")
        elif opcao == "0":
            return