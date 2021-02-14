import discord
import random
import io
import os
import aiohttp
import urllib.request
import json
from discord.ext import commands

#client (my bot)
client = commands.Bot(command_prefix = "!")
client.remove_command('help')
#discord.Client()

token = os.environ['discord_token']

fortuneBox = ['fortune box', 'fortune box legendary']

premiumBox = ['premium box', 'premium box legendary']

premiumPack = ['premium pack', 'premium pack legendary']

itemBoxes = ['item box', 'item box legendary', 'item box epic', 'item box rare', 'item box common', 'sliver box',
            'sliver box legendary', 'sliver box epic', 'sliver box rare', 'sliver box common']

arenaBoxes = ['rank 1 box', 'rank 1 box legendary', 'rank 3 box', 'rank 3 box legendary', 'rank 5 box', 'rank 5 box legendary', 
            'rank 7 box', 'rank 7 box legendary', 'rank 10 box', 'rank 10 box legendary', 'rank 12 box',
            'rank 15 box','rank 20 box', 'rank 25 box']

wlgang = ['wlgang flag', 'wlgang logo', 'wlgang logo with eye']

#used to know when the bot goes online
@client.event
async def on_ready():
    main_channel = client.get_channel(803809420282822681)
    await main_channel.send('ready')
    print('Bot is active')

#used to find commands that the bot has
@client.command()
async def help(ctx):
        help = discord.Embed(title='These are the possible help commands.', 
        color=discord.Colour.dark_blue())
        help.add_field(name = '!png help', value = 'This will help you on how to use the **!png** command please do **!png help** to learn more', inline = False)
        help.add_field(name = '!ping help', value = 'This will help you on how to use the **!ping** command please do **!ping help** to learn more', inline = False)
        help.add_field(name = '!link help', value = 'This will help you on how to use the **!link** command please do **!link help** to learn more', inline = False)
        help.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await ctx.send(embed=help)

#used to find the ping of the bot
@client.command()
async def ping(ctx):
    ping=discord.Embed(title="What is my Ping?", description=f"My Ping is {round(client.latency * 1000)}ms", color=0xFF5733)
    ping.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
    await ctx.send(embed=ping)

