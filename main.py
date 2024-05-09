import discord
import nacl
import asyncio
from datetime import datetime, time  
from discord.ext import commands, tasks
from discord import FFmpegPCMAudio

BEN_USER_ID = open("ben_id.txt").read()

GUILD_ID = 927788453150748732

bot = commands.Bot(command_prefix="", intents=discord.Intents.all())

@bot.event
async def on_ready():
    check_user_voice_state.start()
    print("Aw fellas, bot's ready!")


async def play_sound():
    # Check if Ben is in a voice channel
    print("Attempting to play sound...")
    guild = bot.get_guild(GUILD_ID)
    user = guild.get_member(int(BEN_USER_ID))
    if user.voice:
        print("Found the slammer! Let's count down!")
            # Find his channel and snipe him
        voice_channel = user.voice.channel
        voice_client = await voice_channel.connect()

            # Load the sound!
        audio = FFmpegPCMAudio('final_countdown.mp3')
        voice_client.play(audio)
        while voice_client.is_playing():
            await asyncio.sleep(1)
        await voice_client.disconnect()
    

@tasks.loop(seconds=2)  # Adjust the interval as needed
async def check_user_voice_state():
    if datetime.now().time() >= time(23,58) and datetime.now().time() <= time(23,59):
        await play_sound()


with open("token.txt") as file:
    bot.run(file.read())