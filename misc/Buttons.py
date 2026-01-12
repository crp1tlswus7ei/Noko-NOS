import discord
from discord.ui import View, Button
from misc.Exceptions import *

class Delete(View):
   def __init__(self):
      super().__init__(timeout = None)

      delete_button = Button(
         emoji = '<:white_cross:1405656979266867210>',
         style = discord.ButtonStyle.danger, # ignore warn
      )
      delete_button.callback = self.delete_message
      self.add_item(delete_button)

   async def callback_delete( # ignore warn
           self,
           interaction: discord.Interaction
   ):
      if interaction.user != interaction.message.interaction.user:
         await interaction.response.send_message(
            embed = intresponse_(interaction),
            ephemeral = True
         )
         return

      await interaction.message.delete()

class Forbidden(discord.ui.View):
   def __init__(self):
      super().__init__()
      self.add_item(
         discord.ui.Button(
            label = 'Documentation',
            url = 'https://discordpy.readthedocs.io/en/stable/api.html?highlight=discord%20forbidden#discord.Forbidden'
         )
      )

class InteractionB(discord.ui.View):
   def __init__(self):
      super().__init__()
      self.add_item(
         discord.ui.Button(
            label = 'Documentation',
            url = 'https://discordpy.readthedocs.io/en/stable/api.html#discord.InteractionResponded'
         )
      )