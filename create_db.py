import mysql.connector
from configparser import ConfigParser

try:
	config = ConfigParser()
	config.read('config.ini')

	mysql_host = config.get('mysql_config', 'mysql_host')
	mysql_db = ""
	mysql_user = config.get('mysql_config', 'mysql_user')
	mysql_passwd = config.get('mysql_config', 'mysql_pass')
except:
	print("problem creating db")
	
global connection
connection = mysql.connector.connect(host=mysql_host, database=mysql_db, user= mysql_user, password=mysql_passwd)

cur = connection.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS construct")