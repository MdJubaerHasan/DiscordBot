import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print("{0.user} in the system.".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startwith('$hello'):
        await message.channel.send('Hello!')


client.run(os.getenv('TOKEN'))