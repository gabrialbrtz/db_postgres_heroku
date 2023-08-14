import os
import psycopg2
from dotenv import load_dotenv


class PostgresConnector:
    """
    Connector PostgresSQL data base
    """

    def __init__(self):
        self.load_env = load_dotenv()
        self.url_db = os.getenv('DATABASE_URL')

    def db_connection(self):
        """
        Function to connect to a specific URL postgres database in Heroku
        """
        return psycopg2.connect(self.url_db, sslmode='require')

    @staticmethod
    def read_sql_file(file_path):
        """
        Read SQL files
        :param file_path: "Path of the .sql file to read"
        :return: The .sql ready to execute a SQL query
        """
        with open(file_path, 'r') as file:
            sql_query = file.read()
        return sql_query
