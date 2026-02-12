import discord
from discord.ui import View, Button
from misc.Exceptions import *

# advice
class Advice(discord.ui.View):
   def __init__(
           self,
           interaction: discord.Interaction
   ):
      super().__init__(timeout = 49)
      self.interaction = interaction
      self.confirmed = False

   @discord.ui.button(
      emoji = '<:white_check:1470874033863262220>',
      style = discord.ButtonStyle.green,
   )
   async def accept_(
           self,
           interaction: discord.Interaction,
           button: discord.ui.Button
   ):
      self.confirmed = True
      await interaction.response.defer()
      self.stop()

   @discord.ui.button(
      emoji = '<:white_cross:1405656979266867210>',
      style = discord.ButtonStyle.red
   )
   async def denied_(
           self,
           interaction: discord.Interaction,
           button: discord.ui.Button
   ):
      await interaction.response.defer()
      self.stop()

# delete/dimiss
class Delete(View):
   def __init__(self):
      super().__init__(timeout = 49)

      delete_button = Button(
         emoji = '<:white_cross:1405656979266867210>',
         style = discord.ButtonStyle.danger, # ignore warn
      )
      delete_button.callback = self.delete_message
      self.add_item(delete_button)

   async def delete_message( # ignore warn
           self,
           interaction: discord.Interaction
   ):
      if interaction.user != interaction.message.interaction.user:
         await interaction.response.send_message(
            embed = intresponse_(interaction),
            ephemeral = True
         )
         return

      # primary
      await interaction.response.defer()
      await interaction.message.delete()

# Docs
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