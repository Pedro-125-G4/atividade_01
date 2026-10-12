# ============================================================
# ATIVIDADE DE FIXAÇÃO EXTRACLASSE - AULA 06
# Exercício 1 - Operações com conjuntos
# Pedro Fonseca Teixeira
# ============================================================

# Universo U = {1, 2, ..., 10}
universo = set(range(1, 11))


def eh_primo(numero):
    # Um número primo é maior que 1 e só é divisível por 1 e por ele mesmo
    if numero < 2:
        return False
    return all(numero % divisor != 0 for divisor in range(2, numero))


# A = {x | x é par}  e  B = {x | x é primo}
conjunto_pares = {numero for numero in universo if numero % 2 == 0}
conjunto_primos = {numero for numero in universo if eh_primo(numero)}

print("A (pares) =", sorted(conjunto_pares))
print("B (primos) =", sorted(conjunto_primos))

# (a) União: elementos que estão em A ou em B
uniao = conjunto_pares | conjunto_primos
print("(a) A ∪ B =", sorted(uniao))

# (b) Interseção: elementos que estão em A e em B ao mesmo tempo
intersecao = conjunto_pares & conjunto_primos
print("(b) A ∩ B =", sorted(intersecao))

# (c) Diferença: elementos de A que não estão em B
diferenca = conjunto_pares - conjunto_primos
print("(c) A \\ B =", sorted(diferenca))

# (d) Complemento da união: elementos do universo fora de A ∪ B
complemento_da_uniao = universo - uniao
print("(d) (A ∪ B)' =", sorted(complemento_da_uniao))


# ============================================================
# BATERIA DE TESTES / ASSERTS
# ============================================================

assert conjunto_pares == {2, 4, 6, 8, 10}
assert conjunto_primos == {2, 3, 5, 7}
assert uniao == {2, 3, 4, 5, 6, 7, 8, 10}
assert intersecao == {2}
assert diferenca == {4, 6, 8, 10}
assert complemento_da_uniao == {1, 9}

print("Todos os testes passaram!")