#used to find png of stuff in the game
@client.command()
async def png(ctx, *, arg):
    if(arg == 'help'):
        png = discord.Enbed(title = 'This is the !help png menu.')
        png.add_field(name = 'How to use it?', value = 'use it like this: !png (something)\nFor example: !png wlgang flag')
        png.add_field(name = 'special Commands', value = 'Please do **!png list** for the list of commands')
        png.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await ctx.send(embed=png)
    elif(arg == 'list'):
        png = discord.Embed(title = 'List of all png', description = 'Here is a list of all png that are in the code as of right now')
        png.add_field(name = 'Fortune box', value = '\n'.join(fortuneBox), inline = True)
        png.add_field(name = 'Premium Box', value = '\n'.join(premiumBox), inline = True)
        png.add_field(name = 'Premium Pack', value = '\n'.join(premiumPack), inline = True)
        png.add_field(name = 'Arena Boxes', value = '\n'.join(arenaBoxes), inline = True)
        png.add_field(name = 'Item and Sliver Boxes', value = '\n'.join(itemBoxes), inline = True)
        png.add_field(name = 'WLGang', value = '\n'.join(wlgang), inline = True)
        png.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await ctx.send(embed=png)
    elif(arg == 'item box' or arg == 'mix box'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/itemBox.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'itemBox.png'))
    elif(arg == 'item box legendary' or arg == 'mix box legendary'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/itemBoxLegendary.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'itemBoxLegendary.png'))
    #sliver box
    elif(arg == 'sliver box'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/silverBox.PNG") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'silverBox.PNG'))
    elif(arg == 'sliver box legendary'):
        await ctx.send('no png yet')
    #premium pack
    elif(arg == 'pack' or arg == 'premium pack'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/premiumPack.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'premiumPack.png'))
    elif(arg == 'premium pack legendary' or arg == 'pack legendary'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/premiumPackLegendary.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'premiumPackLegendary.png'))
    #premium box
    elif(arg == 'premium box'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/premiumBox.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'premiumBox.png'))
    elif(arg == 'premium box legendary'):
        await ctx.send('no png yet')
    #fortune box
    elif(arg == 'fortune box'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/fortuneBox.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'fortuneBox.png'))
    elif(arg == 'fortune box legendary'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/fortuneBoxLegendary.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'fortuneBoxLegendary.png'))
    #Arena Boxes
    elif(arg == 'rank 1 box'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/rankOneBox.PNG") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'rankOneBox.PNG'))
    elif(arg == 'rank 1 box legendary'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/rankOneBoxLegendary.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'rankOneBoxLegendary.png'))
    elif(arg == 'rank 3 box'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/rankThreeBox.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'rankThreeBox.png'))
    elif(arg == 'rank 3 box legendary'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/rankThreeBoxLegendary.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'rankThreeBoxLegendary.png'))
    elif(arg == 'rank 5 box'):
        await ctx.send('no png yet')
    elif(arg == 'rank 5 box legendary'):
        await ctx.send('no png yet')
    elif(arg == 'rank 7 box'):
        await ctx.send('no png yet')
    elif(arg == 'rank 7 box legendary'):
        await ctx.send('no png yet')
    elif(arg == 'rank 10 box'):
        await ctx.send('no png yet')
    elif(arg == 'rank 10 box legendary'):
        await ctx.send('no png yet')
    elif(arg == 'rank 12 box'):
        await ctx.send('no png yet')
    elif(arg == 'rank 15 box'):
        await ctx.send('no png yet')
    elif(arg == 'rank 20 box'):
        await ctx.send('no png yet')
    elif(arg == 'rank 25 box'):
        await ctx.send('no png yet')
    #clan war box
    #WLGang stuff
    elif(arg == 'wlgang' or arg == 'wlgang logo' or arg == 'WLGang logo'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/wlgangLogo.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'wlgangLogo.png'))
    elif(arg == 'wlgang with eyes' or arg == 'wlgang logo with eyes' or arg == 'WLGang logo with eyes'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/wlgangLogowithEyes.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'wlgangLogowithEyes.png'))
    elif(arg == 'wlgang flag' or arg == 'WLGang flag'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/wlgangFlag.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'wlgangFlag.png'))
  
    #mechs
    elif(arg == 'god mode'):
        await ctx.send(file=discord.File('godMode.png'))
    #other
    elif(arg == 'logo' or arg == 'supermechs'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/supermechs.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'supermechs.png'))
    #Torsos
    elif(arg == 'interceptor'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/Interceptor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Interceptor.png'))
    elif(arg == 'nightmare'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/Nightmare.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Nightmare.png'))
    elif(arg == 'sith'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/Sith.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Sith.png'))
    elif(arg == 'archimond'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/Archimonde.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Archimonde.png'))
    elif(arg == 'avenger'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/Avenger.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Avenger.png'))
    elif(arg == 'energy free armor' or arg == 'efa'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/EnergyFreeArmor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'EnergyFreeArmor.png'))
    elif(arg == 'hollow spectral armor' or arg == 'physical monkey'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/HollowSpectralArmor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'HollowSpectralArmor.png'))
    elif(arg == 'hollow cyber armor' or arg == 'physical cyber'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/HollowCyberArmor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'HollowCyberArmor.png'))
    elif(arg == 'rusty energy armor' or arg == 'energy monkey'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/RustyEnergyArmor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'RustyEnergyArmor.png'))
    elif(arg == 'rusty cyber armor' or arg == 'energy cyber'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/RustyCyberArmor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'RustyCyberArmor.png'))
    elif(arg == 'fractured heat armor' or arg == 'heat monkey'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/FracturedHeatArmor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'FracturedHeatArmor.png'))
    elif(arg == 'fractured cyber armor' or arg == 'heat cyber'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/FracturedCyberArmor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'FracturedCyberArmor.png'))
    elif(arg == 'hardened platinum vest' or arg == 'physical vest' or arg == 'hpv'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/HardenedPlatinumVest.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'HardenedPlatinumVest.png'))
    elif(arg == 'molten platinum vest' or arg == 'heat vest' or arg == 'mpv'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/MoltenPlatinumVest.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'MoltenPlatinumVest.png'))
    elif(arg == 'lightning platinum vest' or arg == 'energy vest' or arg == 'lpv'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/LightningPlatinumVest.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'LightningPlatinumVest.png'))
    elif(arg == 'battery armor'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/BatteryArmor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'BatteryArmor.png'))
    elif(arg == 'flame battery armor'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/FlamingBatteryArmor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'FlamingBatteryArmor.png'))
    elif(arg == 'energy battery armor'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/EnergyBatteryArmor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'EnergyBatteryArmor.png'))
    elif(arg == 'naga'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/Naga.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Naga.png'))
    elif(arg == 'zarkares'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/Zarkares.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Zarkares.png'))
    elif(arg == 'sabretooth'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/Sabretooth.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Sabretooth.png'))
    elif(arg == 'windigo'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/Windigo.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Windigo.png'))
    elif(arg == 'brutality'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/Brutality.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Brutality.png'))
    elif(arg == 'grim reaper'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/GrimReaper.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'GrimReaper.png'))
    #legs [15]
    elif(arg == 'massive stone feet'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/MassiveStoneFeet.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'MassiveStoneFeet.png'))
    elif(arg == 'massive lava feet'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/MassiveLavaFeet.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'MassiveLavaFeet.png'))
    elif(arg == 'massive shocker feet'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/MassiveShockerFeet.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'MassiveShockerFeet.png'))
    elif(arg == 'iron boots'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/IronBoots.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'IronBoots.png'))
    elif(arg == 'scorching feet'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/ScorchingFeet.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'ScorchingFeet.png'))
    elif(arg == 'charged walkers'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/ChargedWalkers.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'ChargedWalkers.png'))
    elif(arg == 'grave diggers'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/GraveDiggers.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'GraveDiggers.png'))
    elif(arg == 'dynamic stompers'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/DynamicStompers.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'DynamicStompers.png'))
    elif(arg == 'recoil stompers'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/RecoilStompers.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'RecoilStompers.png'))
    elif(arg == 'dynamite boots'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/DynamiteBoots.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'DynamiteBoots.png'))
    elif(arg == 'lightning supporters'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/LightningSupporters.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'LightningSupporters.png'))
    elif(arg == 'devouring paws'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/DevouringPaws.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'DevouringPaws.png'))
    elif(arg == 'the claw' or arg == 'claw'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/TheClaw.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'TheClaw.png'))
    elif(arg == 'rolling beasts'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/RollingBeasts.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'RollingBeasts.png'))
    elif(arg == 'sparked runners'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/SparkedRunners.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'SparkedRunners.png'))                 

