import os
import discord # ?
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv as core_load
from misc.Buttons import *
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
      self.interactionb = InteractionB()
      self.docs = Forbidden()

   @app_commands.command(
      name = 'load',
      description = 'Load new Bot extension.',
      nsfw = False
   )
   @app_commands.describe(
      extension = 'Extension name to load.',
      password = 'auth'
   )
   @app_commands.default_permissions(
      administrator = True
   )
   async def load(
           self,
           interaction: discord.Interaction,
           extension: str,
           password: str
   ):
      # permissions
      try:
         if password == PASS:
            pass
         else:
            await interaction.response.send_message(
               embed = noauth_(interaction), # ignore unfilled
               ephemeral = True
            )
            return

      # handler permissions
      except discord.Forbidden:
         await interaction.response.send_message(
            embed = authexception(interaction),
            ephemeral = True,
            view = self.docs
         )
      except discord.InteractionResponded:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.interactionb
         )
      except Exception as e:
         print(f'y-load: (permissions); {e}')
         return

      # primary
      try:
         await self.core.load_extension(f'extensions.`{extension}`')
         await interaction.response.send_message(
            embed = load_(interaction, extension),
            ephemeral = True
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
      except discord.Forbidden:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.docs
         )
      except discord.InteractionResponded:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.interactionb
         )
      except Exception as e:
         print(f'y-load: (primary); {e}')
         return

# Cog
async def setup(core):
   await core.add_cog(Load(core))