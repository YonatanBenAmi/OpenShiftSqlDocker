import os
import pymysql

class DataLoader:
    def __init__(self):
        self.host = os.getenv("DB_HOST", "mysql")
        self.port = int(os.getenv("DB_PORT", "3306"))
        self.user = os.getenv("DB_USER", "appuser")
        self.password = os.getenv("DB_PASSWORD", "apppass123")
        self.db = os.getenv("DB_NAME", "appdb")

        def _conn(self):
            return pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.db,
                cursorclass=pymysql.cursors.DictCursor
            )
    
    def get_all_data(self):
        with self._conn as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, first_name, last_name FROM data ORDER BY id")
                return cur.fetchall()