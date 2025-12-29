import os
from pymongo import MongoClient
from dotenv import load_dotenv as core_load

core_load()
MONGO_URI = os.getenv('MONGO_URI')
shot = MongoClient(MONGO_URI)
db = shot["kiko"]
w_coll = db["auto_roles"]

async def set_role(
        guild_id: int,
        role_id: int
):
   w_coll.update_one(
      {'_id': guild_id},
      {'$set': {
         'role_id': role_id,
         'enabled': True
      }},
      upsert = True
   )

async def toggle(
        guild_id: int,
        state: bool
):
   w_coll.update_one(
      {'_id': guild_id},
      {'$set': {'enabled': state}}
   )

async def get_role(guild_id: int):
   return w_coll.find_one(
      {'_id': guild_id}
   )

async def del_role(guild_id: int):
   w_coll.delete_one(
      {'_id': guild_id}
   )