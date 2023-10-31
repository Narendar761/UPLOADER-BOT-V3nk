# (c) @AbirHasan2005

from plugins.config import Config
from .database import db
from pyrogram import Client
from pyrogram.types import Message
from pymongo import MongoClient

# Replace 'localhost' with the hostname or IP address of your MongoDB server.
# Replace 27017 with the port number of your MongoDB server if it's not the default.
client = MongoClient('localhost', 27017)



async def add_user_to_database(bot: Client, cmd: Message):
    if not await db.is_user_exist(cmd.from_user.id):
        await db.add_user(cmd.from_user.id)
        


