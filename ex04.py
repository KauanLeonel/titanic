#4. Qual o porto que ocorreu o embarque com a quantidade maior de sobreviventes?

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/train.csv")

# Seleciona apenas os sobreviventes
sobreviventes = df[df["Survived"] == 1]

# Conta sobreviventes por porto
sobreviventes_por_porto = (
    sobreviventes["Embarked"]
    .value_counts()
)

# Descobre o porto com maior quantidade
porto_maior = sobreviventes_por_porto.idxmax()
quantidade_maior = sobreviventes_por_porto.max()

# Nome dos portos
portos = {
    "C": "Cherbourg",
    "Q": "Queenstown",
    "S": "Southampton"
}

nome_porto = portos.get(porto_maior, porto_maior)

conclusao = (
    f"O porto com maior quantidade de sobreviventes foi "
    f"{nome_porto}, com {quantidade_maior} sobreviventes."
)

print(sobreviventes_por_porto)
print(conclusao)

# Gráfico
fig, ax = plt.subplots(figsize=(8, 6))

sobreviventes_por_porto.plot(
    kind="bar",
    ax=ax
)

ax.set_title("Quantidade de sobreviventes por porto de embarque")
ax.set_xlabel("Porto de embarque")
ax.set_ylabel("Quantidade de sobreviventes")
ax.tick_params(axis="x", rotation=0)

for barra in ax.patches:
    altura = barra.get_height()

    ax.text(
        barra.get_x() + barra.get_width() / 2,
        altura,
        f"{int(altura)}",
        ha="center",
        va="bottom"
    )

ax.text(
    0.5,
    0.95,
    conclusao,
    transform=ax.transAxes,
    ha="center",
    va="top",
    wrap=True,
    bbox={
        "boxstyle": "round",
        "facecolor": "white",
        "alpha": 0.8
    }
)

plt.tight_layout()
plt.show()