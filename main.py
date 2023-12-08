from dotenv import load_dotenv
import os
from bot import Bot

load_dotenv()
# load the crediential from the .env file
email = os.getenv("username")  # facebook email address /username
password = os.getenv("password")  # facebook password
ID = os.getenv("ID")  # group id to send the message to 


# creating an instance of class bot
if __name__ == '__main__':
    client = Bot(email, password, ID)
    client.listen()  #loop that continuously checks for new messages