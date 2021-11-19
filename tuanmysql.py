# TODO:
# - Add more conditional operators to the WHERE clause (OR, IN, BETWEEN, etc.)

class TuanMySQL:
    ''' Some utilities for MySQL connection. '''
    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.sql = ''

    def select(self, *columns):
        self.sql += 'SELECT '
        for column in columns:
            self.sql += column + ', '
        self.sql = self.sql[:-2] + ' '
        return self

    def from_table(self, table):
        self.sql += 'FROM ' + table + ' '
        return self

    def join(self, table, *conditions):
        self.sql += 'JOIN ' + table + ' '
        self.sql += 'ON '
        for condition in conditions:
            self.sql += str(condition) + ' AND '
        self.sql = self.sql[:-4] + ' '
        return self

    def where(self, *conditions):
        self.sql += 'WHERE '
        for condition in conditions:
            self.sql += str(condition) + ' AND '
        self.sql = self.sql[:-4] + ' '
        return self

    def group_by(self, *columns):
        self.sql += 'GROUP BY '
        for column in columns:
            self.sql += column + ', '
        self.sql = self.sql[:-2] + ' '
        return self

    def having(self, *conditions):
        self.sql += 'HAVING '
        for condition in conditions:
            self.sql += str(condition) + ' AND '
        self.sql = self.sql[:-4] + ' '
        return self

    def order_by(self, *columns):
        self.sql += 'ORDER BY '
        for column in columns:
            self.sql += column + ', '
        self.sql = self.sql[:-2] + ' '
        return self

    def limit(self, limit):
        self.sql += 'LIMIT ' + str(limit) + ' '
        return self

    def update(self, table):
        self.sql += 'UPDATE ' + table + ' '
        return self

    def set(self, *data):
        self.sql += 'SET '
        for column, value in data:
            self.sql += column + ' = ' + str(value) + ', '
        self.sql = self.sql[:-2] + ' '
        return self

    def execute(self):
        ''' Execute the sql. '''
        self.cursor.execute(self.sql)
        sql = self.sql
        self.sql = ''
        if sql.split()[0] == 'SELECT':
            result = self.cursor.fetchall()
            return TuanMySQLResult(result)
        self.connection.commit()
        return TuanMySQLResult([])

    def __str__(self):
        return self.sql


class TuanMySQLResult:
    ''' Some utilities for getting result. '''
    def __init__(self, result):
        self.result = result

    def first(self) -> list:
        ''' Get first column of the result. '''
        return [row[0] for row in self.result]

    def all(self) -> list:
        ''' Get the original result. '''
        return self.result