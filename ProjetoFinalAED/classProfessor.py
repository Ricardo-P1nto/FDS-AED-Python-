import time
import csv
import testeStress
from algoritmos import bubble_sort

# Se a biblioteca não estiver instalada, o programa não crasha ao iniciar
try:
    from fpdf import FPDF
    FPDF_DISPONIVEL = True
except ImportError:
    FPDF_DISPONIVEL = False
    print("⚠️  Aviso: biblioteca 'fpdf2' não instalada. Exportação PDF desativada.")
    print("    Para ativar, corre: pip install fpdf2")


class Professor:
    def __init__(self, nome, senha, id_prof):
        self.nome = nome
        self.senha = senha
        self.id = id_prof

    def exportar_csv(self, presencas, tempo_duracao):
        """Exporta a lista de presenças para um ficheiro CSV."""
        filename = "relatorio_aula.csv"
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # Cabeçalho da tabela
                writer.writerow(["ID Aluno", "Nome", "Hora da Aula", "Duração (s)"])
                for aluno in presencas:
                    writer.writerow([aluno[0], aluno[1], time.strftime("%Y-%m-%d %H:%M"), f"{tempo_duracao:.2f}"])
            print(f"✅ Relatório CSV exportado: {filename}")
        except Exception as e:
            print(f"❌ Erro ao exportar CSV: {e}")

    def exportar_pdf(self, presencas, tempo_duracao):
        """Exporta a lista de presenças para um ficheiro PDF."""
        if not FPDF_DISPONIVEL:
            print("❌ Exportação PDF não disponível. Instala a biblioteca fpdf2.")
            return

        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Título e cabeçalho do relatório
            pdf.cell(200, 10, txt=f"Relatorio de Aula - Prof. {self.nome}", ln=1, align='C')
            pdf.cell(200, 10, txt=f"Data: {time.strftime('%Y-%m-%d %H:%M')}", ln=1, align='C')
            pdf.cell(200, 10, txt=f"Duracao da Aula: {tempo_duracao:.2f} segundos", ln=1, align='C')
            pdf.ln(10)

            # Cabeçalho da tabela
            pdf.set_font("Arial", 'B', size=12)
            pdf.cell(40, 10, "ID Aluno", 1)
            pdf.cell(100, 10, "Nome Aluno", 1)
            pdf.ln()

            # Linhas da tabela com os dados de cada aluno
            pdf.set_font("Arial", size=12)
            for aluno in presencas:
                pdf.cell(40, 10, str(aluno[0]), 1)
                pdf.cell(100, 10, str(aluno[1]), 1)
                pdf.ln()

            filename = "relatorio_aula.pdf"
            pdf.output(filename)
            print(f"✅ Relatório PDF exportado: {filename}")

        except Exception as e:
            print(f"❌ Erro ao exportar PDF: {e}")

    def menu_professor(self, estado_aula):
        while True:
            print(f"\n--- PAINEL PROFESSOR: {self.nome} ---")
            status = "ABERTA 🟢" if estado_aula['aberta'] else "FECHADA 🔴"
            print(f"Estado da Aula: {status}")
            print("1. Abrir Aula (Iniciar Cronómetro)")
            print("2. Fechar Aula e Exportar Relatório")
            print("3. Gerar Carga de Stress (Teste de Algoritmos com limite de 99000 registos)")
            print("0. Logout")

            opcao = input("Escolha: ").strip()

            if opcao == "1":
                if estado_aula['aberta']:
                    print("⚠️  A aula já está aberta!")
                else:
                    estado_aula['aberta'] = True
                    estado_aula['inicio'] = time.time()
                    estado_aula['presencas'] = []
                    print("🔔 AULA ABERTA! Os alunos já podem marcar presença.")

            elif opcao == "2":
                if not estado_aula['aberta']:
                    print("⚠️  Não há nenhuma aula a decorrer para fechar.")
                else:
                    fim = time.time()
                    duracao = fim - estado_aula['inicio']
                    estado_aula['aberta'] = False

                    # Ordenar a lista de presenças com Bubble Sort antes de exportar
                    print("A ordenar lista de presenças com Bubble Sort...")
                    estado_aula['presencas'] = bubble_sort(estado_aula['presencas'])

                    print(f"\n🛑 Aula Fechada! Duração: {duracao:.2f} segundos.")
                    print(f"Total de presenças: {len(estado_aula['presencas'])}")

                    # Mostrar lista ordenada no terminal
                    if estado_aula['presencas']:
                        print("\n📋 Lista de Presenças (ordenada por ID):")
                        for aluno in estado_aula['presencas']:
                            print(f"  ID: {aluno[0]} | Nome: {aluno[1]}")

                    resp = input("\nDeseja exportar relatório (PDF e CSV)? (s/n): ").lower().strip()
                    if resp == 's':
                        self.exportar_csv(estado_aula['presencas'], duracao)
                        self.exportar_pdf(estado_aula['presencas'], duracao)

            elif opcao == "3":
                try:
                    qtd = int(input("Quantos registos quer gerar? "))
                    if qtd <= 0:
                        print("❌ O número de registos tem de ser positivo.")
                    else:
                        testeStress.gerar_dados_teste(qtd)
                except ValueError:
                    print("❌ Introduz um número inteiro válido.")

            elif opcao == "0":
                print(f"Logout efetuado. Até logo, Prof. {self.nome}!")
                break

            else:
                print("❌ Opção inválida.")
