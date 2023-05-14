import sqlite3
from sqlalchemy import create_engine

def deletar(self):
    conn = sqlite3.connect('D:/Banco de Dados Python/agenda.db')
    engine = create_engine('sqlite:///D:/Banco de Dados Python/agenda.db')

    try:
        conn.execute(f'DROP TABLE {self};')
        print("Tabela deletada com sucesso!")
    except Exception as ex:
        print("Erro ao deletar a tabela!")


def criarFuncao(self):
    conn = sqlite3.connect('D:/Banco de Dados Python/agenda.db')
    engine = create_engine('sqlite:///D:/Banco de Dados Python/agenda.db')

    conn.execute(f"CREATE TABLE {self} (X INTEGER PRIMARY KEY,Y INTEGER);")

    for i in range(-100, 101):

        try:
            conn.execute(f"INSERT INTO {self} (X, Y) VALUES ({i}, {i ** 3 + i ** 2});")
            conn.commit()

        except Exception as ex:
            print("Erro ao inserir valores!")




deletar('Valores')
