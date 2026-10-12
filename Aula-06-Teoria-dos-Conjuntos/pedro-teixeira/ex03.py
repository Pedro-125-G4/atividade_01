# ============================================================
# ATIVIDADE DE FIXAÇÃO EXTRACLASSE - AULA 06
# Exercício 3 - Como o CPython trata colisões de hash no set
# Pedro Fonseca Teixeira
# ============================================================

# RESPOSTA TEÓRICA
#
# 1) Estrutura interna
#    No CPython, um set é uma TABELA HASH: um vetor de "slots" (entradas).
#    Cada slot guarda o elemento e o hash dele. A tabela sempre tem um
#    tamanho que é potência de 2 (começa com 8 slots).
#
# 2) Onde o elemento vai parar
#    Ao inserir ou buscar x, o Python calcula hash(x) e usa os bits mais
#    baixos dele como índice:  indice = hash(x) & (tamanho - 1)
#
# 3) Colisão
#    Colisão acontece quando dois elementos diferentes caem no mesmo slot.
#    O CPython NÃO usa listas encadeadas; ele usa ENDEREÇAMENTO ABERTO:
#    procura outro slot livre dentro da própria tabela.
#      - Primeiro faz uma SONDAGEM LINEAR curta (olha alguns slots vizinhos,
#        até 9 seguidos), o que aproveita bem o cache da CPU.
#      - Se continuar ocupado, usa uma SONDAGEM PSEUDOALEATÓRIA:
#            perturb >>= 5
#            indice = (indice * 5 + 1 + perturb) & (tamanho - 1)
#        O "perturb" começa com o hash completo, então os bits altos do
#        hash também passam a influenciar o caminho, espalhando os elementos.
#    Na busca o caminho é o mesmo: para cada slot visitado o Python compara
#    primeiro o hash (rápido) e só se for igual compara com ==. Se achar um
#    slot vazio, sabe que o elemento não está no conjunto.
#
# 4) Remoção
#    Ao remover, o slot vira uma marca "dummy" (lápide) em vez de vazio,
#    para não quebrar o caminho de sondagem dos outros elementos.
#
# 5) Por que a busca é O(1) em média
#    - Calcular o hash e o índice custa tempo constante.
#    - O set é redimensionado (cresce) quando passa de ~60% de ocupação
#      (fator de carga 3/5). Com sempre bastante espaço livre, o número
#      médio de slots visitados até achar o elemento (ou um vazio) é
#      pequeno e NÃO depende de quantos elementos existem.
#    - Ou seja, em média são poucas comparações: O(1).
#    - No PIOR caso (muitos elementos com o mesmo hash) todos colidem e a
#      busca vira O(n). Por isso é O(1) MÉDIO, e não garantido.


# DEMONSTRAÇÃO PRÁTICA
import time


class ChaveComHashFixo:
    # Todos os objetos desta classe têm o MESMO hash -> colisão sempre

    def __init__(self, valor):
        self.valor = valor

    def __hash__(self):
        return 42

    def __eq__(self, outro):
        return isinstance(outro, ChaveComHashFixo) and self.valor == outro.valor


def medir_tempo_de_busca(conjunto, elemento, repeticoes=200):
    inicio = time.perf_counter()
    for _ in range(repeticoes):
        elemento in conjunto
    return time.perf_counter() - inicio


quantidade_elementos = 2000

conjunto_hash_bom = set(range(quantidade_elementos))
conjunto_com_colisoes = {ChaveComHashFixo(valor) for valor in range(quantidade_elementos)}

tempo_hash_bom = medir_tempo_de_busca(conjunto_hash_bom, quantidade_elementos - 1)
tempo_com_colisoes = medir_tempo_de_busca(
    conjunto_com_colisoes, ChaveComHashFixo(quantidade_elementos - 1)
)

print(f"Busca com hashes bem distribuídos: {tempo_hash_bom:.6f} s (O(1) médio)")
print(f"Busca com todos os hashes iguais:  {tempo_com_colisoes:.6f} s (pior caso O(n))")


# ============================================================
# BATERIA DE TESTES / ASSERTS
# ============================================================

# Mesmo com colisões o set continua correto, só fica mais lento
assert ChaveComHashFixo(10) in conjunto_com_colisoes
assert ChaveComHashFixo(quantidade_elementos) not in conjunto_com_colisoes
assert len(conjunto_com_colisoes) == quantidade_elementos
assert tempo_com_colisoes > tempo_hash_bom

print("Todos os testes passaram!")
