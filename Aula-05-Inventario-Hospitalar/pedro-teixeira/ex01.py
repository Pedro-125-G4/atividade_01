# ============================================================
# MISSÃO DE SALA - SQUAD URBANINVENTORY
# Aula 05 - all(), any() e List Comprehension
# Pedro Fonseca Teixeira
# ============================================================

# Prazo máximo (em dias) desde a última revisão
PRAZO_REVISAO_DIAS = 180

# Base de teste com 4 equipamentos
equipamentos = [
    {"id": "RESP-01", "nome": "Respirador 1", "setor": "UTI",     "dias": 45,  "revisado": True},
    {"id": "RESP-02", "nome": "Respirador 2", "setor": "UTI",     "dias": 210, "revisado": True},
    {"id": "BOMB-01", "nome": "Bomba 1",      "setor": "Triagem", "dias": 30,  "revisado": False},
    {"id": "MON-01",  "nome": "Monitor 1",    "setor": "UTI",     "dias": 100, "revisado": True},
]


def dentro_do_prazo(equipamento):
    return equipamento["dias"] <= PRAZO_REVISAO_DIAS


def tem_problema(equipamento):
    return not dentro_do_prazo(equipamento) or not equipamento["revisado"]


# ============================================================
# TAREFA 1 - all(): todos estão dentro do prazo de revisão?
# ============================================================

todos_no_prazo = all(dentro_do_prazo(equipamento) for equipamento in equipamentos)

print("Tarefa 1 - Todos os equipamentos estão dentro do prazo?", todos_no_prazo)


# ============================================================
# TAREFA 2 - any(): existe algum equipamento da UTI sem revisão?
# ============================================================

uti_sem_revisao = any(
    equipamento["setor"] == "UTI" and not equipamento["revisado"]
    for equipamento in equipamentos
)

print("Tarefa 2 - Existe equipamento da UTI sem revisão?", uti_sem_revisao)


# ============================================================
# TAREFA 3 - list comprehension: IDs dos equipamentos com problema
# ============================================================

ids_com_problema = [equipamento["id"] for equipamento in equipamentos if tem_problema(equipamento)]

print("Tarefa 3 - IDs dos equipamentos com problema:", ids_com_problema)


# ============================================================
# BATERIA DE TESTES / ASSERTS
# ============================================================

assert todos_no_prazo == False                    # Respirador 2 passou do prazo (210 dias)
assert uti_sem_revisao == False                   # todos os equipamentos da UTI estão revisados
assert ids_com_problema == ["RESP-02", "BOMB-01"]  # fora do prazo + não revisado
print("\nSUCESSO: TODAS AS VERIFICAÇÕES DO INVENTÁRIO PASSARAM!")
