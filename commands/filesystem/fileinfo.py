import discord
import globals

from utils import fileutil

from classes.uploads.file import File

async def run(message: discord.Message, args: list[str], client: discord.Client = None):
    if len(args) == 0:
        return await message.channel.send("you need to supply a filename to get info of!")
    
    filename = " ".join(args)

    files = fileutil.search_file(filename)

    if len(files) == 0:
        return await message.channel.send("no files found with that name!")
    multiple = len(files) > 1

    tosend = ""
    if multiple:
        tosend = "i found multiple uploads with that name!\n\n"

    for file in files:
        tosend += (
            f"filename: `{file.name_with_ext}`" + "\n" +
            f"uploader: `{file.owner.name}`" + "\n" +
            f"size: `{file.formatted_size}`" + "\n" +
            f"times gotten: `{file.get_metadata("times_gotten")}`" + "\n\n"
        )

    await message.channel.send(tosend)