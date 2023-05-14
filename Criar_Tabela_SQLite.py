import sqlite3
from sqlalchemy import create_engine

conn = sqlite3.connect('D:/C#/Aplicativo_pollock_seven/Aplicativo_Pollock_Seven/bin/Debug/pollock_seven.db')

#en = create_engine('sqlite:///D:/C#/CFB_Academia/bd/banco_academia.db')

try:
    conn.execute(f"""ALTER TABLE tb_pollock ADD T_DATA VARCHAR (30);""")

except Exception as ex:
    print("Erro ao criar tabela!")