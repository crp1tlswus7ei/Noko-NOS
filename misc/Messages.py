import discord

# default customizable embed
def embed_(
        interaction: discord.Interaction, # ignore weak warning
        title: str) -> discord.Embed:
   embed = discord.Embed(
      title = title,
      color = discord.Color.light_gray() # change to primary color
   )
   return embed

# prefix messages
def setprefix_(
        ctx,
        new_prefix: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'New Prefix: {new_prefix}',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'Prefix update by: {ctx.author.display_name}',
      icon_url = ctx.author.avatar
   )
   return embed

# Ban messages
def ban_(
        interaction: discord.Interaction,
        user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'Ban: {user.display_name}',
      description = f'**id:** {user.id}',
      color = discord.Color.light_gray() # change later to primary color
   )
   embed.set_footer(
      text = f'Ban by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def banys_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = "You can't ban yourself.",
      color = discord.Color.light_gray()
   )
   return embed

# Softban messages
def softban_(
        interaction: discord.Interaction, # ignore weak warning
        user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'Soft-ban: {user.display_name}',
      description = f'**id:** {user.id}',
      color = discord.Color.light_gray() # change to primary color
   )
   embed.set_footer(
      text = f'Soft-ban by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

# Unban messages
def unban_(
        interaction: discord.Interaction,
        user_id: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Unban: {user_id}',
      color = discord.Color.light_gray() # change to primary color
   )
   embed.set_footer(
      text = f'Unban by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def unbanys_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = "You can't unban yourself.",
      color = discord.Color.light_gray()
   )
   return embed

# Kick messages
def kick_(
        interaction: discord.Interaction,
        user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'Kick: {user.display_name}',
      description = f'**id:** {user.id}',
      color = discord.Color.light_gray() # change to primary color
   )
   embed.set_footer(
      text = f'Kick by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def kickys_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = "You can't kick yourself.",
      color = discord.Color.light_gray()
   )
   return embed

# Clear Warns messages
def clearw_(
        interaction: discord.Interaction,
        user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} warns cleaned',
      color = discord.Color.light_gray() # change to primary color
   )
   embed.set_footer(
      text = f'Clean by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def clearys_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = "You can't remove your own warns.",
      color = discord.Color.light_gray()
   )
   return embed

def nowarns_(
        interaction: discord.Interaction, # ignore weak warning
        user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} has no warns to clean.',
      color = discord.Color.light_gray()
   )
   return embed

# Unwarn messages
def unwarn_(
        interaction: discord.Interaction, # ignore weak warning
        user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} warn(s) removed.',
      color = discord.Color.light_gray() # change to primary color
   )
   # footer in primary
   return embed

def nullwarn_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = 'Invalid warn.',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = 'Enter a valid amount.'
   )
   return embed

# Warn messages
def warn_(
        interaction: discord.Interaction,
        total_warns: int) -> discord.Embed:
   embed = discord.Embed(
      title = f'{interaction.user.display_name} has been warned.',
      description = f'**Warns:** {total_warns}',
      color = discord.Color.light_gray() # change to primary color
   )
   embed.set_footer(
      text = f'Warn by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def warnys_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = "You can't warn yourself.",
      color = discord.Color.light_gray()
   )
   return embed

# Warnings message list
def warnings_(
        interaction: discord.Interaction,
        title: str) -> discord.Embed:
   embed = discord.Embed(
      title = title,
      color = discord.Color.light_gray() # change to primary color
   )
   embed.set_footer(
      text = f'List requested by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def nowarnings_ (
        interaction: discord.Interaction, # ignore weak warning
        user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} has no warnings.',
      color = discord.Color.light_gray()
   )
   return embed

# Hardmute messages
def hardmute_(
        interaction: discord.Interaction,
        user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'Hard Mute: {user.display_name}',
      color = discord.Color.light_gray() # cuamge to primary color
   )
   embed.set_footer(
      text = f'Mute by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def hardmuteys_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = "You can't mute yourself.",
      color = discord.Color.light_gray()
   )
   return embed

def alrmute_(
        interaction: discord.Interaction, # ignore weak warning
        user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} already muted.',
      color = discord.Color.light_gray()
   )
   return embed

