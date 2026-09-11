# import pandas as pd

# caminho_dataset = "dataset/train.csv"
# df = pd.read_csv(caminho_dataset)

# df_7var = df[
#     [
#         "Pclass",
#         "Sex",
#         "Age",
#         "SibSp",
#         "Parch",
#         "Fare",
#         "Embarked",
#         "Survived"
#     ]
# ]

# df_7var.to_csv("dataset/train7var.csv", index= False)

# print(df_7var.head())


#CONDIÇÕES: Sex == "female" AND Pclass > 2 AND Age < 18
#DESCRIÇÃO: SOBREVIVE

import pandas as pd
import numpy as np

# Carregando o dataset
df = pd.read_csv("dataset/train.csv")

# Selecionando apenas mulheres da 3ª classe
grupo = df[
    (df["Sex"] == "female") &
    (df["Pclass"] > 2)
].copy()

print("Quantidade de passageiras:", len(grupo))

print("\nTaxa geral de sobrevivência:")
print(grupo["Survived"].mean())

# Testando diferentes idades
print("\nAnálise por idade:")

for idade in range(2, 66):

    abaixo = grupo[grupo["Age"] < idade]

    # Ignora cortes sem passageiros
    if len(abaixo) == 0:
        continue

    taxa_sobrevivencia = abaixo["Survived"].mean()

    print(
        f"Age < {idade:2d} | "
        f"Passageiros: {len(abaixo):3d} | "
        f"Sobrevivência: {taxa_sobrevivencia:.2%}"
    )