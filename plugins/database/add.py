# (c) @AbirHasan2005

from plugins.config import Config
from .database import db
from pyrogram import Client
from pyrogram.types import Message

db = connection.test
things = db.things
item  = things.find_one()

print (item['name'])


async def add_user_to_database(bot: Client, cmd: Message):
    if not await db.is_user_exist(cmd.from_user.id):
        await db.add_user(cmd.from_user.id)
        


