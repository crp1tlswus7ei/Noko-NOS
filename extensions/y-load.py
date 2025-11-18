import os
import discord # ?
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv as core_load
from misc.Buttons import ForbiddenButton, InteractionButton
from misc.Exceptions import *
from misc.Messages import *

# auth
core_load()
PASS = str(
   os.getenv('CORE_AUTH')
)

class Load(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.int_button = InteractionButton()
      self.docs_button = ForbiddenButton()

   @app_commands.command(
      name = 'load',
      description = 'Load new Bot extension.',
      nsfw = False
   )
   @app_commands.describe(
      extension = 'Extension name to load.',
      password = 'auth'
   )
   async def load(
           self,
           interaction: discord.Interaction,
           user: discord.Member,
           extension: str,
           password: str
   ):
      # permissions
      try:
         if password == PASS:
            pass
         else:
            await interaction.response.send_message(
               embed = noauth_(interaction, user), # ignore unfilled
               ephemeral = True
            )
            return

      # handler permissions
      except discord.Forbidden:
         await interaction.response.send_message(
            embed = authexception(interaction),
            ephemeral = True,
            view = self.docs_button
         )
      except discord.InteractionResponded:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.int_button
         )
      except Exception as e:
         print(f'y-load: (permissions); {e}')
         return

      # primary
      try:
         await self.core.load_extension(f'cmds.`{extension}`')
         await interaction.response.send_message(
            embed = load_(interaction, extension),
            ephemeral = True
          # view = self.reload_button
         )

      #handler primary
      except commands.ExtensionAlreadyLoaded:
         await interaction.response.send_message(
            embed = extalreadyload_(interaction, extension),
            ephemeral = True
         )
      except commands.ExtensionNotFound:
         await interaction.response.send_message(
            embed = extnotfound_(interaction, extension),
            ephemeral = True
         )
      except commands.ExtensionNotLoaded:
         await interaction.response.send_message(
            embed = extnotload_(interaction, extension),
            ephemeral = True
         )
      except discord.InteractionResponded:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.int_button
         )
      except Exception as e:
         print(f'y-load: (primary); {e}')
         return

# Cog
async def setup(core):
   await core.add_cog(Load(core))