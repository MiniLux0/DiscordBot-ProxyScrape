import discord
import requests
from discord import Embed, File, Button, View
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext #SLASH NO IS A WORKING IN PYTHON 2.0 - SORRY

token = "Token Here"

client = commands.Bot(command_prefix='+')
client.remove_command('help')
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
    activity = discord.Activity(
        type=discord.ActivityType.watching, name=f"+help | +invite")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")

# client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=f"+help | +invite"))

@client.event
async def on_message(message):  
    if message.author == client.user:
        return
    if message.mention_everyone:
        return
    if client.user.mentioned_in(message):
        embed = Embed(title="<:reglas1:908809948824227850> Light Proxy",
                      description=f'')
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/890390947983142982/917192888306237470/7ee5f4b74d52ed3bb5f89b74208019db.png")
        embed.set_footer(text="» Simple Bot Scraper Proxies")
        embed.add_field(name="What does this bot do?", value="It is a bot where it compiles lists of proxies from different web pages.", inline=False)
        embed.add_field(name="Info:", value="Use `+help` to see the bot commands", inline=False)
        embed.add_field(name="Data:", value="Use the bot on the creator's server, type `+invite` to get the invitation", inline=False)
        embed.add_field(name="Creator:", value="JessVV#8274", inline=False)
        await message.channel.send(embed=embed)
    await client.process_commands(message)

@client.command()
async def help(ctx):
    embed = Embed(title=f"All Commands - Hi!!  `{ctx.guild.name}`",
                  description=f"This is all the information of the **Light Proxy** `<3`")
    
    embed.add_field(name="~ +help", value="Displays all available commands", inline=False)
    embed.add_field(name="~ +http", value="Sends fresh http proxy list", inline=False)
    embed.add_field(name="~ +https", value="Sends fresh https proxy list", inline=False)
    embed.add_field(name="~ +socks4", value="Sends fresh socks4 proxy list", inline=False)
    embed.add_field(name="~ +socks5", value="Sends fresh socsk5 proxy list", inline=False)
    embed.add_field(name="~ +all", value="Sends fresh http, https, socks4 and socks5 proxy list", inline=False)
    await ctx.send(embed=embed)


@client.command(name="Ping", description="Shows the bots latentcy")
async def ping(ctx):
    embed = discord.Embed(title="Pong!", color=0xff0000)
    embed.add_field(name=(f'{round(ctx.bot.latency * 1000)} ms'), value="`Light Sniper working properly!`", inline=True)  # este es el comando del ping
    await ctx.send(embed=embed)


@client.command()
async def invite(ctx):
    # SERVER NOMBRE  # TIME . COLOR
    embed = discord.Embed(
        title="Invite server")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/890390947983142982/917188787283570698/862df01902ea182f604662835aa5185e.png")
    embed.add_field(name="Server Light Proxy",
                    value="\nClick on the button to join my server. ^^\n\n~ Thanks `<3`")
    button = Button(label="Invite", url="https://dsc.gg/lighthit",
                    style=discord.ButtonStyle.green, emoji="🔧")
    view = View()
    view.add_item(button)
    await ctx.send(embed=embed, view=view)

@client.command()
async def http(ctx):
    f = open("File/http-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Data/http-proxies.txt"))

@client.command()
async def https(ctx):
    f = open("File/https-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Data/https-proxies.txt"))

@client.command()
async def socks4(ctx):
    f = open("File/socks4-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Data/socks4-proxies.txt"))

@client.command()
async def socks5(ctx):
    f = open("File/socks5-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Data/socks5-proxies.txt"))

@client.command()
async def all(ctx):
    f = open("File/all-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=all&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Data/all-proxies.txt"))

client.run(token)