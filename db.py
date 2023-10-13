import logging
import logging.config
import mysql.connector
from configparser import ConfigParser
from mysql.connector import Error
import yaml
import os
import time
from datetime import datetime

# Loading logging configuration
with open('./log_migrate_db.yaml', 'r') as stream:
    config = yaml.safe_load(stream)

logging.config.dictConfig(config)

#Creating logger
logger = logging.getLogger('root')

# Initiating and reading config values
logger.info('Loading configuration from file')

try:
	config = ConfigParser()
	config.read('config.ini')

	mysql_host = config.get('mysql_config', 'mysql_host')
	mysql_db = config.get('mysql_config', 'mysql_db')
	mysql_user = config.get('mysql_config', 'mysql_user')
	mysql_passwd = config.get('mysql_config', 'mysql_pass')

except:
	logger.exception('')
logger.info('DONE')

def init_db():
    global conn
    conn = mysql.connector.connect(
        host=mysql_host, 
        user=mysql_user, 
        password=mysql_passwd,
        database=mysql_db
        )
	
init_db()

#insert joke into db
def insert_joke_into_db(id, text, type, flags):
	data = (id, text, type, str(flags))
	sql_query = "INSERT INTO liked_jokes (id, text, type, flags) VALUES (%s, %s, %s, %s)"
	try:
		# Execute the SQL query using data variable
		cursor.execute(sql_query, data)
		# Commit the transaction
		conn.commit()
		logger.info( sql_query )
		logger.info("Successful insertion")
	except mysql.connector.Error as error:
		logger.error( sql_query )
		logger.error("Error: {}".format(error))


def get_cursor():
	global conn
	try:
		conn.ping(reconnect=True, attempts=1, delay=0)
		conn.commit()
	except mysql.connector.Error as err:
		logger.error("No connection to db " + str(err))
		conn = init_db()
		conn.commit()
	return conn.cursor()
	

# Opening connection to mysql DB
logger.info('Connecting to MySQL DB')
try:

	cursor = get_cursor()
	if conn.is_connected():
		db_Info = conn.get_server_info()
		logger.info('Connected to MySQL database. MySQL Server version on ' + str(db_Info))
		cursor = conn.cursor()
		cursor.execute("select database();")
		record = cursor.fetchone()
		logger.debug('You are connected to - ' + record[0])
		conn.commit()
except Exception as e:
	logger.error('Error while connecting to MySQL ' + str(e))



