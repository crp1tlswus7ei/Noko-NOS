import discord
from discord.ext import commands
from systems.SysAutoRole import *

class AutoRoleListener(commands.Cog):
   def __init__(self, core):
      self.core = core

   @commands.Cog.listener()
   async def on_member_join(
           self,
           user: discord.Member
   ):
      # primary
      data = await get_role(user.guild.id)
      if not data:
         return

      if not data.get('enabled', False):
         return

      role = user.guild.get_role(data['role_id'])
      if not role:
         return

      if role >= user.guild.me.top_role:
         return

      try:
         await user.add_roles(
            role,
            reason = 'AutoRole by CS'
         )
      except Exception as e:
         print(f'AutoRole: (listener); {e}')

# Cog
async def setup(core):
   await core.add_cog(AutoRoleListener(core))