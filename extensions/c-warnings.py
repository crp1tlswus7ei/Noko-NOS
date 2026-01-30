import discord # ?
from discord import app_commands
from discord.ext import commands
from misc.Buttons import *
from misc.Exceptions import *
from misc.Messages import *

class Warnings(commands.Cog):
   from systems.SysWarn import get_warns
   def __init__(self, core):
      self.core = core
      self.delete = Delete()
      self.interactionb = InteractionB()
      self.docs = Forbidden()

   @app_commands.command(
      name = 'warnings',
      description = 'List of user warnings.',
      nsfw = False
   )
   @app_commands.describe(
      user = 'User to review warnings.'
   )
   @app_commands.default_permissions(
      manage_roles = True
   )
   async def warnings(
           self,
           interaction: discord.Interaction,
           user: discord.Member = None
   ):
      # permissions
      user = user or interaction.user
      try:
         if user == self.core.user: #
            await interaction.response.send_message(
               embed = selfwarns_(interaction),
               ephemeral = True
            )

         if not interaction.user.guild_permissions.manage_roles: #
            await interaction.response.send_message(
               embed = noperms_(interaction),
               ephemeral = True
            )
            return

         if user is None: # ?
            pass

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
         print(f'c-warnings: (permissions); {e}')
         return

      ## primary
      user_id = str(user.id)
      try:
         user_warns = self.get_warns(user_id) # ignore unfilled
         if user_warns:
            await interaction.response.send_message(
               embed = warnings_(
                  interaction,
                  title = f'{user.display_name} warns:',
                  description = '\n' + '\n'.join(user_warns),
               ),
               ephemeral = False,
               view = self.delete
            )
         else:
            await interaction.response.send_message(
               embed = nowarnings_(interaction, user),
               ephemeral = False
            )

      ## handler primary
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
         print(f'c-warnings: (primary); {e}')
         return

# Cog
async def setup(core):
   await core.add_cog(Warnings(core))