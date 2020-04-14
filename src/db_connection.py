import pymysql
import pymysql.cursors as mc
import contextlib

from src.db_config import (MYSQL_DATABASE_USER, 
    MYSQL_DATABASE_PASSWORD, MYSQL_DATABASE_DB, 
    MYSQL_DATABASE_CURSOR, 
    MYSQL_DATABASE_HOST, 
    MYSQL_DATABASE_DRIVER,
    MYSQL_DATABASE_PORT)


# For database connection
@contextlib.contextmanager
def connection(cursorclass, host, user, passwd, dbname, 
							driver=MYSQL_DATABASE_DRIVER):
	connection = driver.connect(
			host=host, user=user, passwd=passwd, db=dbname, cursorclass=cursorclass, port=MYSQL_DATABASE_PORT)
	try:
			yield connection
	except Exception:
			connection.rollback()
			raise
	else:
			connection.commit()
	finally:
			connection.close()

@contextlib.contextmanager
def cursor(cursorclass, 
					host = MYSQL_DATABASE_HOST, 
					user = MYSQL_DATABASE_USER,
					 passwd = MYSQL_DATABASE_PASSWORD, 
					 dbname = MYSQL_DATABASE_DB):
	with connection(cursorclass, host, user, passwd, dbname) as conn:
		cursor = conn.cursor()
		try:
			yield cursor
		finally:
			cursor.close()


class database:
	# get data function is used to retrieved data from database
	def getData(self, query):
		with cursor(MYSQL_DATABASE_CURSOR) as cur:
			# building a database connection
			connection = cur.connection
			# execute the query
			cur.execute(query)
			# get the result from cursor
			result = cur.fetchall()
			#  return the result
			return list(result)
	
	# for adding data to database	 
	def editData(self, query):
		with cursor(MYSQL_DATABASE_CURSOR) as cur:
			connection = cur.connection
			cur.execute(query)
			num = cur.lastrowid
			return num

exdb = database()