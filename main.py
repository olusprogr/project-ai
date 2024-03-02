import time

start_time = time.time()
import os
from dotenv import load_dotenv
import psutil

import discord

# from debug.ADMIN import Database, Log, Administrator

# Setting up the bot intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = discord.Bot(
    intents=intents,
)


# Function to get the current time
def getCurrentTime():
    t = time.localtime()
    current_time = time.asctime(t)
    return current_time


# Event to run when the bot is ready
@bot.event
async def on_ready():
    # Getting the bot's stats and performance
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_info = psutil.virtual_memory()
    total_ram = round(ram_info.total / (1024 ** 3), 2)
    available_ram = round(ram_info.available / (1024 ** 3), 2)
    used_ram = round(ram_info.used / (1024 ** 3), 2)

    end_time = time.time()
    boot_time = end_time - start_time

    # Printing whenever the bot is ready
    print(
        f"Bot booted in {boot_time:.2f} seconds\n"
        f"Name: {bot.user}\n"
        f"Description: {bot.description if bot.description is None else 'Empty'}\n"
        f"Invite: https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot%20applications.commands\n"
        f"Bot ID: {bot.user.id}\n"
        f"Server count: {len(bot.guilds)}\n"
        f"Ping: {int(bot.latency * 1000)}ms\n\n"
        f"CPU-usage: {cpu_usage}%\n"
        f"Total RAM: {total_ram} GB\n"
        f"Available RAM: {available_ram} GB\n"
        f"Used RAM: {used_ram} GB\n\n"
        f"{bot.user} marked as running..."
    )


# Loading the token from the .env file
load_dotenv()
bot.run(os.getenv("TOKEN"))