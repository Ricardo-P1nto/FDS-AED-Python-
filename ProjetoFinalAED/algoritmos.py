
# --- ALGORITMO A: Bubble Sort (O mais simples de explicar) ---
def bubble_sort(lista):
    # Faz uma cópia para não estragar a lista original
    lista_ordenada = lista.copy()
    n = len(lista_ordenada)
    
    # Percorre a lista toda várias vezes
    for i in range(n):
        for j in range(0, n - i - 1):
            # Se o ID do aluno atual for maior que o do vizinho, troca
            if lista_ordenada[j][0] > lista_ordenada[j + 1][0]:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
                
    return lista_ordenada

# --- ALGORITMO B: BST (Árvore Binária) ---
class Node:
    def __init__(self, id_aluno, nome):
        self.id = id_aluno
        self.nome = nome
        self.left = None
        self.right = None

class PresencaBST:
    def __init__(self):
        self.root = None

    def inserir(self, id_aluno, nome):
        if self.root is None:
            self.root = Node(id_aluno, nome)
        else:
            self._inserir_recursivo(self.root, id_aluno, nome)

    def _inserir_recursivo(self, node, id_aluno, nome):
        if id_aluno < node.id:
            if node.left is None:
                node.left = Node(id_aluno, nome)
            else:
                self._inserir_recursivo(node.left, id_aluno, nome)
        elif id_aluno > node.id:
            if node.right is None:
                node.right = Node(id_aluno, nome)
            else:
                self._inserir_recursivo(node.right, id_aluno, nome)

    def obter_lista_ordenada(self):
        lista = []
        self._in_order(self.root, lista)
        return lista

    def _in_order(self, node, lista):
        if node:
            self._in_order(node.left, lista)
            lista.append((node.id, node.nome))
            self._in_order(node.right, lista)