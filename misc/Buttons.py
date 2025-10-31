import discord
from discord.ui import View, Button

class ForbiddenButton(discord.ui.View):
   def __init__(self):
      super().__init__()
      self.add_item(
         discord.ui.Button(
            label = 'Documentation',
            url = 'https://discordpy.readthedocs.io/en/stable/api.html?highlight=discord%20forbidden#discord.Forbidden'
         )
      )

class PermissionsButton(discord.ui.View):
   def __init__(self):
      super().__init__()
      self.add_item(
         discord.ui.Button(
            label = 'Documentation',
            url = '' # add url
         )
      )