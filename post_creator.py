"""
MJR
Michael Roussell
Copyright 2022

New Blog Post Script. Adds post 

Python 3.9.7 version of the python interpreter.
If there are any questions, please contact me at 'mjr.dev.contact@gmail.com.

MIT Education License Preferred.
"""
import os
import json
import glob
import sys
from dotenv import load_dotenv
from dbhandler import DBHandler


# Check for empty directory
dir = os.listdir(".new_posts")
if len(dir) <= 0:
	print("No files to add. Please add new post in correct format to the .new_posts directory. \nExiting!")
	quit()


# Use all text files in new post directory to create new post.
os.chdir(".new_posts")
post_json_files  = []
for file in glob.glob("*.txt"):
	with open(file) as tf:
		file_json = json.load(tf)
		post_json_files.append(file_json)

# Gather table name input
table_name = input("Give Table Name for Post Add, \nEither 'tech_projects_live' or 'data_projects_live':")


# Post are added in proper json form
dbh = DBHandler()
for post in post_json_files:
	title = post['title']
	body = post['body']
	img_loc = post['post_img_loc']
	repo_link = post['repo_link']
	dbh.add_post(table_name,title, body, img_loc, repo_link)
	print(f"Added post with title: {title}")

# If added argument for clear directory
if len(sys.argv) > 1 and sys.argv[1] == '-c':
	print("Clearing posts from local directory: ~~~~~")
	# Delete added posts from local directory.
	for file in glob.glob("*.txt"):
		os.remove(file)
		print(f"Removed post file: {file}")
else: 
	print("Post NOT cleared from local directory. WARNING!!! Please Clear Manually.")


print("Added post to database. Exit 0.")