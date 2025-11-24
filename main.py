'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
#exercicio 1
print("Exercício 1\n")

class Produto:
    
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
        


    def detalhes(self):
        print("O produto", self.nome, "custa", self.preco, "$ e temos", self.quantidade, "em Stock")
        

P1 = Produto("Laptop", 1500, 200)

P2 = Produto("Desktop", 2000, 100)

P1.detalhes()
P2.detalhes()

# Exercicio 2
print("\nExercício 2\n")

class Funcionario:
    
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def mostrar(self):
        print("sou o", self.nome, "o meu salário é de", self.salario)
        
class Gerente(Funcionario):
    
    def __init__(self, nome, salario, bonus):
    
        super().__init__(nome, salario)
        
        self.bonus = bonus

    def mostrar(self):
        print("sou o", self.nome, "o meu salário é de", self.salario, "e tambem tenho um bonus de ", self.bonus)

G1 = Gerente ("Rafael", 3000, 200)
F1 = Funcionario ("Miguel", 1000)

F1.mostrar()
G1.mostrar()


#Exercicio 3
print("\nExercicio 3\n")

class Veiculo:
    
    def deslocar(self):
        print("Movimento")
        
class Carro (Veiculo):
    
    def deslocar(self):
        print("Anda na Estrada")
        
class Barco (Veiculo):
    
    def deslocar(self):
        print("Navega na Agua")
        
    
garagem = [Carro(), Barco()]
for v in garagem:
    v.deslocar()
