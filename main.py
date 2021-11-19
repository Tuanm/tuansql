from tuanmysql import TuanMySQL
import mysql.connector

tuan = TuanMySQL(mysql.connector.connect(
    user='root',
    password='',
    database='test'
))

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
