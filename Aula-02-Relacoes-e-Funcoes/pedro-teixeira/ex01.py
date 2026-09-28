# ============================================================
# PARTE 1 - CONJUNTOS, PRODUTO CARTESIANO E RELAÇÃO
# ============================================================

equipamentos = {
    "Notebook",
    "Projetor",
    "Roteador",
    "Impressora"
}

bairros = {
    "Centro",
    "Vila Nova",
    "Jardim Sul"
}

produto_cartesiano = {
    (equipamento, bairro)
    for equipamento in equipamentos
    for bairro in bairros
}

relacao_atendimento = {
    ("Notebook", "Centro"),
    ("Projetor", "Centro"),
    ("Roteador", "Vila Nova"),
    ("Impressora", "Jardim Sul")
}

print("========== PARTE 1 ==========")

print("\nProduto cartesiano:")
for par in sorted(produto_cartesiano):
    print(par)

print("\nRelação de atendimento:")
for par in sorted(relacao_atendimento):
    print(par)

print("\nQuantidade de elementos de A x B:", len(produto_cartesiano))


# ============================================================
# PARTE 2 - FUNÇÃO INJETORA
# ============================================================

f = {
    "Notebook": "TI",
    "Projetor": "Educação",
    "Roteador": "Infraestrutura",
    "Impressora": "Administração"
}

imagem = set(f.values())

print("\n\n========== PARTE 2 ==========")

print("\nFunção f:")
for ativo, secretaria in f.items():
    print(f"{ativo} -> {secretaria}")

print("\nImagem de f:", imagem)

if len(imagem) == len(f):
    print("f é INJETORA.")
else:
    print("f NÃO é injetora.")


# ============================================================
# PARTE 3 - FUNÇÃO INVERSA E BIJETIVIDADE
# ============================================================

h = {
    "Notebook": "TOMB-901",
    "Projetor": "TOMB-902",
    "Roteador": "TOMB-903",
    "Impressora": "TOMB-904"
}

tombamentos = {
    "TOMB-901",
    "TOMB-902",
    "TOMB-903",
    "TOMB-904"
}

h_inversa = {
    tombamento: ativo
    for ativo, tombamento in h.items()
}

print("\n\n========== PARTE 3 ==========")

print("\nFunção h:")
for ativo, tombamento in h.items():
    print(f"{ativo} -> {tombamento}")

print("\nFunção inversa h⁻¹:")
for tombamento, ativo in h_inversa.items():
    print(f"{tombamento} -> {ativo}")

# Verificação da bijetividade
eh_injetora = len(set(h.values())) == len(h)

eh_sobrejetora = set(h.values()) == tombamentos

if eh_injetora and eh_sobrejetora:
    print("\nh é BIJETORA.")
else:
    print("\nh não é bijetora.")


# ============================================================
# PARTE 4 - COMPOSIÇÃO (g ∘ f) E VALIDAÇÃO
# ============================================================

g = {
    "TI": "TOMB-901",
    "Educação": "TOMB-902",
    "Infraestrutura": "TOMB-903",
    "Administração": "TOMB-904"
}


def composicao(ativo):

    if ativo not in f:
        return None

    secretaria = f[ativo]

    if secretaria not in g:
        return None

    return g[secretaria]


print("\n\n========== PARTE 4 ==========")

print("\nComposição g ∘ f:")

for ativo in f:
    resultado = composicao(ativo)
    print(f"{ativo} -> {resultado}")


# Validação do TOMB-901
def buscar_tombamento(tombamento):

    for ativo in f:
        if composicao(ativo) == tombamento:
            return ativo

    return None


tombamento_procurado = "TOMB-901"

ativo = buscar_tombamento(tombamento_procurado)

if ativo:
    print(f"\n{tombamento_procurado} pertence ao ativo: {ativo}")
else:
    print(f"\n{tombamento_procurado} não foi encontrado.")


# Teste com tombamento inexistente
tombamento_inexistente = "TOMB-999"

ativo = buscar_tombamento(tombamento_inexistente)

if ativo:
    print(f"{tombamento_inexistente} pertence ao ativo: {ativo}")
else:
    print(f"{tombamento_inexistente} não existe no inventário.")