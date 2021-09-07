import discord
import ssl

with open("Bot_token.txt") as f:
    token = f.read()
client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.content == 'うー':
        await message.channel.send('にゃー')

client.run(token)