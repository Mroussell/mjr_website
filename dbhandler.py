"""
MJR
Michael Roussell
Copyright 2022

This file handlers all of the database connectivity for the app.

Python 3.9.7 version of the python interpreter.
If there are any questions, please contact me at 'mjr.dev.contact@gmail.com.

MIT Education License Preferred.
"""
import os
import psycopg2
from dotenv import load_dotenv

class DBHandler:

	# Load Database URL and then connect to database
	def initdbconnect(self):
		"""
		Initializes the psycopg2 DATABASE Connection object.
		"""
		load_dotenv()
		try:
			DATABASE_URL = os.getenv('DATABASE_URL')
			conn = psycopg2.connect(DATABASE_URL, sslmode='require')
			return conn
		except ValueError:
			print("Please use your own DATABASE_URL. Define it in to your .env file!")
			quit()


	def initdbcursor(self, conn):
		"""
		Initializes the psycopg2 DATABASE Curser for DATABASE Interaction.

		Parameter
		---------
			conn : pscopq2 connect object (required)
				An object that hold the connect object for the psycopg2 library that initializes DB connection.
		"""
		cur = conn.cursor()
		return cur


	def create_table(self):
		"""
		Used the psycopg2 init functions to create table if one does not already exist. If it does throw error and pass.

		"""
		connect = self.initdbconnect()
		cursor = self.initdbcursor(connect)
		try:
			cursor.execute('''CREATE TABLE IF NOT EXISTS tech_projects_test (
			    POST_ID SERIAL NOT NULL,
			    POST_IMG_Loc text,
			    TITLE varchar(100),
			    BODY text,
			    PRIMARY KEY (POST_ID)
				);''')
			connect.commit()
			connect.close()
			print(f"Table Created!")
			return
		except ValueError:
			print(f"Table Creation error. Either already exist or other. \n{ValueError}")
			connect.commit()
			connect.close()
			pass

	
	def inspect_table(self):
		"""
		Used the psycopg2 init functions to inspect table if one does not already exist. If it does throw error and pass.

		"""
		connect = self.initdbconnect()
		cursor = self.initdbcursor(connect)
		try:
			cursor.execute('''SELECT * FROM tech_projects_test;''')
			connect.commit()
			connect.close()
			print(f"Table Inspected!")
			return
		except ValueError:
			print(f"Table Creation error. Either already exist or other. \n{ValueError}")
			connect.commit()
			connect.close()
			pass		


bdh = DBHandler()
bdh.inspect_table()

