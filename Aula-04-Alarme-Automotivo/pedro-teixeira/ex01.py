# ============================================================
# ESTUDO DE CASO: ALARME AUTOMOTIVO
# Aula 04 - Lógica Combinacional e Tabela-Verdade
# Pedro Fonseca Teixeira
# ============================================================
# Variáveis:
#   A = Porta do veículo      (1: aberta   | 0: fechada)
#   B = Chave de ignição      (1: ligada   | 0: desligada)
#   C = Interruptor dos faróis (1: ligados | 0: desligados)
#
# Regra 1 (alerta de bateria):  faróis ligados E ignição desligada  -> C and not B
# Regra 2 (alerta de segurança): porta aberta E ignição ligada      -> A and B
#
# Expressão final: S = (C AND NOT B) OR (A AND B)
# ============================================================
from itertools import product


def alarme_soa(porta_aberta: bool, ignicao_ligada: bool, farois_ligados: bool) -> bool:

    # Regra 1: alerta de bateria
    alerta_bateria = farois_ligados and not ignicao_ligada

    # Regra 2: alerta de segurança
    alerta_seguranca = porta_aberta and ignicao_ligada

    return alerta_bateria or alerta_seguranca


# ============================================================
# BATERIA DE TESTES / ASSERTS
# ============================================================

assert alarme_soa(False, False, True) == True    # faróis ligados com ignição desligada
assert alarme_soa(True, True, False) == True     # porta aberta com ignição ligada
assert alarme_soa(False, True, True) == False    # ignição ligada, porta fechada
assert alarme_soa(True, False, False) == False   # porta aberta, mas ignição desligada
assert alarme_soa(False, False, False) == False  # tudo desligado
print("SUCESSO: TODAS AS REGRAS DO ALARME FORAM VALIDADAS!")


# ============================================================
# TABELA-VERDADE (2³ = 8 combinações)
# ============================================================

print("\n A | B | C || S")
print("---------------")
for porta_aberta, ignicao_ligada, farois_ligados in product([0, 1], repeat=3):
    saida = alarme_soa(bool(porta_aberta), bool(ignicao_ligada), bool(farois_ligados))
    print(f" {porta_aberta} | {ignicao_ligada} | {farois_ligados} || {int(saida)}")
