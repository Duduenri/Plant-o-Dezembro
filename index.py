import pandas as pd # type: ignore
from datetime import datetime, timedelta
import random

# Lista de pessoas
pessoas = ["Bianca", "Carol", "Claudio", "Franer", "Illie", "Luciana", "Marcio", "Martini", "Neto", "Rafael"]

# Datas de início e fim
inicio = datetime(2024, 12, 1)
fim = datetime(2024, 12, 31)

# Lista de datas válidas
datas = []
data_atual = inicio
while data_atual <= fim:
    if data_atual.weekday() != 6 and not (data_atual >= datetime(2024, 12, 21) and data_atual <= datetime(2024, 12, 31)):
        datas.append(data_atual)
    data_atual += timedelta(days=1)

# Inicializar DataFrame
calendario_df = pd.DataFrame(columns=["Data", "Turno", "Pessoa"])

# Função para distribuir plantões
def distribuir_plantoes(datas, pessoas):
    plantao_manha = []
    plantao_tarde = []
    random.shuffle(pessoas)  # Embaralhar a lista de pessoas
    index_pessoa = 0

    for data in datas:
        if data.weekday() == 5:  # Sábado
            while pessoas[index_pessoa] in ["Carol", "Illie"]:
                index_pessoa = (index_pessoa + 1) % len(pessoas)
            plantao_manha.append({"Data": data.strftime("%Y-%m-%d"), "Turno": "Manhã", "Pessoa": pessoas[index_pessoa]})
            index_pessoa = (index_pessoa + 1) % len(pessoas)
        else:
            if data <= datetime(2024, 12, 15) and pessoas[index_pessoa] == "Rafael":
                plantao_manha.append({"Data": data.strftime("%Y-%m-%d"), "Turno": "Manhã", "Pessoa": pessoas[index_pessoa]})
                index_pessoa = (index_pessoa + 1) % len(pessoas)
            else:
                plantao_manha.append({"Data": data.strftime("%Y-%m-%d"), "Turno": "Manhã", "Pessoa": pessoas[index_pessoa]})
                index_pessoa = (index_pessoa + 1) % len(pessoas)
            plantao_tarde.append({"Data": data.strftime("%Y-%m-%d"), "Turno": "Tarde", "Pessoa": pessoas[index_pessoa]})
            index_pessoa = (index_pessoa + 1) % len(pessoas)

    return plantao_manha, plantao_tarde

# Distribuir plantões
plantao_manha, plantao_tarde = distribuir_plantoes(datas, pessoas)

# Adicionar plantões ao DataFrame
calendario_df = pd.concat([calendario_df, pd.DataFrame(plantao_manha)], ignore_index=True)
calendario_df = pd.concat([calendario_df, pd.DataFrame(plantao_tarde)], ignore_index=True)

# Salvar o calendário em um arquivo CSV
calendario_df.to_csv("calendario_plantao_dezembro_2024.csv", index=False)

print(calendario_df)