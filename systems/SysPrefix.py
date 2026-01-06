import os
from discord.ext import commands
from pymongo import MongoClient
from dotenv import load_dotenv as core_load

core_load()
MONGO_URI = os.getenv('MONGO_URI')
shot = MongoClient(MONGO_URI)
db = shot["kiko"]
w_coll = db["prefix"]
default_prefix = '!',
aux_prefix = 'core'

async def get_prefix(
        bot,
        message
):
   if not message.guild:
      command.when_mentioned_or(
         default_prefix,
         aux_prefix,
      )(
         bot,
         message
      )

   data = w_coll.find_one({'_id': message.guild.id})
   if data:
      user_prefix = data['prefix']
   else:
      user_prefix = default_prefix

   return commands.when_mentioned_or(user_prefix, aux_prefix)(bot, message)

async def update_prefix(
        ctx,
        new_prefix
):
   w_coll.update_one(
      {'_id': ctx.guild.id},
      {'$set': {'prefix': new_prefix}},
      upsert = True
   )

async def delete_prefix(ctx):
   w_coll.update_one(
      {"_id": ctx.guild.id},
      {"$set": {"prefix": default_prefix}},
      upsert = True
   )