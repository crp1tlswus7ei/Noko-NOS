import os
import asyncio
import discord
from discord.ext import commands
from pymongo import MongoClient
from dotenv import load_dotenv as load_auth
from systems.SysPrefix import get_prefix

load_auth()
class Shot:
   def __init__(self):
      self.folders = (
         'extensions', 'listeners'
      )
      self.token = os.getenv('CORE_TOKEN')
      self.mongo_uri = os.getenv('MONGO_URI')
      self.shot = MongoClient(self.mongo_uri)
      self.ints = discord.Intents.all() # change
      self.ints.members = True
      self.core = commands.Bot(
         intents = self.ints,
         command_prefix = get_prefix,
         help_command = None,
         strip_after_prefix = True,
         owner_id = 529441009004707840  # crp1tlswus7ei
      )

      # on noko
      @self.core.event
      async def on_ready():
         print(f'Core: Online... as: {self.core.user.display_name}')
         await self.core.change_presence(
            activity = discord.CustomActivity(
               name = 'In maintenance...'
            ),
            status = discord.Status('dnd') # do not disturb while maintenance
          # status = discord.Status('online')
         )
         try:
            sync_ = await self.core.tree.sync()
            print(f'Core: Sync; {len(sync_)} commands.')

         # systems on
         except Exception as e:
            print(f'!!! Core: (on); {e}')

   # connect db
   async def connect_(self):
      try:
         self.shot.admin.command('ping')
         print(f'Core: Database Online.')

      # systems db
      except Exception as e:
         print(f'!!! Core: (connect); {e}')

   # load commands
   async def load_(self): # 24

      # secondary
      try:
         for folder in self.folders:
            path = f'./{folder}'

            if not os.path.isdir(path):
               print(f'Core: folder not found: {folder}')
               continue

            for filename in os.listdir(path):
               if not filename.endswith('.py'):
                  continue

               # primary
               ext_ = f'{folder}.{filename[:-3]}'
               try:
                  await self.core.load_extension(ext_)
               except Exception as e:
                  print(f'!!! Core: (load primary); {e}')

      except Exception as e:
         print(f'!!! Core: (load secondary); {e}')

   # Shot
   async def shot_(self):
      async with self.core:
         await self.load_()
         await self.connect_()
         await self.core.start(self.token)

# run
asyncio.run(Shot().shot_())