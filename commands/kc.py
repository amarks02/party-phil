import discord
import globals

ACTION_TEMPLATES = {
    "test": {
        "action": "test",
        "args": []
    }
}

async def run(message:discord.Message, args:list[str], client:discord.Client):
    return

    if not "kcactionqueue" in globals.kevin_globals.keys():
        globals.kevin_globals["kcactionqueue"] = []
    if len(args) == 0: return

    cmd = args[0]
    if cmd in ACTION_TEMPLATES.keys():
        action_data = ACTION_TEMPLATES[cmd]
        if len(args) > 1:
            action_data["args"] = args[1:]

        globals.kevin_globals["kcactionqueue"].append(action_data)
        await message.channel.send(f"queued action {cmd}")