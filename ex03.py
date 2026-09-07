#3. A tarifa paga pelos sobreviventes era diferente da tarifa paga pelos não sobreviventes?

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/train.csv")

# Calcula a tarifa média por situação de sobrevivência
tarifa_media = (
    df.groupby("Survived")["Fare"]
    .mean()
    .round(2)
)

print(tarifa_media)

# Separa os valores
tarifa_nao_sobreviventes = tarifa_media[0]
tarifa_sobreviventes = tarifa_media[1]

# Estrutura de decisão
if tarifa_sobreviventes > tarifa_nao_sobreviventes:
    conclusao = (
        "Sim. Os sobreviventes pagaram, em média, "
        "uma tarifa maior."
    )
elif tarifa_sobreviventes < tarifa_nao_sobreviventes:
    conclusao = (
        "Sim. Os não sobreviventes pagaram, em média, "
        "uma tarifa maior."
    )
else:
    conclusao = (
        "Não. A tarifa média foi igual entre os grupos."
    )

# Renomeia para facilitar a leitura do gráfico
tarifa_media.index = [
    "Não sobreviveu",
    "Sobreviveu"
]

# Criação do gráfico
fig, ax = plt.subplots(figsize=(8, 6))

tarifa_media.plot(
    kind="bar",
    ax=ax
)

ax.set_title("Tarifa média paga por sobrevivência")
ax.set_xlabel("Situação")
ax.set_ylabel("Tarifa média")
ax.tick_params(axis="x", rotation=0)

# Coloca os valores sobre as barras
for barra in ax.patches:
    altura = barra.get_height()

    ax.text(
        barra.get_x() + barra.get_width() / 2,
        altura,
        f"{altura:.2f}",
        ha="center",
        va="bottom"
    )

# Coloca a conclusão dentro do gráfico
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