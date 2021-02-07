import discord
import os
import requests
import json
import random



client = discord.Client()

sad_words = ["kms", "fuck me"]

pma = [
    "Please bro",
    "GUH",
    "mood bro"
]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('!hello'):
        await message.channel.send('Sup bitch')

    if msg.startswith('!quote'):
        # quote = get_quote()
        await message.channel.send(get_quote())

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice
                                   (pma))


client.run(os.environ['TOKEN'])