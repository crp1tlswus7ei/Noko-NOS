import os
from discord.ext import commands
from pymongo import MongoClient
from dotenv import load_dotenv as core_load

core_load()
MONGO_URI = os.getenv('MONGO_URI')
shot = MongoClient(MONGO_URI)
db = shot['kiko']
w_coll = db['prefix']
DEFAULT_PREFIX = '!'
AUX_PREFIX = 'core'

async def get_prefix(
        bot,
        message
):
   if not message.guild:
      commands.when_mentioned_or(
         DEFAULT_PREFIX,
         AUX_PREFIX,
      )(
         bot,
         message
      )

   data = w_coll.find_one({'_id': message.guild.id})
   custom_ = None
   if data:
      custom_ = data.get('prefix')

   prefixes = [DEFAULT_PREFIX, AUX_PREFIX]
   if custom_:
      prefixes.insert(0, custom_)

   return commands.when_mentioned_or(*prefixes)(bot, message)

async def getactual_prefix(guild_id: int):
   prefix = w_coll.find_one(
      {'_id': guild_id}
   )
   return prefix['prefix']

async def update_prefix(
        ctx,
        new_prefix
):
   w_coll.update_one(
      {'_id': ctx.guild.id},
      {'$set': {'prefix': new_prefix}},
      upsert = True
   )

async def reset_prefix(ctx):
   w_coll.update_one(
      {'_id': ctx.guild.id},
      {'$set': {'prefix': DEFAULT_PREFIX}},
      upsert = True
   )