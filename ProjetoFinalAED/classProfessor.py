import time
import csv
import testeStress
from fpdf import FPDF # Certifica-te que instalaste: pip install fpdf

class Professor:
    def __init__(self, nome, senha, id_prof):
        self.nome = nome
        self.senha = senha
        self.id = id_prof

    def exportar_csv(self, presencas, tempo_duracao):
        filename = "relatorio_aula.csv"
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["ID Aluno", "Nome", "Hora da Aula"])
                for aluno in presencas:
                    writer.writerow([aluno[0], aluno[1], time.strftime("%Y-%m-%d %H:%M")])
            print(f"✅ Relatório CSV exportado: {filename}")
        except Exception as e:
            print(f"Erro ao exportar CSV: {e}")

    def exportar_pdf(self, presencas, tempo_duracao):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        pdf.cell(200, 10, txt=f"Relatório de Aula - Prof. {self.nome}", ln=1, align='C')
        pdf.cell(200, 10, txt=f"Duração da Aula: {tempo_duracao:.2f} segundos", ln=1, align='C')
        pdf.ln(10)
        
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(40, 10, "ID Aluno", 1)
        pdf.cell(100, 10, "Nome Aluno", 1)
        pdf.ln()
        
        pdf.set_font("Arial", size=12)
        for aluno in presencas:
            pdf.cell(40, 10, str(aluno[0]), 1)
            pdf.cell(100, 10, str(aluno[1]), 1)
            pdf.ln()
            
        filename = "relatorio_aula.pdf"
        pdf.output(filename)
        print(f"✅ Relatório PDF exportado: {filename}")

    def menu_professor(self, estado_aula):
        while True:
            print(f"\n--- PAINEL PROFESSOR: {self.nome} ---")
            status = "ABERTA 🟢" if estado_aula['aberta'] else "FECHADA 🔴"
            print(f"Estado da Aula: {status}")
            print("1. Abrir Aula (Iniciar Cronómetro)")
            print("2. Fechar Aula e Exportar Relatório")
            print("3. Gerar Carga de Stress (Teste)")
            print("0. Logout")
            
            opcao = input("Escolha: ")

            if opcao == "1":
                if estado_aula['aberta']:
                    print("⚠️ A aula já está aberta!")
                else:
                    estado_aula['aberta'] = True
                    estado_aula['inicio'] = time.time()
                    estado_aula['presencas'] = [] # Limpa presenças anteriores
                    print("🔔 AULA ABERTA! Os alunos já podem marcar presença.")

            elif opcao == "2":
                if not estado_aula['aberta']:
                    print("⚠️ Não há nenhuma aula a decorrer para fechar.")
                else:
                    fim = time.time()
                    duracao = fim - estado_aula['inicio']
                    estado_aula['aberta'] = False
                    
                    print(f"\n🛑 Aula Fechada! Duração: {duracao:.2f} segundos.")
                    print(f"Total de presenças: {len(estado_aula['presencas'])}")
                    
                    resp = input("Deseja exportar relatório (PDF e CSV)? (s/n): ").lower()
                    if resp == 's':
                        self.exportar_csv(estado_aula['presencas'], duracao)
                        self.exportar_pdf(estado_aula['presencas'], duracao)

            elif opcao == "3":
                qtd = int(input("Quantos registos quer gerar? "))
                testeStress.gerar_dados_teste(qtd)

            elif opcao == "0":
                break
            else:
                print("Opção inválida.")