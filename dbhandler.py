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
import psycopg2.extras
from psycopg2 import sql
import json
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
		cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
		return cur


	def create_table(self, table_name):
		"""
		Used the psycopg2 init functions to create table if one does not already exist. If it does throw error and pass.

		"""
		connect = self.initdbconnect()
		cursor = self.initdbcursor(connect)
		try:
			query = '''CREATE TABLE IF NOT EXISTS ''' + table_name + ''' (
			    POST_ID SERIAL NOT NULL,
			    POST_IMG_LOC text,
			    REPO_LINK text,
			    TITLE varchar(100),
			    BODY text,
			    PRIMARY KEY (POST_ID)
				);'''
			cursor.execute(query)
			connect.commit()
			connect.close()
			print(f"Table Created!")
			return
		except ValueError:
			print(f"Table Creation error. Either already exist or other. \n{ValueError}")
			connect.commit()
			connect.close()
			pass

	
	def inspect_table(self, table_name:str):
		"""
		Used the psycopg2 init functions to inspect table if one does not already exist. If it does throw error and pass.

		Parameter
		---------
			table_name : string (required)
				A String object that holds the table name for the SQL query

		Returns:
		---------
			post_json: string
				A string object that is the representation a dictionary for all rows in table.
		"""
		connect = self.initdbconnect()
		cursor = self.initdbcursor(connect)
		try:
			query = "SELECT * FROM "+ table_name + ";"
			cursor.execute(query)
			results = cursor.fetchall()
			post_json = json.dumps(results, indent=2)
			print(str(type(post_json)) + " ~ containing:")
			print(post_json)
			connect.commit()
			connect.close()
			print(f"Table Inspected!")
			return post_json
		except ValueError:
			print(f"Table Creation error. Either already exist or other. \n{ValueError}")
			connect.commit()
			connect.close()
			pass		


	def add_post(self, table_name:str, title:str, body:str, img_loc:str, repo_link:str):
		"""
		Used the psycopg2 init functions to add a post to a table. If throws error, pass.

		Parameters
		----------
			table_name : string (required)
				A String object that determins the table location for the post to be added. Has no size limit.
			title : string (required)
				A String object that holds the title of the post, under 100 characters.
			body : string (required)
				A String object that hold the body of the post. This is converted to text dataype in SQL and has no size limit.
			img_loc : string (required)
				A String object that hold the image location for the post thumbnail. Has not size limit
			repo_link: string (required)
				A String object that hold the link to the github repo for the post. Has no size limit.
		"""
		connect = self.initdbconnect()
		cursor = self.initdbcursor(connect)
		try:
			cursor.execute(sql.SQL('''INSERT INTO {} (TITLE, BODY, POST_IMG_LOC, REPO_LINK)
				VALUES (%s, %s, %s, %s);''').format(sql.Identifier(table_name)),
				(title, body, img_loc, repo_link)
			)
			connect.commit()
			connect.close()
			print(f"Table Insert Complete!")
			return
		except ValueError:
			print(f"Post creation error. Either already exist or other. \n{ValueError}")
			connect.commit()
			connect.close()
			pass


	def del_post(self, post_id:int, table_name:str):
		"""
		Use the psycopg2 init function to delete a post from table. If throws error, pass.

		Parameters
		----------
			post_id : int (required)
				An integer object that represents the post id column identifier to be deleted.
			table_name: string (required)
				A String object that indentifies the table for which row should be deleted.
		"""	
		connect = self.initdbconnect()
		cursor = self.initdbcursor(connect)
		if post_id <= 0:
			print(type(post_id))
			print(f"POST_ID {post_id} needs to be greater than 0.")
			return 
		try:
			query = "DELETE FROM " + table_name + " WHERE POST_ID = " + str(post_id) + ";"
			cursor.execute(query)
			connect.commit()
			connect.close()
			print(f"Table Deletion Complete! POST_ID {post_id} removed")
		except ValueError:
			print(f"Post deletion error. Either already exist or other. \n{ValueError}")
			connect.commit()
			connect.close()
			pass


	def clear_table_rows(self, table_name:str):
		"""
		Use the psycopg2 init function to delete a post from table. If throws error, pass.

		Parameters
		----------
			post_id : int (required)
				An integer object that represents the post id column identifier to be deleted.
			table_name: string (required)
				A String object that indentifies the table for which row should be deleted.
		"""	
		connect = self.initdbconnect()
		cursor = self.initdbcursor(connect)
		try:
			query = "DELETE FROM " + table_name + ";"
			cursor.execute(query)
			connect.commit()
			connect.close()
			print(f"Table {table_name} cleared of ALL rows.")
		except ValueError:
			print(f"Table clear error. Either does not exist or other. \n{ValueError}")
			connect.commit()
			connect.close()
			pass



# dbh = DBHandler()
# table_name = 'tech_projects_test_3'
# test_title = 'Building a Flask Web App from Scratch'
# test_body = "To start off the new year in 2022 and my journey into tech, I've decided to begin by creating a portfolio site for me to store all my projects and talk about them, the challanges I faced creating them, and the technologies I explored using them. So to start off, I wanted to make this site almost completely from scratch. So after some research, I landed on using the Python micro framework, Flask, as the backend server for this site, as it is light weight, quick to start, and easy to maintain. Using Flask allows for HTML and CSS to be set up on a Heroku Deployment quickly and with little maintaince. I..."
# test_img_loc = 'static/images/thumbs/website_thumb.png'
# test_repo_link = "https://github.com/Mroussell/mjr_website"
# dbh.add_post(table_name,test_title, test_body, test_img_loc, test_repo_link)
# # dbh.create_table(table_name)
# dbh.inspect_table(table_name)
# # dbh.del_post(1, table_name)

