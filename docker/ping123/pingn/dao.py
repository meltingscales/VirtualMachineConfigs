import psycopg2
from flask import Flask


class DAO:
    def __init__(self, app: Flask,
                 apphost='localhost',
                 host='localhost',
                 port=5432,
                 database='pingn',
                 user='postgres',
                 password='postgres'):
        self.app = app
        self.apphost = apphost
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

        self.app.logger.info("init dao for '{}'".format(self.host))

        self.connection = psycopg2.connect(
            host=self.host,
            port=self.port,
            database='postgres',
            user=self.user,
            password=self.password)
        self.connection.autocommit = True
        self.ensure_database_exists()
        self.connection.close()

        self.connection = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password)
        self.connection.autocommit = True

        self.ensure_table_exists()

    def ensure_database_exists(self):
        cursor = self.connection.cursor()

        cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", [self.database])
        exists = cursor.fetchone()
        if not exists:
            self.app.logger.info("Database {} does not exist. Creating.".format(self.database))
            cursor.execute('CREATE DATABASE {}'.format(self.database))
        else:
            self.app.logger.info("Database {} already exists.".format(self.database))

        self.connection.commit()
        cursor.close()

    def ensure_table_exists(self):
        cursor = self.connection.cursor()

        self.app.logger.info("ensuring 'logs' db exists.".format(self.database))

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id          serial PRIMARY KEY,
            host        VARCHAR(100)        NOT NULL,
            category    VARCHAR(100)        NOT NULL,
            msg         VARCHAR(1000)       NOT NULL,
            date        TIMESTAMP           NOT NULL
        );''')

        self.connection.commit()
        cursor.close()

    def log_event(self, category='default', event: str = None) -> None:
        cursor = self.connection.cursor()

        cursor.execute(
            '''INSERT INTO logs(host, category, msg, date)
                VALUES(%s, %s, %s, current_timestamp);''',
            [self.apphost, str(category), str(event)])

        cursor.close()
