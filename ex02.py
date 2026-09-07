#2. A classe do passageiro estava associada à sobrevivência?

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/train.csv")

# Calcula a taxa de sobrevivência por classe
taxa_classe = (
    df.groupby("Pclass")["Survived"]
    .mean()
    .mul(100)
    .round(2)
)

print(taxa_classe)

# Estrutura de decisão
maior_taxa = taxa_classe.idxmax()
menor_taxa = taxa_classe.idxmin()

if taxa_classe.nunique() > 1:
    conclusao = (
        f"Sim. A classe estava associada à sobrevivência. "
        f"A {maior_taxa}ª classe apresentou a maior taxa."
    )
else:
    conclusao = "Não houve diferença na taxa de sobrevivência entre as classes."

# Criação do gráfico
fig, ax = plt.subplots(figsize=(8, 6))

taxa_classe.plot(
    kind="bar",
    ax=ax
)

ax.set_title("Taxa de sobrevivência por classe")
ax.set_xlabel("Classe do passageiro")
ax.set_ylabel("Sobrevivência (%)")
ax.set_ylim(0, 100)
ax.tick_params(axis="x", rotation=0)

# Valores sobre as barras
for barra in ax.patches:
    altura = barra.get_height()

    ax.text(
        barra.get_x() + barra.get_width() / 2,
        altura + 2,
        f"{altura:.1f}%",
        ha="center"
    )

# Conclusão dentro do gráfico
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