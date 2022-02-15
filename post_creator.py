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
from dotenv import load_dotenv
from dbhandler import DBHandler

# Use all text files in new post directory to create new post.
os.chdir(".new_posts")
post_json_files  = []
for file in glob.glob("*.txt"):
	with open(file) as tf:
		file_json = json.load(tf)
		post_json_files.append(file_json)

dbh = DBHandler()
for post in post_json_files:
	title = post['title']
	body = post['body']
	img_loc = post['post_img_loc']
	dbh.add_post(title, body, img_loc)
	print(f"Added post with title: {title}")

