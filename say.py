import discord
import ssl
token = "ODYwODg5NzcxOTY2MzMyOTM4.YOB0FA.M9ylkrXcmu8G_EsUNLIGpSvDBY0"
client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.content == 'うー':
        await message.channel.send('にゃー')

client.run(token)