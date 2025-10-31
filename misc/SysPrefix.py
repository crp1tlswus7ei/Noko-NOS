import os
from pymongo import MongoClient

MONGO_URI = os.getenv('MONGO_URI')
shot = MongoClient(MONGO_URI)
db = shot["kiko"]
w_coll = db["prefix"]

async def get_prefix(self, bot, message):
   if not message.guild:
      return '!!' # default

   data = w_coll.find_one(
      {'_id': message.guild.id}
   )
   if data:
      return data['prefix']
   else:
      return '!!' # default

async def update_prefix(self, ctx, new_prefix):
   w_coll.update_one(
      {'_id': ctx.guild.id},
      {'$set': {'prefix': new_prefix}},
      upsert = True
   )