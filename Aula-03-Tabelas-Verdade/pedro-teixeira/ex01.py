# ============================================================
# SAFE TRAFFIC - MOTOR DE DECISÃO SEMAFÓRICA
# Aula 03 - Tabelas-Verdade
# Pedro Fonseca Teixeira
# Data: 31/08/2026
# ============================================================

# %%
def decidir_sinal_verde(
    ambulancia: bool,
    fluxo_alto: bool,
    pedestre: bool,
    cancela_trem: bool
) -> bool:

    # Regra 1: se a cancela do trem estiver fechada,
    # ninguém pode avançar.
    if cancela_trem:
        return False

    # Regra 2: ambulância tem prioridade.
    if ambulancia:
        return True

    # Regra 3 e 4:
    # o sinal fica verde somente quando existe fluxo alto
    # e não há pedestre atravessando.
    return fluxo_alto and not pedestre


# ============================================================
# BATERIA DE TESTES / ASSERTS
# ============================================================

assert decidir_sinal_verde(True, False, True, False) == True
assert decidir_sinal_verde(False, True, False, False) == True
assert decidir_sinal_verde(False, True, True, False) == False
assert decidir_sinal_verde(True, True, False, True) == False
assert decidir_sinal_verde(False, False, False, False) == False


# Mostra o resultado de cada teste
print(decidir_sinal_verde(True, False, True, False))
print(decidir_sinal_verde(False, True, False, False))
print(decidir_sinal_verde(False, True, True, False))
print(decidir_sinal_verde(True, True, False, True))
print(decidir_sinal_verde(False, False, False, False))

print("SUCESSO: TODAS AS REGRAS LÓGICAS FORAM HOMOLOGADAS!")


# ============================================================
# TESTE INTERATIVO
# ============================================================

print("\n===== SAFE TRAFFIC =====")
print("Motor de decisão semafórica\n")


ambulancia = input("Há uma ambulância? (s/n): ").lower() == "s"

fluxo_alto = input(
    "O fluxo de veículos está alto? (s/n): "
).lower() == "s"

pedestre = input(
    "Há pedestre atravessando? (s/n): "
).lower() == "s"

cancela_trem = input(
    "A cancela do trem está fechada? (s/n): "
).lower() == "s"


resultado = decidir_sinal_verde(
    ambulancia,
    fluxo_alto,
    pedestre,
    cancela_trem
)


print("\n===== RESULTADO =====")

if resultado:
    print("SINAL VERDE: o fluxo pode avançar.")
else:
    print("SINAL VERMELHO: o fluxo deve parar.")
# %%