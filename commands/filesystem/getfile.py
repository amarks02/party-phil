import discord
import globals

from utils import fileutil

from classes.uploads.file import File

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    filename = " ".join(args)
    files = fileutil.search_file(filename)

    if len(files) == 0:
        return await message.channel.send("no files found with that name!")
    elif len(files) != 1:
        await message.channel.send("i found multiple uploads with that name!")
    
    for file in files:
        await fileutil.send_file_formatted(message.channel, file)