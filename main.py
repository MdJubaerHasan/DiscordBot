import discord

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

token = 'ODYwNTM3NDg4NzQ5NDk0MzQz.YN8r_Q.ChADbrNWdg2pywuTiVyEGTtu9yA'
client.run(token)