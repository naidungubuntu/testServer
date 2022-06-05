import sqlite3
import pandas as pd

def query_data(qr):
    import sqlite3
    import pandas as pd
    record = None
    try:
        sqliteConnection = sqlite3.connect('data.db')
        cursor = sqliteConnection.cursor()
        cursor.execute(qr)
        record = cursor.fetchall()
        cursor.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return pd.DataFrame(record)