import psycopg2
from flask import Flask


class DAO:
    def __init__(self, app: Flask, host='localhost', port=5432, database='pingn', user='postgres', password='postgres'):
        self.app = app
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

        self.ensure_database_exists()

    def ensure_database_exists(self):
        cursor = self.connection.cursor()

        cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", [self.database])
        exists = cursor.fetchone()
        if not exists:
            self.app.logger.info("Database {} does not exist. Creating.".format(self.database))
            cursor.execute('CREATE DATABASE {}'.format(self.database))
        else:
            self.app.logger.info("Database {} already exists.".format(self.database))
        cursor.close()

    def ensure_table_exists(self):
        cursor = self.connection.cursor()

        cursor.execute('''
        CREATE TABLE [IF NOT EXISTS] logs (
            id      serial PRIMARY KEY,
            msg     VARCHAR(1000)       NOT NULL,
            date    TIMESTAMP           NOT NULL
        );''')

        cursor.close()

    def logEvent(self, event: str) -> None:
        cursor = self.connection.cursor()

        cursor.execute('''INSERT INTO logs(msg, date) VALUES(%s, current_timestamp);''', [str(event)])

        cursor.close()
