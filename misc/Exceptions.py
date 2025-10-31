import discord

# general hybrid exceptions
def exceptioncore(ctx) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = 'Error executing command.',
      color = discord.Color.dark_red()
   )
   embed.set_footer(
      text = 'Check the error documentation.',
   )
   return embed

def noperms(ctx) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = 'You are not allowed to use this command!',
      color = discord.Color.light_gray()
   )
   return embed

def noamount(ctx) -> discord.Embed:
   embed = discord.Embed(
      title = 'Enter a valid amount.',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = 'The amount must be greater than 0.'
   )
   return embed

def noprefix(ctx) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = 'New prefix cannot be empty.',
      color = discord.Color.light_gray()
   )
   return embed

def lenprefix(ctx) -> discord.Embed:
   embed = discord.Embed(
      title = 'Prefix cannot have more than 4 characters.',
      color = discord.Color.light_gray()
   )
   return embed

# general exceptions
def nocore_(
        interaction: discord.Interaction) -> discord.Embed: # ignore wear warning
   embed = discord.Embed(
      title = "You can't do that!",
      color = discord.Color.dark_red()
   )
   return embed

def permscore_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = 'Noko is not allowed to perform this action.',
      color = discord.color.dark_red()
   )
   embed.set_footer(
      text = 'Check documentation for more information.'
   )
   return embed

def corexcepctions(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = 'Error executing command',
      color = discord.Color.dark_red() # severe
   )
   embed.set_footer(
      text = 'Check the error documentation.'
   )
   return embed

def corerror_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = f'Error.',
      color = discord.Color.dark_red() # severe
   )
   embed.set_footer(
      text = 'Check the error documentation.'
   )
   return embed

# all id exceptions
def noid_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = f'The ID cannot be empty',
      color = discord.Color.light_gray()
   )
   return embed

def errorid_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = 'Invalid ID',
      color = discord.Color.orange() # mid
   )
   return embed

def nullid_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = 'This ID does no exist.',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = 'Make sure the ID is correct.'
   )

# general interaction
def noperms_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = 'You are not allowed to use this command.',
      color = discord.Color.light_gray()
   )
   return embed

def nouser_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = 'You must mention a user.',
      color = discord.Color.light_gray()
   )
   return embed

def norole_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = 'You must mention a role.',
      color = discord.Color.light_gray()
   )
   return embed

def notarget_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = 'Target cannot be empty.',
      color = discord.Color.light_gray()
   )
   return embed

def usrnotfound_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = 'User not found.',
      color = discord.Color.light_gray()
   )
   return embed

def noamount_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = 'Enter a valid amount.',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = 'The amount must be greater than 0.',
   )
   return embed

def noduration_(
        interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Enter a valid duration in minutes.',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = 'Duration must be greater than 0.'
   )
   return embed

def usrtop_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = 'You do not have permissions on this user.',
      color = discord.Color.light_gray()
   )
   return embed

def roletop_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = 'You cannot handle this role.',
      color = discord.color.light_gray()
   )
   return embed

# create role messages
def authmrole_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = 'Hard Mute role not found and was automatically created.',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = 'Check documentation for more information.'
   )
   return embed

def autmrole_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = 'Mute role not found and was automatically created.',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = 'Check documentation for more information.'
   )
   return embed

# severe
def channelerror_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = 'Error modifying channel permissions.',
      color = discord.Color.dark_red()
   )
   embed.set_footer(
      text = 'Check error documentation for more information.'
   )
   return embed

# auth messages
def noauth_(
        interaction: discord.Interaction,
        user: discord.Member) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = 'Authorization required: 401.',
      color = discord.Color.dark_red()
   )
   print(f'z-:'
         f'Authorization failed by:'
         f'{interaction.user.id} in {interaction.guild_id}:'
         f'{interaction.guild.name}'
   )
   return embed

def authexception(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = "Can't verify authorization.",
      color = discord.Color.dark_red()
   )
   return embed

# extension exceptions
def extalreadyload_(
        interaction: discord.Interaction, # ignore weak warning
        extension: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Already loaded: `{extension}`',
      color = discord.Color.light_gray() # change to primary color
   )
   return embed

def extnotload_(
        interaction: discord.Interaction, # ignore weak warning
        extension: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Not loaded: `{extension}`',
      color = discord.Color.light_gray() # change to primary color
   )
   return embed

def extnotfound_(
        interaction: discord.Interaction, # ignore weak warning
        extension: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Not found: `{extension}`',
      color = discord.Color.light_gray() # change to primary color
   )
   return embed