import discord
from discord.ext import commands
import datetime, random, traceback, json, os
from html2image import Html2Image
import requests


hti = Html2Image()
current_directory = os.getcwd().replace('\\', '/')
intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)
channel_id = channeldihere
token = "MTE0OTcyMTkxMDI4OTEwNDkxNw.GrLqrb.Z6IrVIhgUwqPqDP1ms9F7LlnAOkk"
headers = {
    'authorization': f'Bot {token}'
}

def get_proof(fakename, fakeavatar):
    filename = "test.html"
    with open(filename, 'r') as boost_page:
        proof = boost_page.read().replace('WHITNEYFONT', f"{current_directory}/assets/Whitneyfont.woff").replace('WHITNEYMEDIUM', f"{current_directory}/assets/Whitneymedium.woff").replace('POSTNAME', fakename).replace('POSTAVATAR', fakeavatar)
    return proof

@client.event
async def on_message(message):
    if message.author==client.user:
        return
    if message.channel.id == channel_id:
        await message.reply("Working. dont run another one message or ill fuck u")
        try:
            USER_ID = int(message.content)
        except:
            await message.reply("not a valid ID")
        response = requests.get(f'https://discord.com/api/v9/users/{USER_ID}', headers=headers)
        print(response.text)
        if response.status_code == 200:
            user_data = response.json()
            username = user_data['global_name']
            if username==None:
                username=user_data['username']
            print(username)
            avatar_url = f'https://cdn.discordapp.com/avatars/{USER_ID}/{user_data["avatar"]}.png'
            print(avatar_url)
            proof = get_proof(username, avatar_url)
            image = hti.screenshot(html_str=proof, size=(700, 1195), save_as='proof.png')
            await message.channel.send(file=discord.File('proof.png'))
        else:
            await message.channel.send("Something went wrong while fetching user, make sure its in the same mutual guilds nd stuff ykyk or just dm me.")


@client.command()
async def id(ctx, USER_ID):
    response = requests.get(f'https://discord.com/api/v9/users/{USER_ID}', headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        try:
            username = user_data['global_name']
        except:
            username = user_data['username']
        avatar_url = f'https://cdn.discordapp.com/avatars/{USER_ID}/{user_data["avatar"]}.png'
        proof = get_proof(username, avatar_url)
        image = hti.screenshot(html_str=proof, size=(700, 1065), save_as='proof.png')
        await ctx.send(file=discord.File('proof.png'))
    else:
        await ctx.send("Something went wrong while fetching user, make sure its in the same mutual guilds nd stuff ykyk or just dm me.")


@client.command()
async def custom(ctx, username, avatar_url):
    proof = get_proof(username, avatar_url)
    image = hti.screenshot(html_str=proof, size=(700, 1050), save_as='proof.png')
    await ctx.send(file=discord.File('proof.png'))






client.run(token)