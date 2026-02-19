import discord # ?
from discord import app_commands
from discord.ext import commands
from misc.Buttons import *
from misc.Exceptions import *
from misc.Messages import *

class Purge(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.delete = Delete()
      self.interactionb = InteractionB()
      self.docs = Forbidden()

   @app_commands.command(
      name = 'purge',
      description = 'Clear all messages from a specific user.',
      nsfw = False
   )
   @app_commands.describe(
      user = 'User to clear messages.'
   )
   @app_commands.default_permissions(
      manage_messages = True,
   )
   async def purge(
           self,
           interaction: discord.Interaction,
           user: discord.Member
   ):
      # permissions
      try:
         if user == self.core.user: #
            await interaction.response.send_message(
               embed = selfpurge_(interaction),
               ephemeral = True
            )
            return

         if interaction.user.id == user.id: #
            await interaction.response.send_message(
               embed = purgeys_(interaction),
               ephemeral = True
            )
            return

         if not interaction.user.guild_permissions.manage_messages: #
            await interaction.response.send_message(
               embed = noperms_(interaction),
               ephemeral = True
            )
            return

         if user is None: #
            await interaction.response.send_message(
               embed = nouser_(interaction),
               ephemeral = True
            )
            return

         if interaction.user.top_role <= user.top_role: #
            await interaction.response.send_message(
               embed = usrtop_(interaction),
               ephemeral = True
            )
            return

      ## handler permissions
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
         print(f'x-purge: (permissions); {e}')
         return

      ## secondary
      def check_usr(msg):
         return msg.author.id == user.id

      # defer for primary
      await interaction.response.send_message(
         embed = loadingpurge_(interaction, user),
         ephemeral = True
      )

      ## primary
      try:
         await interaction.channel.purge(
            limit = 7049,
            check = check_usr,
         )
         await interaction.edit_original_response(
            embed = purge_(interaction, user)
         )

      ## handler primary
      except discord.Forbidden:
         await interaction.followup.send(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.docs
         )
      except discord.InteractionResponded:
         await interaction.followup.send(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.interactionb
         )
      except Exception as e:
         print(f'x-purge: (primary); {e}')
         return

# Cog
async def setup(core):
   await core.add_cog(Purge(core))