# ============================================================
# ATIVIDADE DE FIXAÇÃO EXTRACLASSE - AULA 06
# Exercício 4 - Desafio prático: rotas circulares
# Pedro Fonseca Teixeira
# ============================================================

from itertools import product


def detectar_rotas_circulares(linhas: dict[str, list[str]]) -> set[tuple[str, str]]:
    # Recebe um dicionário: estação -> lista de estações com ligação direta.
    # Devolve os pares de estações com ligação nos DOIS sentidos (A -> B e B -> A).
    # Cada par aparece uma vez só, em ordem alfabética: ("A", "B").

    # Produto cartesiano {origem} x destinos: gera todas as conexões (origem, destino)
    conexoes = set()
    for estacao_origem, estacoes_destino in linhas.items():
        conexoes |= set(product([estacao_origem], estacoes_destino))

    # Conjunto com as mesmas conexões, mas no sentido contrário
    conexoes_invertidas = {(destino, origem) for origem, destino in conexoes}

    # Interseção: só fica a conexão que existe nos dois sentidos
    conexoes_bidirecionais = conexoes & conexoes_invertidas

    # Remove repetição (A, B) / (B, A) e ignora estação ligada a ela mesma
    return {
        (origem, destino)
        for origem, destino in conexoes_bidirecionais
        if origem < destino
    }


# Exemplo de uso
linhas_metro = {
    "Centro": ["Rodoviária", "Hospital", "Praça"],
    "Rodoviária": ["Centro", "Aeroporto"],
    "Hospital": ["Centro"],
    "Aeroporto": ["Shopping"],
    "Praça": ["Shopping"],
    "Shopping": ["Praça"],
}

rotas_circulares = detectar_rotas_circulares(linhas_metro)
print("Rotas circulares (ida e volta direta):")
for estacao_a, estacao_b in sorted(rotas_circulares):
    print(f"  {estacao_a} <-> {estacao_b}")


# ============================================================
# BATERIA DE TESTES / ASSERTS
# ============================================================

assert rotas_circulares == {
    ("Centro", "Rodoviária"),
    ("Centro", "Hospital"),
    ("Praça", "Shopping"),
}

# Ligação só de ida não conta
assert detectar_rotas_circulares({"A": ["B"], "B": []}) == set()

# Estação sem ligações e dicionário vazio
assert detectar_rotas_circulares({}) == set()
assert detectar_rotas_circulares({"A": []}) == set()

# Laço na própria estação não conta como rota entre pares
assert detectar_rotas_circulares({"A": ["A"]}) == set()

# Destino repetido não gera par duplicado
assert detectar_rotas_circulares({"A": ["B", "B"], "B": ["A"]}) == {("A", "B")}

print("Todos os testes passaram!")
