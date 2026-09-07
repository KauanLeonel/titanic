#1. Mulheres realmente tiveram maior probabilidade de sobrevivência?

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/train.csv")

# Calcula a taxa de sobrevivência
taxa_sobrevivencia = (
    df.groupby("Sex")["Survived"]
    .mean()
    .mul(100)
    .round(2)
)

taxa_mulheres = taxa_sobrevivencia["female"]
taxa_homens = taxa_sobrevivencia["male"]

# Estrutura de decisão
if taxa_mulheres > taxa_homens:
    conclusao = "Sim. Mulheres tiveram maior taxa de sobrevivência."
elif taxa_mulheres < taxa_homens:
    conclusao = "Não. Homens tiveram maior taxa de sobrevivência."
else:
    conclusao = "As taxas de sobrevivência foram iguais."

# Criação do gráfico
fig, ax = plt.subplots(figsize=(8, 6))

taxa_sobrevivencia.plot(
    kind="bar",
    ax=ax
)

ax.set_title("Taxa de sobrevivência por sexo")
ax.set_xlabel("Sexo")
ax.set_ylabel("Sobrevivência (%)")
ax.set_ylim(0, 100)

ax.tick_params(axis="x", rotation=0)

# Mostra os valores em cima das barras
for barra in ax.patches:
    altura = barra.get_height()

    ax.text(
        barra.get_x() + barra.get_width() / 2,
        altura + 2,
        f"{altura:.1f}%",
        ha="center"
    )

# Coloca a conclusão dentro do gráfico
ax.text(
    0.5,
    0.95,
    conclusao,
    transform=ax.transAxes,
    ha="center",
    va="top",
    bbox={
        "boxstyle": "round",
        "facecolor": "white",
        "alpha": 0.8
    }
)

plt.tight_layout()
plt.show()