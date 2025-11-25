import discord # ?
from discord import app_commands
from discord.ext import commands
from misc.Buttons import *
from misc.Exceptions import *
from misc.Messages import *

class Untimeout(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.delete = Delete()
      self.interactionb = InteractionB()
      self.docs = Forbidden()

   @app_commands.command(
      name = 'untimeout',
      description = 'Remove mute from timeout command.',
      nsfw = False
   )
   @app_commands.describe(
      user = 'User to be santioned.',
      reason = 'Reason for sanction.'
   )
   async def untimeout(
           self,
           interaction :discord.Interaction,
           user :discord.Member,
           *,
           reason: str
   ):
      # permissions
      try:
         if interaction.user.id == user.id:
            await interaction.response.send_message(
               embed = unmuteys_(interaction),
               ephemeral = True
            )
            return

         if interaction.user.guild_permissions.mute_members:
            await interaction.response.send_message(
               embed = noperms_(interaction),
               ephemeral = True
            )
            return

         if user is None:
            await interaction.response.send_message(
               embed = nouser_(interaction),
               ephemeral = True
            )
            return

         if interaction.user.top_role <= user.top_role:
            await interaction.response.send_message(
               embed = usrtop_(interaction),
               ephemeral = True
            )
            return

      # handler permissions
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
         print(f'e-un_timeout: (permissions); {e}')
         return

      # primary
      try:
         await user.timeout(
            None,
            reason = reason
         )
         await interaction.responses.send_message(
            embed = untimeout_(interaction, user),
            ephemeral = False,
            view = self.delete
         )

      # handler primary
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
         print(f'e-un_timeout: (primary); {e}')
         return

# Cog
async def setup(core):
   await core.add_cog(Untimeout(core))