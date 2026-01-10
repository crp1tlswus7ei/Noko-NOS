import os
from datetime import datetime
from pymongo import MongoClient
from dotenv import load_dotenv as core_load

core_load()
MONGO_URI = os.getenv('MONGO_URI')
shot = MongoClient(MONGO_URI)
db = shot['kiko']
w_coll = db['handler']

async def logsave_(
        self, # ignore weak
        log_type: str,
        message: str,
):
   w_coll.insert_one({
      'type': log_type,
      'message': message,
      'timestap': datetime.now(),
   })

async def getlogs_(limit = 10):
   cursor = w_coll.find().sort(
      'timestamp',
      -1
   ).limit(limit)

   return [log async for log in cursor]

async def clear_logs():
   w_coll.delete_many({}) # all clean