# ============================================================
# ATIVIDADE DE FIXAÇÃO EXTRACLASSE - AULA 06
# Exercício 2 - Simplificação de expressão de conjuntos
# Pedro Fonseca Teixeira
# ============================================================

# Expressão: (A ∩ B) ∪ (A ∩ B')
#
# Passo 1 - Propriedade distributiva (colocando A em evidência):
#     (A ∩ B) ∪ (A ∩ B') = A ∩ (B ∪ B')
#
# Passo 2 - Lei do complemento (um conjunto unido ao seu complemento
# é o universo):
#     B ∪ B' = U
#
# Passo 3 - Lei da identidade (A interseção com o universo é o próprio A):
#     A ∩ U = A
#
# Resultado: (A ∩ B) ∪ (A ∩ B') = A
#
# Observação: De Morgan, (X ∪ Y)' = X' ∩ Y', confirma o mesmo resultado
# pelo complemento: [(A ∩ B) ∪ (A ∩ B')]' = (A ∩ B)' ∩ (A ∩ B')
#                                          = (A' ∪ B') ∩ (A' ∪ B) = A' ∪ (B' ∩ B) = A'
# Se o complemento da expressão é A', a expressão é A.

# Verificação prática com conjuntos de exemplo
universo = set(range(1, 11))
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7}
complemento_b = universo - conjunto_b

expressao_original = (conjunto_a & conjunto_b) | (conjunto_a & complemento_b)

print("A =", sorted(conjunto_a))
print("(A ∩ B) ∪ (A ∩ B') =", sorted(expressao_original))


# ============================================================
# BATERIA DE TESTES / ASSERTS
# ============================================================

assert expressao_original == conjunto_a

# Testa também com outros conjuntos, inclusive vazios
casos_de_teste = [
    (set(), {1, 2}),
    ({1, 2, 3}, set()),
    ({1, 2, 3}, {1, 2, 3}),
    ({2, 4, 6, 8, 10}, {2, 3, 5, 7}),
]
for teste_a, teste_b in casos_de_teste:
    teste_b_complemento = universo - teste_b
    assert (teste_a & teste_b) | (teste_a & teste_b_complemento) == teste_a

print("Todos os testes passaram!")
