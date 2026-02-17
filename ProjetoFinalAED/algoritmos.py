# algoritmos.py
# Implementação dos dois algoritmos de ordenação exigidos pelo enunciado.

# --- ALGORITMO A: Bubble Sort ---
# Complexidade Temporal:
#   - Melhor caso:  O(n)   — lista já ordenada (com otimização de flag)
#   - Caso médio:   O(n²)
#   - Pior caso:    O(n²)  — lista em ordem inversa
# Complexidade Espacial: O(1) — ordenação in-place (aqui usamos cópia: O(n))

def bubble_sort(lista):
    """
    Ordena uma lista de tuplos (id, nome) pelo ID (primeiro elemento).
    Percorre a lista repetidamente, comparando pares adjacentes e trocando-os
    se estiverem fora de ordem. A cada passagem, o maior elemento 'borbulha'
    para o final.
    Faz uma cópia para não modificar a lista original.
    """
    lista_ordenada = lista.copy()
    n = len(lista_ordenada)

    for i in range(n):
        trocou = False  # Otimização: se não houver trocas, a lista já está ordenada
        for j in range(0, n - i - 1):
            # Se o ID do elemento atual for maior que o do vizinho à direita, troca
            if lista_ordenada[j][0] > lista_ordenada[j + 1][0]:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
                trocou = True
        # Otimização: termina cedo se a lista já ficou ordenada
        if not trocou:
            break

    return lista_ordenada


# --- ALGORITMO B: Tree Sort via Árvore Binária de Busca (BST) ---
# Complexidade de Inserção (por elemento):
#   - Média: O(log n) — árvore balanceada
#   - Pior caso: O(n)  — árvore desbalanceada (inserção de dados já ordenados)
# Complexidade do Percurso In-Order: O(n)
# Complexidade Total (n inserções + percurso): O(n log n) em média

class Node:
    """Representa um nó da árvore binária, com um ID, um nome, e
    referências para os filhos esquerdo e direito."""
    def __init__(self, id_aluno, nome):
        self.id = id_aluno
        self.nome = nome
        self.left = None   # Filho esquerdo: IDs menores
        self.right = None  # Filho direito: IDs maiores


class PresencaBST:
    """
    Árvore Binária de Busca (BST) para armazenar e ordenar presenças.
    A propriedade fundamental da BST garante que:
      - Todos os nós à esquerda têm ID menor que o nó pai.
      - Todos os nós à direita têm ID maior que o nó pai.
    O percurso in-order (esquerda → raiz → direita) devolve os elementos
    em ordem crescente de ID, sem necessidade de um algoritmo de ordenação separado.
    """
    def __init__(self):
        self.root = None  # A árvore começa vazia

    def inserir(self, id_aluno, nome):
        """Insere um novo aluno na posição correta da árvore."""
        if self.root is None:
            self.root = Node(id_aluno, nome)
        else:
            self._inserir_recursivo(self.root, id_aluno, nome)

    def _inserir_recursivo(self, node, id_aluno, nome):
        """
        Navega recursivamente pela árvore até encontrar a posição correta.
        IDs iguais são ignorados (sem duplicatas na BST).
        """
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
        # Se id_aluno == node.id, ignora (sem duplicatas)

    def obter_lista_ordenada(self):
        """Devolve todos os elementos da árvore ordenados por ID (percurso in-order)."""
        lista = []
        self._in_order(self.root, lista)
        return lista

    def _in_order(self, node, lista):
        """
        Percurso in-order: visita primeiro o filho esquerdo (menor),
        depois o nó atual, depois o filho direito (maior).
        Resultado: lista ordenada de forma crescente.
        """
        if node:
            self._in_order(node.left, lista)
            lista.append((node.id, node.nome))
            self._in_order(node.right, lista)