#used to find the link of a youtuber
@client.command()
async def link(ctx, *, arg):
    if(arg == 'firewater789'):
        await ctx.send('https://www.youtube.com/channel/UCoku4b76Dhs-xZbrkmwidUQ')
    elif(arg == 'Atusiff' or arg == 'atusiff'):
        await ctx.send('https://www.youtube.com/channel/UCk4OvXT494YJWpdVaJwvWyQ')
    elif(arg == 'tacocat' or arg == 'naoki ogawa'):
        await ctx.send('https://www.youtube.com/channel/UCR86NR06Ur1MxaPYCTVk74Q')
    elif(arg == 'windforge' or arg == 'WindForge'):
        await ctx.send('https://www.youtube.com/channel/UCzsrFcyccu1FN3fBvpNDJnA')
    elif(arg == 'Pyra Pinky-K' or arg == 'pyra pinky' or arg == 'pyra pinky k'):
        await ctx.send('https://www.youtube.com/channel/UCT66b-SZCXkYm6ahSbiplVA')
    elif(arg == 'Lookotza' or arg == 'lookotza'):
        await ctx.send('https://www.youtube.com/channel/UC89sVdPFHtzib90X4vJJGtg')
    elif(arg == 'madao san'):
        await ctx.send('https://www.youtube.com/channel/UC1ItNEPxPV0IQJPGpvFez2Q')
    elif(arg == 'dwightx' or arg == 'Dwightx'):
        await ctx.send('https://www.youtube.com/channel/UCFGugxNDgF2LzL1ictmxDXQ')
    elif(arg == 'chinaski' or arg == 'Chinaski'):
        await ctx.send('https://www.youtube.com/user/DmDnDfD')
    elif(arg == 'Rambo Gaming' or arg == 'rambo gaming' or arg == 'rambo'):
        await ctx.send('https://www.youtube.com/channel/UCeOf32uACOWTLTxYAHnaOZA')
    elif(arg == 'L4K3 v' or arg == 'l4k3 v' or arg == 'lake' or arg == 'L4K3' or arg == 'l4k3'):
        await ctx.send('https://www.youtube.com/channel/UCgdMVzvwiE1NTBHm_tggGnA')
    elif(arg == 'Stefan Ludak' or arg == 'stefan ludak' or arg == 'stefan'):
        await ctx.send('https://www.youtube.com/channel/UCdYzUORe0HyC7UDE5y6TEiA')
    elif(arg == 'simpleon' or arg == 'yeet' or arg == 'yeet' or arg == 'Yeet'):
        await ctx.send('https://www.youtube.com/channel/UCsGYt995Qobe46uluJ_cCdg')
    elif(arg == 'Purific' or arg == 'purific'):
        await ctx.send('https://www.youtube.com/channel/UCWDulhcB8oJq80PNi5RCy5Q')
    elif(arg == 'CleverNameSM' or arg == 'clevername' or arg == 'clevernamesm'):
        await ctx.send('https://www.youtube.com/channel/UCwgZFzMbhNnppqRzIAVwQPA')
    elif(arg == 'ambroise'):
        await ctx.send('https://www.youtube.com/channel/UCzJL0bq22-EvX5RY9fUtVzQ')
    elif(arg == 'AEROST' or arg == 'aerost'):
        await ctx.send('https://www.youtube.com/channel/UCMicacPcFVmvTI2JfkUD5RA/videos')
    elif(arg == 'Alex2040 bR' or arg == 'alex2040'):
        await ctx.send('https://www.youtube.com/channel/UCQXq-AFvt-zDKzMHY5HJkwQ')
    elif(arg == 'bestplayeroftheworld'):
        await ctx.send('https://www.youtube.com/channel/UCd8Rd4aMvOEPrYkqSe8_XJg')
    elif(arg == 'BossParody SM' or arg == 'BossParody' or arg == 'bossparody'):
        await ctx.send('https://www.youtube.com/channel/UCvrnVpsuQmeHtP845PCXfHA')
    elif(arg == 'CHIPS' or arg == 'chips'):
        await ctx.send('https://www.youtube.com/channel/UCyqUTkIXoz2dbfySWg3Vi-g')
    elif(arg == 'ClockLiuOG' or arg == 'clockliuog' or arg == 'clockliu'):
        await ctx.send('https://www.youtube.com/channel/UCLWnnIyyZ0ZvvuLLEfikfxQ')
    elif(arg == 'DOOM BRINGER' or arg == 'doom bringer'):
        await ctx.send('https://www.youtube.com/channel/UCWTUp7ADNL7fVwRF_JUb0Aw/featured')
    elif(arg == 'epicspeedster'):
        await ctx.send('https://www.youtube.com/channel/UCYbL5QSlQuL3mqeQVlU25Dw')
    elif(arg == 'FAIOLA GAMES' or arg == 'faiola games' or arg == 'faiola'):
        await ctx.send('https://www.youtube.com/channel/UC0OsraC3NUb1WKvKc2UrWOg')
    elif(arg == 'Fyrestare' or arg == 'fyrestare'):
        await ctx.send('https://www.youtube.com/channel/UCa0xXEaj92pNPl3Vnc3hUUQ')
    elif(arg == 'Hauer Horatio' or arg == 'hauer horatio' or arg == 'Hauer' or arg == 'hauer'):
        await ctx.send('https://www.youtube.com/channel/UCPjCO3B-SHCoa_CWznChweA')
    elif(arg == 'iDani RF' or arg == 'iDani' or arg == 'idani'):
        await ctx.send('https://www.youtube.com/channel/UCrC2PCKk72iI9BJS6c6m3PA')
    elif(arg == 'JIYOON' or arg == 'jiyoon'):
        await ctx.send('https://www.youtube.com/channel/UCcl0Zx3wBLyPcQcjLFjqwmA')
    elif(arg == 'Laszeski' or arg == 'laszeski'):
        await ctx.send('https://www.youtube.com/channel/UCu8czDKpVyWI34SJrPEUqnQ')
    elif(arg == 'MakeHappyVideos' or arg == 'makehappyvideos'):
        await ctx.send('https://www.youtube.com/channel/UCrQWVFMk-RoJvEtMoZgzWOw')
    elif(arg == 'MAX GAMES' or arg == 'max games'):
        await ctx.send('https://www.youtube.com/channel/UClCQ-idlW1lcaCcf7Qb8YNQ')
    elif(arg == 'Maxx' or arg == 'warrmachine' or arg == 'WarrMachine'):
        await ctx.send('https://www.youtube.com/channel/UCgpqiDLRNMeS2G8rSfhKmfA')
    elif(arg == 'solitaire' or arg == 'Solitaire'):
        await ctx.send('https://www.youtube.com/channel/UCz1AL1Q0QlTzYPFCK8qaudw')
    elif(arg == 'Moretusiff' or arg =='moretusiff'):
        await ctx.send('https://www.youtube.com/channel/UCMDM8S1Riuf14AOvvC85JHQ')
    elif(arg == 'nullification zealot' or arg == 'nullification'):
        await ctx.send('https://www.youtube.com/channel/UCuw9Df6hBt0w729_EGM40tw')
    elif(arg == 'Pizza4UAndMe' or arg == 'pizza4uandme'):
        await ctx.send('https://www.youtube.com/channel/UCUDPQaSsYX6bFoPb2sSkKtw')
    elif(arg == 'PRO Sm' or arg == 'pro sm'):
        await ctx.send('https://www.youtube.com/channel/UCIDvTNjCT2v0ZKuwZbsXZtA')
    elif(arg == 'S.A.M' or arg == 's.a.m'):
        await ctx.send('https://www.youtube.com/channel/UCfr5truubiCZxqugvWfuyRA')
    elif(arg == 'Smulated ace' or arg == 'Smulated' or arg == 'smulated ace' or arg == 'smulated'):
        await ctx.send('https://www.youtube.com/channel/UC9eHwO-_ImkvyMy1MncUDQA')
    elif(arg == 'SuperMechs Helper' or arg == 'supermechs helper'):
        await ctx.send('https://www.youtube.com/channel/UCwTlAgskjqJ6blYJH5JuSNg')
    elif(arg == 'Unlucky Joe' or arg == 'unlucky joe'):
        await ctx.send('https://www.youtube.com/channel/UCtV3vCHHpXUDgqoQdb8KIqA')
    elif(arg == 'WLGang Clan' or arg == 'wlgang clan'):
        await ctx.send('https://www.youtube.com/channel/UCo9ZZdvB6tI8-BBjf0349Kw')
    elif(arg == 'ZeRo' or arg == 'zero'):
        await ctx.send('https://www.youtube.com/channel/UCFLteDDcJ6Y7UFxulXJpbRA')
    elif(arg == 'Zoner' or arg == 'zoner'):
        await ctx.send('https://www.youtube.com/channel/UCNhmVDtEb6sC1lS0tUGZH3A')
    else:
        link=discord.Embed(title='Invailed Name', 
        description='The name you entered is a invailed name or maybe you typed it wrong.\nFor Example:\ninstead of typing Firewater789 try firewater789',
        color=0xFF5733)
        await ctx.send(embed=link)

#Rum the client on the server
client.run(token)
