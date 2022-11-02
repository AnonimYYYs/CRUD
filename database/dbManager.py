import psycopg2
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
        self.cursor.execute(f'select * from {self.table_name} order by "id"')
        select_result = self.cursor.fetchall()
        return select_result


    def select_by_hash(self, hash_value):
        self.cursor.execute(f"select * from {self.table_name} where {self.table_name}.hash = {hash_value}")
        select_result = self.cursor.fetchall()
        return select_result

    def delete_by_id(self, delete_id):
        string = f"delete from {self.table_name} where id = {delete_id}"
        try:
            self.cursor.execute(string)
            self.conn.commit()
        except:
            self.conn.rollback()

    def insert_row(self, ins_name, ins_desc, ins_hash):
        if ins_hash is None:
            string = f'INSERT INTO {self.table_name} ("name", "description") '
            string += f"VALUES ('{ins_name}', '{ins_desc}');"
        else:
            string = f'INSERT INTO {self.table_name} ("name", "description", "hash") '
            string += f"VALUES ('{ins_name}', '{ins_desc}', {ins_hash});"
        try:
            self.cursor.execute(string)
            self.conn.commit()
        except:
            self.conn.rollback()

    def update_row(self, upd_id, upd_name=None, upd_desc=None, upd_hash=None):
        string = f'UPDATE {self.table_name} SET '
        if upd_name is not None:
            string += f'"name" = '
            string += f"'{upd_name}',"
        if upd_desc is not None:
            string += f'"description" = '
            string += f"'{upd_desc}',"
        if upd_hash is not None:
            string += f'"hash" = '
            string += f"'{upd_hash}',"

        string = string[:-1]
        string += f' WHERE "id" = {upd_id};'

        try:
            self.cursor.execute(string)
            self.conn.commit()
        except:
            self.conn.rollback()


def return_dull_db_select():
    return [(1, 'item1', 'sdasdasdfqfqw', 123), (2, 'item2', 'ddddddaaassaaaassa', None), (3, 'not item', 'dd', 11), (4, 'also item', 'qwwqqqwqwqwqqwqwwqdqwdshhfsh', 11)]

if __name__ == "__main__":

    from database.dbManager import DatabaseManager
    db = DatabaseManager()
    result = db.select_all()