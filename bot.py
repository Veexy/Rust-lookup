import discord
from discord.ext import commands
import requests

client = commands.Bot(command_prefix="l.")
url = "https://api.rust-servers.info/status/"
full_url = "https://api.rust-servers.info/info/"
graph_url = "https://api.rust-servers.info/graph/"
player_url = "https://api.rust-servers.info/players/"

@client.event
async def on_ready():
    print("online")

@client.command()
async def lookup(ctx, server_id: int):
    print(f"Looking up {server_id}")
    full_lookup_url = "{}/{}".format(full_url, server_id)
    lookup_url = "{}/{}".format(url, server_id)
    #=====================================================#
    lookup = requests.get(lookup_url)
    full_lookup = requests.get(full_lookup_url)
    #=====================================================#
    status = lookup.json()['status']
    name = lookup.json()['name']
    players = lookup.json()['players']
    max_players = lookup.json()['players_max']
    avg_players = full_lookup.json()['players_avg']
    avg_fps = full_lookup.json()['fps_avg']
    fps = lookup.json()['fps']
    uptime = lookup.json()['uptime']
    website = full_lookup.json()['url']
    country = full_lookup.json()['country_full']
    wipe = full_lookup.json()['wipe_cycle']
    ip = full_lookup.json()['ip']
    port = full_lookup.json()['port']
    #=====================================================#
    image = full_lookup.json()['image']
    image_big = f"https://rust-servers.info/server/sig-468-{ip}-{port}.png"
    #=====================================================#
    if status == "Online":
        embed = discord.Embed(title="<:logo:925961460985765950> Rust Server Lookup", description="Lookup Rust servers from [rust-servers](https://rust-servers.info)")
        embed.set_thumbnail(url=f"{image}")
        embed.add_field(name=f"Name: {name}", value=f"**Players: {players}/{max_players} | Average: {avg_players}**", inline=False)
        embed.add_field(name=f"URL: {website}", value=f"**Location: {country} | Wipe Cycle: {wipe}**", inline=False)
        embed.add_field(name=f"Status: {status}", value=f"**Uptime: {uptime}**", inline=False)
        embed.add_field(name=f"Connect: {ip}:{port}", value=f"**FPS: {fps} | Average FPS: {avg_fps}**", inline=False)
        embed.set_image(url=f"{image_big}")
        embed.set_footer(text=f'Requested by: {ctx.author.name}')
        await ctx.send(embed=embed)
    else:
        await ctx.send("Server is offline")



client.run("token here")
