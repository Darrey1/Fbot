
from fbchat import *
from fbchat.models import *
from message import *
from time import sleep
import random, re


# create class object for the bot 
class Bot(Client):   #inherit the base class Client from the fbchat
    def __init__(self, email, password, thread_id):
        super().__init__(email, password)
        self.thread_id = thread_id
        
        
    def onMessage(self, author_id, message_object, thread_id, thread_type,**kwargs):
         if author_id != self.uid:
             if (message_object.text.lower() == "is this still available?"):
                sleep(random.randrange(5,15))
                self.markAsDelivered(thread_id, message_object.uid)
                self.markAsRead(thread_id)
                self.setTypingStatus(TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type)
                sleep(random.randrange(10,25))
                self.send(Message(text=default_message), thread_id=thread_id, thread_type=thread_type)
             if message_object.text.find('how much') >= 0:
                    sleep(random.randrange(5,15))
                    self.markAsDelivered(thread_id, message_object.uid)
                    self.markAsRead(thread_id)
                    self.setTypingStatus(TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type)
                    sleep(random.randrange(10,25))
                    self.send(Message(text=deliver_message), thread_id=thread_id, thread_type=thread_type)
                    
             if (message_object.text.find('condition') >= 0) or (message_object.text.find('state') >= 0):
                    sleep(random.randrange(5,15))
                    self.markAsDelivered(thread_id, message_object.uid)
                    self.markAsRead(thread_id)
                    self.setTypingStatus(TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type)
                    sleep(random.randrange(10,20))
                    self.send(Message(text=status_message), thread_id=thread_id, thread_type=thread_type)
                    
             if (message_object.text.find('address') >= 0):
                    sleep(random.randrange(5,15))
                    self.markAsDelivered(thread_id, message_object.uid)
                    self.markAsRead(thread_id)
                    self.setTypingStatus(TypingStatus.TYPING, thread_id=thread_id, thread_type=thread_type)
                    sleep(random.randrange(10,20))
                    self.send(Message(text=shop_adress_message), thread_id=thread_id, thread_type=thread_type)
             if message_object.text.lower() == "ok":
                sleep(random.randrange(5,15))
                self.markAsDelivered(thread_id, message_object.uid)
                self.markAsRead(thread_id)
                self.reactToMessage(message_object.uid, MessageReaction.YES)
    
                  