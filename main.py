from dotenv import load_dotenv
import os
from bot import Bot
from fbchat.models import *

load_dotenv()
# load the crediential from the .env file
email = os.getenv("username")  # facebook email address /username
password = os.getenv("password")  # facebook password
ID = os.getenv("ID")  # group id to send the message to 
thread_type = ThreadType.USER

cookies = {
    "sb": "PdweZYhofWyHE5czZMN3_hUV",
    "fr":"KBplOOgwTESkb9O8.AWUpYDmFSFu4kW8AZKVQdOS8nbA.BldIff.EM.AAA.0.0.BldIff.AWVjMEwC6Pc",
    "c_user":"100083123186881",
    "datr": "PdweZT7Gx2OiK98sDutqrcJV",
    "xs": "4%3A9LdbLYldUQ06aQ%3A2%3A1702135760%3A-1%3A3041%3A%3AAcXggnem4xYFGT4ZSF-XQ51Ll0z5aHVLIaX1VeQa_g"
}

# creating an instance of class bot
if __name__ == '__main__':
       client = Bot(email, password, ID,thread_type,cookies)
       print(client.isLoggedIn())
       #client.listen()  #loop that continuously checks for new messages
       try:
           client.listen()
       except Exception as arr:
           print(arr)
    