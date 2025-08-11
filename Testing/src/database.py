import pymysql as MySQLdb

def query_db(client: MySQLdb.Connection, sql: str):
    cursor = client.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    cursor.close()
    return row
