"""
MJR
Michael Roussell
Copyright 2022

This file handlers all of the ai blog components for the app. 
As well as the parsing and decision making used to create meaningful blog post.

Python 3.9.7 version of the python interpreter.
If there are any questions, please contact me at 'mjr.dev.contact@gmail.com.

MIT Education License Preferred.
"""
import os
from typing import final
import openai
from dotenv import load_dotenv

class BloggerAI:
    def generate_topics(self, topic:str):
        """
		Use Open AI API functions  and parsing to genreate a weeks worth of topics for blogging.

        Parameter
		---------
			topic : string (required)
				A String object that holds the topic top generate more topics for the blog.

        Returns:
		---------
			post_json: list
				A List of Strings with Topic Ideas for the AI to Blog about.
		"""

        # Gather API Key
        load_dotenv()
        openai.api_key = os.getenv('OPEN_AI_SEC_KEY')

        # Create promt string
        prompt = "Topic in " + topic + "."

        # Generate AI response and begin parsing for topics
        topics = []
        response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=16, n=7, temperature=0.9)
        for r in response["choices"]:
            print(r["text"])
            topics.append(r["text"])

        # Replace unneeded characters
        topics_nnn = {x.replace('\n\n', '') for x in topics}
        parsed_topics = list(set(topics_nnn))

        # For duplicate topics find new ones.
        if len(parsed_topics) == 7:
            final_topics = parsed_topics
        while len(parsed_topics) < 7:
            missing = 7  - len(parsed_topics)
            response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=16, n=1, temperature=0.9)
            possible_topics = response["choices"]["text"]
            topics_nnn = {x.replace('\n\n', '') for x in possible_topics}
            final_topics =  list(set(parsed_topics + list(set(topics_nnn))))

        return final_topics

    def generate_post(self, topic:str):
        """
		Use Open AI API functions and parsing to genreate a post from a genreated topic for blogging.

        Parameter
		---------
			topic : str (required)
				A String object that holds the topic top generate more topics for the blog.

        Returns:
		---------
			post_json: str
				A Json String of Strings with Post information for the AI to post onto website page.
		"""

        # Gather API Key
        load_dotenv()
        openai.api_key = os.getenv('OPEN_AI_SEC_KEY')

        # Generate Post AI Intro 
        prompt = "What is " + topic + "?" 
        post = ""
        response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=280, n=1, temperature=0.8)
        intro_paragraph = response["choices"][0]["text"]

        # Generate AI Post Meat
        prompt = "White an in depth paragraph about " + topic + "."
        response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=280, n=1, temperature=0.8)
        explain_paragraph = response["choices"][0]["text"]
        
        # Generate Future Paragraph for Conclusion.
        prompt = "The future of " + topic + "."
        response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=280, n=1, temperature=0.8)
        end_paragraph = response["choices"][0]["text"]
        
        post = intro_paragraph + "\n" + explain_paragraph + "\n\n" + end_paragraph + "\n\n - MJR's Friendly AI"
        return post


bai = BloggerAI()
possilbe_post_body = bai.generate_post("IoT")
print(possilbe_post_body)