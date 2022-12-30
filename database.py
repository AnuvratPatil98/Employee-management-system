from flask import g
import sqlite3


def connect_to_database():
    sql = sqlite3.connect('C:/Users/HP/PycharmProjects/CRUDApplication/crudapplication.db')
    sql.row_factory = sqlite3.Row
    return sql


def get_database():
    if not hasattr(g, ''):
        g.crudapplication_db = connect_to_database()
    return g.crudapplication_db
