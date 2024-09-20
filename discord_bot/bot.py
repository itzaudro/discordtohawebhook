import discord
from discord.ext import commands
import requests

# Set up the bot
bot = commands.Bot(command_prefix='/', intents=discord.Intents.default())

# Define the role name that is allowed to use the command
ALLOWED_ROLE_NAME = 'YourRoleName'

# Define the webhook URL
WEBHOOK_URL = 'https://your-home-assistant-server/webhook-url'

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def plexsync(ctx):
    # Check if the user has the required role
    if any(role.name == ALLOWED_ROLE_NAME for role in ctx.author.roles):
        # Call the webhook
        response = requests.post(WEBHOOK_URL)

        # Check response status
        if response.status_code == 200:
            await ctx.send('Plex sync command executed successfully!')
        else:
            await ctx.send('Failed to execute Plex sync command.')
    else:
        await ctx.send('You do not have the required role to use this command.')

# Run the bot
bot.run('YOUR_BOT_TOKEN')
