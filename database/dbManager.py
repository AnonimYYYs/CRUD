# todo() import psycopg2
import json
import os


class DatabaseManager:
    def __init__(self):
        with open(f"{os.path.dirname(__file__)}/config.json", "r") as cfgFile:
            db_config = json.load(cfgFile)
        self.table_name = db_config.get("TABLE_NAME")

        self.conn = psycopg2.connect(
            host=db_config.get("HOST"),
            database=db_config.get("DB_NAME"),
            user=db_config.get("SUPERUSER"),
            password=db_config.get("SUPERUSER_PASSWORD")
        )

        self.cursor = self.conn.cursor()

    def select_all(self):
        self.cursor.execute(f"select * from {self.table_name}")
        select_result = self.cursor.fetchall()
        return select_result


    def select_by_hash(self, hash_value):
        self.cursor.execute(f"select * from {self.table_name} where {self.table_name}.hash = {hash_value}")
        select_result = self.cursor.fetchall()
        return select_result

def return_dull_db_select():
    return [(1, 'item1', 'sdasdasdfqfqw', 123), (2, 'item2', 'ddddddaaassaaaassa', None), (3, 'not item', 'dd', 11), (4, 'also item', 'qwwqqqwqwqwqqwqwwqdqwdshhfsh', 11)]

if __name__ == "__main__":

    from database.dbManager import DatabaseManager
    db = DatabaseManager()
    result = db.select_all()