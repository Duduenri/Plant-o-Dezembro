import pandas as pd

# Carregar o calendário de plantões
calendario_df = pd.read_csv("calendario_plantao_dezembro_2024.csv")

# Lista de pessoas
pessoas = ["Bianca", "Carol", "Claudio", "Franer", "Illie", "Luciana", "Marcio", "Martini", "Neto", "Rafael"]

# Gerar relatório individual para cada pessoa
for pessoa in pessoas:
    # Filtrar o DataFrame para a pessoa atual
    relatorio_pessoa = calendario_df[calendario_df["Pessoa"] == pessoa]
    
    # Salvar o relatório em um arquivo CSV
    relatorio_pessoa.to_csv(f"relatorio_{pessoa.lower()}.csv", index=False)

    # Exibir o relatório no console (opcional)
    print(f"Relatório de {pessoa}:")
    print(relatorio_pessoa)
    print("\n")