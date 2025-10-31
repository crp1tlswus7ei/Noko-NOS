import os
import discord # ?
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv as core_load
from misc.Buttons import ForbiddenButton
from misc.Exceptions import *
from misc.Messages import *

# auth
core_load()
PASS = str(
   os.getenv('CORE_AUTH')
)

class Reload(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.docs_button = ForbiddenButton()

   @app_commands.command(
      name = 'reload',
      description = 'Reload a bot extension.',
      nsfw = False
   )
   @app_commands.describe(
      extension = 'Extension name to load.',
      password = 'auth'
   )
   async def reload(
           self,
           interaction: discord.Interaction,
         # user: discord.Member,
           extension: str,
           password: str
   ):
      # permissions
      try:
         if password == PASS:
            pass
         else:
            await interaction.response.send_message(
               embed = noauth_(interaction, user),
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
      except Exception as e:
         print(f'y-reload: (permissions); {e}')

      # primary
      try:
         await self.core.reload_extension(f'cmds.`{extension}`')
         await interaction.response.send_message(
            embed = reload_(interaction, extension),
            ephemeral = True
          # view = self.reload_button
         )

      # handler primary
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
      except Exception as e:
         print(f'y-reload: (primary); {e}')

# Cog
async def setup(core):
   await core.add_cog(Reload(core))