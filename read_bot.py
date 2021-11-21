import discord
from discord import channel
from discord.ext import commands
from discord.utils import get
import subprocess
import ffmpeg
import time
from voice_generator import creat_WAV, creat_WAV_2

client = commands.Bot(command_prefix='!!')
voice_client = None

with open("Bot_token.txt") as f:
    token = f.read()

with open("channel_id_mentaiko.txt") as f:
    CHANNEL_ID = f.read()

with open("vchannnel_id_mentaiko.txt") as f:
    VCHA_ID = f.read()
CHANNEL_ID = int(CHANNEL_ID)
VCHA_ID = int(VCHA_ID)

default_voice = 1

@client.event
async def on_ready():
    chanel = client.get_channel(CHANNEL_ID)
    vcha = client.get_channel(VCHA_ID)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    #await chanel.send('こんにちは！')
    await vcha.connect()



@client.command()
async def join(ctx):
    #voicechannelを取得
    vc = ctx.author.voice.channel
    #voicechannelに接続
    await vc.connect()

@client.command()
async def bye(ctx):
    #切断
    await ctx.voice_client.disconnect()

@client.event
async def on_message(message):
    global default_voice
    if message.content == '.join':
        vcha = client.get_channel(VCHA_ID)
        await vcha.connect()
    if message.content == '.punish':
        voice_client2 = message.guild.voice_client
        #vcha = client.get_channel(VCHA_ID)
        await message.guild.voice_client.disconnect()
        exit()
    if message.content.startswith('%'):
        pass

    elif message.content == '.change':
        if default_voice == 1:
            default_voice = 2
        else:
            default_voice = 1
    elif message.content[0:4] == 'http':
        if default_voice == 1:
            creat_WAV('ゆーあーるえる')
        else :
            creat_WAV_2('ゆーあーるえる')
        source = discord.FFmpegPCMAudio("output.wav")
        message.guild.voice_client.play(source)
    
    elif message.content == ".mute":
        if message.author.guild_permissions.administrator:
            bot_vc = message.guild.me.voice.channel
            for member in bot_vc.members:
                await member.edit(mute=True)
        else:
            await message.channel.send("実行できません。")
    elif message.content == ".unmute":
        if message.author.guild_permissions.administrator:
            bot_vc = message.guild.me.voice.channel
            for member in bot_vc.members:
                await member.edit(mute=False)
        else:
            await message.channel.send("実行できません。")
    else:
        if message.guild.voice_client:
            print(message.content[0:3])
            print(message.author)
            print(message.content)
            
            if default_voice == 1:
                creat_WAV(message.content)
            else :
                creat_WAV_2(message.content)
            source = discord.FFmpegPCMAudio("output.wav")
            message.guild.voice_client.play(source)
        else:
            pass

    

client.run(token)