import discord # ?
from misc.Exceptions import *

# advice
class Advice(discord.ui.View):
   def __init__(
           self,
           interaction: discord.Interaction
   ):
      super().__init__(timeout = 49)
      self.author_ = interaction.user.id
      self.interaction = interaction
      self.confirmed = False

   async def interaction_check(
           self,
           interaction: discord.Interaction) -> bool:

      if interaction.user.id != self.author_:
         await interaction.response.send_message(
            embed = menuexception_(interaction),
            ephemeral = True
         )
         return False
      return True

   # Accept
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

   # Denied
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

# delete
class Delete(discord.ui.View):
   def __init__(self):
      super().__init__(timeout = 49)

   @discord.ui.button(
      emoji = '<:white_cross:1405656979266867210>',
      style = discord.ButtonStyle.red
   )
   async def delete_(
           self,
           interaction: discord.Interaction,
           button: discord.Button
   ):
      if interaction.user != interaction.message.interaction.user:
         await interaction.response.send_message(
            embed = menuexception_(interaction),
            ephemeral = True
         )
         return

      await interaction.response.defer()
      await interaction.message.delete()
      self.stop()

# delete ctx
class DeleteCtx(discord.ui.View):
   def __init__(
           self,
           author: discord.User
   ):
      super().__init__(timeout = 49)
      self.author = author

   @discord.ui.button(
      emoji = '<:white_cross:1405656979266867210>',
      style = discord.ButtonStyle.red
   )
   async def deletectx_(
           self,
           interaction: discord.Interaction,
           button: discord.Button
   ):
      if interaction.user != self.author:
         await interaction.response.send_message(
            embed = menuexception_(interaction),
            ephemeral = True
         )
         return

      await interaction.response.defer()
      await interaction.message.delete()
      self.stop()

# Docs
class Forbidden(discord.ui.View):
   def __init__(self):
      super().__init__(timeout = None)
      self.add_item(
         discord.ui.Button(
            label = 'Documentation',
            url = 'https://discordpy.readthedocs.io/en/stable/api.html?highlight=discord%20forbidden#discord.Forbidden'
         )
      )

class InteractionB(discord.ui.View):
   def __init__(self):
      super().__init__(timeout = None)
      self.add_item(
         discord.ui.Button(
            label = 'Documentation',
            url = 'https://discordpy.readthedocs.io/en/stable/api.html#discord.InteractionResponded'
         )
      )