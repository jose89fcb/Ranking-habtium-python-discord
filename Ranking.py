import discord
from discord.ext import commands
import requests
import json



 
 
 
bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help
 
 
@bot.command()
async def ranking(ctx, *, habboNombre):
    response = requests.get(f"https://api.habtium.es/v1/badgesranking/search?habbo={habboNombre}")
    try:

     Total = response.json()['statistics']['current']
    except KeyError:
        Total="Habbo No encontrado!"

    try:

     Variacion = response.json()['statistics']['variation']
    except KeyError:
     Variacion="Habbo No encontrado!"


    
    
    #Embed
    embed = discord.Embed(title=f"Ranking Habtium - Keko -> {habboNombre}", description=f"Total: {Total}\n\nVariación: {Variacion}")
    embed.set_thumbnail(url=f"https://www.habbo.es/habbo-imaging/avatarimage?user={habboNombre}&direction=2&head_direction=3&gesture=sml&action=wav&size=n")
    await ctx.channel.send(embed=embed)


  
 
 
 
@bot.event
async def on_ready():
    print("BOT listo!")
    
 
    
bot.run('') 
