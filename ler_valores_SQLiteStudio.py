import sqlite3
from sqlalchemy import create_engine
import pandas as pd

conn = sqlite3.connect('D:/Banco de Dados Python/agenda.db')

#en = create_engine('sqlite:///D:/Banco de Dados Python/agenda.db')

df = pd.read_sql('SELECT * FROM Valores Where X > 0', con=conn)

# Calcule a correlação entre as colunas X e Y usando o Pandas
correlacao = df['X'].corr(df['Y'])


# Imprima o resultado da correlação
print(f"A correlação entre as colunas X e Y é {correlacao}")


print(df)