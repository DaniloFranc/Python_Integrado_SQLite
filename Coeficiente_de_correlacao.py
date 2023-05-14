import sqlite3
from sqlalchemy import create_engine
import pandas as pd

# Conecte-se ao banco de dados SQLite
conn = sqlite3.connect('D:/Banco de Dados Python/agenda.db')

# Crie um engine do SQLAlchemy a partir da conexão com o SQLite
engine = create_engine('sqlite:///D:/Banco de Dados Python/agenda.db')


conn.execute("CREATE TABLE Valores (X INTEGER PRIMARY KEY,Y INTEGER);")

# Leia os dados da tabela "Valores" para um DataFrame do Pandas usando o SQLAlchemy

for i in range(-100, 101):

    try:
        conn.execute(f"INSERT INTO Valores (X, Y) VALUES ({i}, {i**3 + i**2});")
        conn.commit()
       # print("Valores inseridos com sucesso!")

    except Exception as ex:
        print("Erro ao inserir valores!")


#df = pd.read_sql('SELECT * FROM Valores', con=conn)

# Calcule a correlação entre as colunas X e Y usando o Pandas
#correlacao = df['X'].corr(df['Y'])


# Imprima o resultado da correlação
#print(f"A correlação entre as colunas X e Y é {correlacao}")


#print(df)