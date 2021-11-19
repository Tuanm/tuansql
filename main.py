from tuanmysql import TuanMySQL
import mysql.connector

if __name__ == '__main__':

    # Connect to MySQL

    tuan = TuanMySQL(mysql.connector.connect(
        user='root',
        password='',
        database='test'
    ))

    # For testing

    result = tuan\
        .select('name', 'age')\
        .from_table('user')\
        .where('age > 19', 'name = "Tuan"')\
        .execute().first()
    print(result)

    tuan\
        .update('user')\
        .set(['name', '"Tuan"'], ['age', 12])\
        .where('age > 17')\
        .execute()

