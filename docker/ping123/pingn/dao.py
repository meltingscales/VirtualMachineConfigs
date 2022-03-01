import psycopg2


class Singleton:  # stolen from https://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Also, the decorated class cannot be
    inherited from. Other than that, there are no restrictions that apply
    to the decorated class.

    To get the singleton instance, use the `instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    """

    def __init__(self, decorated):
        self._decorated = decorated

    def instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            pass
        self._instance = self._decorated()
        return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


@Singleton
class DAO:
    def __init__(self, host='localhost', port=5432, database='pingn', user='postgres', password='postgres'):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

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

        cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{}'".format(self.database))
        exists = cursor.fetchone()
        if not exists:
            print("Database {} does not exist. Creating.".format(self.database))
            cursor.execute('CREATE DATABASE {}'.format(self.database))
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

    def logEvent(self, event:str) -> None:
        cursor = self.connection.cursor()

        cursor.execute('''
            INSERT INTO TABLE logs (msg, date) VALUES('{}', NOW())
        '''.format(event))

        cursor.close()