# Mute messages
def mute_(
        interaction: discord.Interaction,
        user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'Mute: {user.display_name}',
      color = discord.Color.light_gray() # change to primary color
   )
   embed.set_footer(
      text = f'Mute by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

# Unmute messages
def unmute_(
        interaction: discord.Interaction,
        user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'Unmute: {user.display_name}',
      color = discord.Color.light_gray() # change to primary color
   )
   embed.set_footer(
      text = f'Unmute by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def unmuteys_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = "You can't unmute yourself.",
      color = discord.Color.light_gray()
   )
   return embed

def nomute_(
        interaction: discord.Interaction, # ignore weak warning
        user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} is not muted.',
      color = discord.Color.light_gray()
   )
   return embed

# timeout message
def timeout_(
        interaction: discord.Interaction,
        user: discord.Member,
        duration: int) -> discord.Embed:
   embed = discord.Embed(
      title = f'Timeout: {user.display_name}',
      description = f'**Duration:** {duration} minutes.',
      color = discord.Color.light_gray() # change to primary color
   )
   embed.set_footer(
      text = f'Timeout by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

# un-timeout message
def untimeout_(
        interaction: discord.Interaction,
        user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'Untimeout: {user.display_name}',
      color = discord.Color.light_gray() # change to primary color
   )
   embed.set_footer(
      text = f'Untimeout by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

# lockdown message
def lockdown_(
        interaction: discord.Interaction,
        user: discord.Member, # ignore weak warning
        channel: discord.TextChannel) -> discord.Embed:
   embed = discord.Embed(
      title = f'Lock: {channel.mention}',
      color = discord.Color.light_gray() # change to primary color
   )
   embed.set_footer(
      text = f'Lock by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

# unlockdown message
def unlockdown_(
        interaction: discord.Interaction,
        user: discord.Member, # ignore weak warning
        channel: discord.TextChannel) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = f'Unlock: {channel.mention}',
      color = discord.Color.light_gray() # change to primary color
   )
   embed.set_footer(
      text = f'Unlock by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

# clear message
def clear_( # interaction
        interaction: discord.Interaction,
        user: discord.Member, # ignore weak warning
        amount: int) -> discord.Embed:
   embed = discord.Embed(
      title = f'{amount} messages deleted.',
      color = discord.Color.light_gray() # change to primary color
   )
   embed.set_footer(
      text = f'Clear by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def clear( # context
        ctx,
        amount: int) -> discord.Embed:
   embed = discord.Embed(
      title = f'{amount} messages deleted.',
      color = discord.Color.light_gray() # change to primary color
   )
   embed.set_footer(
      text = f'Clear by: {ctx.author.display_name}',
      icon_url = ctx.author.avatar
   )
   return embed

# purge messages
def purge_(
        interaction: discord.Interaction,
        user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f"{user.display_name}'s messages cleared.",
      color = discord.Color.light_gray() # change to primary color
   )
   embed.set_footer(
      text = f'Purge by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def purgeys_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
   embed = discord.Embed(
      title = "You can't clear your own messages.",
      color = discord.Color.light_gray()
   )
   return embed

# massrole messages
def inprocessrole_(
        interaction: discord.Interaction) -> discord.Embed: # ignore weak warning
    embed = discord.Embed(
        title = 'MassRole: in process...',
        color = discord.Color.light_gray()
    )
    return embed

def massrole_(
        interaction: discord.Interaction, # ignore weak warning
        role: discord.Role) -> discord.Embed:
    embed = discord.Embed(
        title = f'MassRole: {role}',
        color = discord.Color.dark_green()
    )
    return embed

# load message
def load_(
        interaction: discord.Interaction,
        extension: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Load: `{extension}`',
      color = discord.Color.light_gray() # change to primary color
   )
   print(f'z-load:'
         f'New Load by:'
         f'{interaction.user.id}: {interaction.user.display_name} in:'
         f'{interaction.guild.name}'
         )
   return embed

# reload message
def reload_(
        interaction: discord.Interaction,
        extension: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Reload: `{extension}`',
      color = discord.Color.light_gray() # change to primary color
   )
   print(f'z-reload:'
         f'New Load by:'
         f'{interaction.user.id}: {interaction.user.display_name} in:'
         f'{interaction.guild.name}'
   )
   return embed

# unload message
def unload_(
        interaction: discord.Interaction,
        extension: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Unload: `{extension}`',
      color = discord.Color.light_gray() # change to primary color
   )
   print(f'z-reload:'
         f'New Load by:'
         f'{interaction.user.id}: {interaction.user.display_name} in:'
         f'{interaction.guild.name}'
   )
   return embed