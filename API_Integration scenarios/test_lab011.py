# Env file
# To store the private information or credentials
# pip install python-dotenv

from dotenv import load_dotenv
import os

def test_update_req():
    load_dotenv()
    url= os.getenv("URL") # reads from .env file
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(url)
    print(username)
    print(password)