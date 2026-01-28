import discord # ?
from discord import app_commands
from discord.ext import commands
from misc.Buttons import *
from misc.Exceptions import *
from misc.Messages import *

class Unban(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.delete = Delete()
      self.interactionb = InteractionB()
      self.docs = Forbidden()

   @app_commands.command(
      name = 'unban',
      description = 'Remove ban of a user.',
      nsfw = False
   )
   @app_commands.describe(
      user_id = 'ID of the user to remove ban.'
   )
   @app_commands.default_permissions(
      ban_members = True
   )
   async def unban(
           self,
           interaction: discord.Interaction,
           *,
           user_id: str
   ):
      # permissions
      try:
         if interaction.user.id == user_id: #
            await interaction.response.send_message(
               embed = unbanys_(interaction),
               ephemeral = True
            )
            return

         if not interaction.user.guild_permissions.ban_members: #
            await interaction.response.send_message(
               embed = noperms_(interaction),
               ephemeral = True
            )
            return

         if user_id is None: #
            await interaction.response.send_message(
               embed = noid_(interaction),
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
         print(f'a-unban: (permissions); {e}')
         return

      ## secondary
      try:
         user_id = int(user_id)

      ## handler secondary
      except ValueError:
         await interaction.response.send_message(
            embed = errorid_(interaction),
            ephemeral = True
         )
      except discord.Forbidden:
         await interaction.response.send_message(
            embed = corerror_(interaction),
            ephemeral = True,
            view = self.docs
         )
      except Exception as e:
         print(f'b-unban: (secondary); {e}')
         return

      ## primary
      banned_users = interaction.guild.bans()
      try:
         async for ban_entry in banned_users:
            user = ban_entry.user
            if user.id == user_id:
               await interaction.guild.unban(user)
               await interaction.response.send_message(
                  embed = unban_(interaction, user_id),
                  ephemeral = False,
                  view = self.delete
               )
            else:
               await interaction.response.send_message(
                  embed = nullid_(interaction),
                  ephemeral = True
               )
               return

         await interaction.response.send_message(
            embed = usrnotfound_(interaction),
            ephemeral = True
         )
         return

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
         print(f'b-unban (primary); {e}')
         return

# Cog
async def setup(core):
   await core.add_cog(Unban(core))