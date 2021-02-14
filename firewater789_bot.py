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

itemBoxes = ['item box', 'item box legendary', 'sliver box', 'sliver box legendary']

arenaBoxes = ['rank 1 box', 'rank 1 box legendary', 'rank 3 box', 'rank 3 box legendary', 'rank 5 box', 'rank 5 box legendary', 
            'rank 7 box', 'rank 7 box legendary', 'rank 10 box', 'rank 10 box legendary', 'rank 12 box',
            'rank 15 box','rank 20 box', 'rank 25 box']

wlgang = ['wlgang flag', 'wlgang logo', 'wlgang logo with eye']

torsos = ['interceptor',
            'nightmare',
            'sith',
            'archimond',            
            'avenger',
            'hollow spectral armor',
            'hollow cyber armor',
            'rusty energy armor',
            'rusty cyber armor',
            'fractured heat armor',
            'fractured cyber armor',
            'hardened platinum vest',
            'molten platinum vest',
            'lightning platinum vest',
            'battery armor',
            'flame battery armor',
            'energy battery armor',
            'naga',
            'zarkares',
            'sabretooth',
            'energy free armor',  
            'windigo',
            'brutality',                          
            'grim reaper']

legs = ['massive lava feet',
        'massive shocker feet',
        'massive stone feet',
        'iron boots',
        'scorching feet',
        'charged walkers',
        'grave diggers',
        'dynamic stompers',
        'recoil stompers',
        'dynamite boots',
        'lightning supporters',
        'devouring paws',
        'sparked runners',
        'rolling beasts',
        'the claw']

sideWeapons = ['**physical [23]**',
            'perimeter protector',
            'back breaker',
            'disintegration',  
            'war hammer',    
            'seraphblade', 
            'rock polisher',  
            'rock recoiler',    
            'annihilation',
            'mercy',             
            'advanced repulser' , 
            'armor annihilator',
            'damaged armor annihilator',
            'sacrifice cannon',   
            'purifier',         
            'unrepaired laser cannon',
            'nightfall',           
            'bloodweep',
            'terror cry',            
            'dark eagle', 
            'malfunctitoning blaster',
            'sweetie',            
            'ejection blast',
            'last resort vulcan',
            '**heat[28]**',
            'distance controller',
            'heronmark',        
            'terrorblade',      
            'flaming hammer',  
            'overcooking oven', 
            'chaos bringer',    
            'crimson rapture', 
            'reckoning',       
            'magma recoiler',  
            'basalt dissolver', 
            'broken devourer', 
            'magma blast',                                      
            'sorrow',          
            'abomination',   
            'heat bomb',        
            'shadow wolf',     
            'explosive retreat',
            'rusty heat blaster',
            'flaminator',
            'hybrid heat cannon',
            'corrupt light',   
            'dawnblaze',
            'cracked plasma cannon',
            'basalt polisher',
            'misguided rocket battery',
            'fractured basalt annihilator',
            'fractured basalt dissolver',
            'overcharged rocket battery', 
            '**Energy[26]**',  
            'distance generator',
            'unstable power cell',
            'brightroar', 
            'bigdaddy',      
            'stormweaver',  
            'ash creator',   
            'viking hammer', 
            'lightning recoiler',
            'bulldog',  
            'blizzard dissolver',
            'drunk lightning',
            'emp',           
            'mortal bullet',
            'last words', 
            'bunker shell',
            'piercing fox',
            'evac spark',
            'scrapped energy blaster',
            'malice beam',
            'ultrabright',   
            'hot flash',     
            'hybrid energy cannon',
            'lightning cutter',
            'obsolete energy cannon',
            'broken blizzard dissolver',
            'broken blizzard annihilator']

topWeapons = ['frantic brute',
            'frantic flame',
            'frantic lightning',
            'reckless beam',
            'savagery',
            'hysteria',
            'distance shredder',
            'space invader',
            'party crasher',
            'mighty cannon',
            'desert snake',
            'spinefall',
            'cockpit piercer',
            'cockpit electrocuter',
            'cockpit burner',
            'falcon',
            'flaming scope',
            'lightning scope',
            'lazy falcon',
            'half brunt scope',
            'electrocuted scope',
            'night eagle',
            'spartan carnage',
            'desert fury',
            'red rain',
            'burning shower',
            'supreme cannon',
            'desolation',
            'iron frenzy',
            'vandal rage',
            'grim cobra',
            'vailent sniper',
            'delerium',
            'overcompressed disintegration',
            'overheated heat bomb',
            'overloaded emp']

drones = ['N/A']
specials = ['N/A']
modules = ['N/A']
mechs = ['god mode']
clan = ['wlgang flag', 'wlgang logo', 'wlgang logo with eye']

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
        png_help = discord.Embed(title = 'This is the !png help menu.')
        png_help.add_field(name = 'How to use it?', value = 'use it like this: !png (something)\nFor example: !png wlgang flag', inline = False)
        png_help.add_field(name = 'To Find all Possible Png Here are a few Commands.', value = '!png torsos\n!png legs\n!png side weapon\n!png top weapon\n!png drone\n!png specials\n!png modules\n!png boxes\n!png mechs\n!png clan', inline = False)
        png_help.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await ctx.send(embed=png_help)
    elif(arg == 'torsos' or arg == 'torso'):
        png_torsos = discord.Embed(title = 'List of all torsos png', description = 'Here is a list of all box png that are in the code as of right now')
        png_torsos.add_field(name = 'Torso', value = '\n'.join(torsos))
        png_torsos.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await ctx.send(embed=png_torsos)
    elif(arg == 'legs' or arg == 'leg'):
        png_legs = discord.Embed(title = 'List of all torsos png', description = 'Here is a list of all box png that are in the code as of right now')
        png_legs.add_field(name = 'Torso', value = '\n'.join(legs))
        png_legs.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await ctx.send(embed=png_legs)
    elif(arg == 'side weapons' or arg == 'side weapon'):
        png_sideWeapons = discord.Embed(title = 'List of all torsos png', description = 'Here is a list of all box png that are in the code as of right now')
        png_sideWeapons.add_field(name = 'Torso', value = '\n'.join(sideWeapons))
        png_sideWeapons.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await ctx.send(embed=png_sideWeapons)
    elif(arg == 'top weapons' or arg == 'top weapon'):
        png_topWeapons = discord.Embed(title = 'List of all torsos png', description = 'Here is a list of all box png that are in the code as of right now')
        png_topWeapons.add_field(name = 'Torso', value = '\n'.join(topWeapons))
        png_topWeapons.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await ctx.send(embed=png_topWeapons)
    elif(arg == 'drones' or arg == 'drone'):
        png_drones = discord.Embed(title = 'List of all torsos png', description = 'Here is a list of all box png that are in the code as of right now')
        png_drones.add_field(name = 'Torso', value = '\n'.join(drones))
        png_drones.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await ctx.send(embed=png_drones)
    elif(arg == 'specials' or arg == 'special'):
        png_specials = discord.Embed(title = 'List of all torsos png', description = 'Here is a list of all box png that are in the code as of right now')
        png_specials.add_field(name = 'Torso', value = '\n'.join(specials))
        png_specials.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await ctx.send(embed=png_specials)
    elif(arg == 'modules' or arg == 'module'):
        png_modules = discord.Embed(title = 'List of all torsos png', description = 'Here is a list of all box png that are in the code as of right now')
        png_modules.add_field(name = 'Torso', value = '\n'.join(modules))
        png_modules.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await ctx.send(embed=png_modules)
    elif(arg == 'mechs' or arg == 'mech'):
        png_mechs = discord.Embed(title = 'List of all torsos png', description = 'Here is a list of all box png that are in the code as of right now')
        png_mechs.add_field(name = 'Torso', value = '\n'.join(mechs))
        png_mechs.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await ctx.send(embed=png_mechs)
    elif(arg == 'clan'):
        png_clan = discord.Embed(title = 'List of all torsos png', description = 'Here is a list of all box png that are in the code as of right now')
        png_clan.add_field(name = 'Torso', value = '\n'.join(clan))
        png_clan.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await ctx.send(embed=png_clan)
    elif(arg == 'boxes'):
        png_boxes = discord.Embed(title = 'List of all box png', description = 'Here is a list of all box png that are in the code as of right now')
        png_boxes.add_field(name = 'Fortune box', value = '\n'.join(fortuneBox), inline = True)
        png_boxes.add_field(name = 'Premium Box', value = '\n'.join(premiumBox), inline = True)
        png_boxes.add_field(name = 'Premium Pack', value = '\n'.join(premiumPack), inline = True)
        png_boxes.add_field(name = 'Arena Boxes', value = '\n'.join(arenaBoxes), inline = True)
        png_boxes.add_field(name = 'Item and Sliver Boxes', value = '\n'.join(itemBoxes), inline = True)
        png_boxes.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await ctx.send(embed=png_boxes)
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
    elif(arg == 'perimeter protector'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/PerimeterProtector.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'PerimeterProtector.png'))
    elif(arg == 'back breaker'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BackBreaker.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'BackBreaker.png'))
    elif(arg == 'disintegration'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/Disintegration.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Disintegration.png'))
    elif(arg == 'war hammer'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/WarHammer.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'WarHammer.png'))
    elif(arg == 'seraphblade'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/SeraphBlade.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'SeraphBlade.png'))
    elif(arg == 'rock recoiler'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/RockRecoiler.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'RockRecoiler.png'))
    elif(arg == 'annihilation'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/Annihilation.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Annihilation.png'))
    elif(arg == 'mercy'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/Mercy.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Mercy.png'))
    elif(arg == 'advanced repulser'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/AdvancedRepulser.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'AdvancedRepulser.png'))
    elif(arg == 'armor annihilator'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/ArmorAnnihilator.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'ArmorAnnihilator.png'))
    elif(arg == 'sacrifice cannon'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/SacrificeCannon.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'SacrificeCannon.png'))
    elif(arg == 'purifier'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/Purifier.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Purifier.png'))
    elif(arg == 'unrepaired laser cannon'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/UnrepairedLaserCannon.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'UnrepairedLaserCannon.png'))
    elif(arg == 'nightfall'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/NightFall.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'NightFall.png'))
    elif(arg == 'bloodweep'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BloodWeep.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'BloodWeep.png'))
    elif(arg == 'terror cry'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/TerrorCry.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'TerrorCry.png'))
    elif(arg == 'dark eagle'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/DarkEagle.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'DarkEagle.png'))
    elif(arg == 'malfunctitoning blaster'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/MalfunctioningBlaster.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'MalfunctioningBlaster.png'))
    elif(arg == 'sweetie'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/Sweetie.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Sweetie.png'))
    elif(arg == 'ejection blast'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/EjectionBlast.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'EjectionBlast.png'))
    elif(arg == 'last resort vulcan'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/LastResortVulcan.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'LastResortVulcan.png'))
    elif(arg == 'damaged armor annihilator'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/DamagedArmorAnnihilator.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'DamagedArmorAnnihilator.png'))
    elif(arg == 'rock polisher'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/RockPolisher.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'RockPolisher.png'))
        
    #heat [28]
    elif(arg == 'distance controller'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/DistanceController.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'DistanceController.png'))
    elif(arg == 'heronmark'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/HeronMark.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'HeronMark.png'))
    elif(arg == 'terrorblade'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/TerrorBlade.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'TerrorBlade.png'))
    elif(arg == 'flamimg hammer'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/FlamingHammer.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'FlamingHammer.png'))
    elif(arg == 'overcooking oven'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/OvercookingOven.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'OvercookingOven.png'))
    elif(arg == 'chaos bringer'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/ChaosBringer.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'ChaosBringer.png'))
    elif(arg == 'crimson rapture'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/CrimsonRapture.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'CrimsonRapture.png'))
    elif(arg == 'reckoning'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/Reckoning.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Reckoning.png'))
    elif(arg == 'magma recoiler'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/MagmaRecoiler.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'MagmaRecoiler.png'))
    elif(arg == 'basalt dissolver'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BasaltDissolver.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'BasaltDissolver.png'))
    elif(arg == 'broken devourer'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BrokenDevourer.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'BrokenDevourer.png'))
    elif(arg == 'magma blast'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/MagmaBlast.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'MagmaBlast.png'))
    elif(arg == 'sorrow'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/Sorrow.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Sorrow.png'))
    elif(arg == 'abomination'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/Abomination.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Abomination.png'))
    elif(arg == 'heat bomb'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/HeatBomb.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'HeatBomb.png'))
    elif(arg == 'shadow wolf'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/ShadowWolf.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'ShadowWolf.png'))
    elif(arg == 'explosive retreat'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/ExplosiveRetreat.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'ExplosiveRetreat.png'))
    elif(arg == 'rusty heat blaster'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/RustyHeatBlaster.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'RustyHeatBlaster.png'))
    elif(arg == 'flaminator'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/Flaminator.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Flaminator.png'))
    elif(arg == 'hybrid heat cannon'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/HybridHeatCannon.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'HybridHeatCannon.png'))
    elif(arg == 'corrupt light'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/CorruptLight.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'CorruptLight.png'))
    elif(arg == 'dawnblaze'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/DawnBlaze.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'DawnBlaze.png'))
    elif(arg == 'cracked plasma cannon'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/CrackedPlasmaCannon.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'CrackedPlasmaCannon.png'))
    elif(arg == 'basalt polisher'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BasaltPolisher.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'BasaltPolisher.png'))
    elif(arg == 'misguided rocket battery'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/MisguidedRocketBattery.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'MisguidedRocketBattery.png'))
    elif(arg == 'fractured basalt annihilator'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/_1.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, '_1.png'))
    elif(arg == 'fractured basalt dissolver'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/_%20(12).png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, '_%20(12).png'))
    elif(arg == 'overcharged rocket battery' ):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/OverchargedRocketBattery.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'OverchargedRocketBattery.png'))

    #energy[26]
    elif(arg == 'distance generator'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/DistanceGenerator.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'DistanceGenerator.png'))
    elif(arg == 'unstable power cell' or arg == 'upc'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/UnstablePowerCell.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'UnstablePowerCell.png'))
    elif(arg == 'brightroar' or arg == 'bright roar'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BrightRoar.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'BrightRoar.png'))
    elif(arg == 'bigdaddy'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BigDaddy.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'BigDaddy.png'))
    elif(arg == 'stormweaver'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/StormWeaver.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'StormWeaver.png'))
    elif(arg == 'ash creator'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/AshCreator.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'AshCreator.png'))
    elif(arg == 'viking hammer'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/VikingHammer.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'VikingHammer.png'))
    elif(arg == 'lightning recoiler'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/LightningRecoiler.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'LightningRecoiler.png'))
    elif(arg == 'bulldog'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BullDog.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'BullDog.png'))
    elif(arg == 'blizzard dissolver'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BlizzardDissolver.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'BlizzardDissolver.png'))
    elif(arg == 'drunk lightning'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/DrunkLightning.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'DrunkLightning.png'))
    elif(arg == 'emp'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/EMP.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'EMP.png'))
    elif(arg == 'mortal bullet'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/MortalBullet.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'MortalBullet.png'))
    elif(arg == 'last words'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/LastWords.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'LastWords.png'))
    elif(arg == 'bunker shell'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BunkerShell.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'BunkerShell.png'))
    elif(arg == 'piercing fox'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/PiercingFox.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'PiercingFox.png'))
    elif(arg == 'evac spark'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/EvacSpark.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'EvacSpark.png'))
    elif(arg == 'scrapped energy blaster'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/ScrappedEnergyBlaster.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'ScrappedEnergyBlaster.png'))
    elif(arg == 'malice beam'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/MaliceBeam.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'MaliceBeam.png'))
    elif(arg == 'ultrabright'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/UltraBright.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'UltraBright.png'))
    elif(arg == 'hot flash'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/HotFlash.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'HotFlash.png'))
    elif(arg == 'hybrid energy cannon'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/HybridEnergyCannon.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'HybridEnergyCannon.png'))
    elif(arg == 'lightning cutter'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/LightningCutter.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'LightningCutter.png'))
    elif(arg == 'obsolete energy cannon'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/ObsoleteEnergyCannon.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'ObsoleteEnergyCannon.png'))
    elif(arg == 'broken blizzard dissolver'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BrokenBlizzardDissolver.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'BrokenBlizzardDissolver.png'))
    elif(arg == 'broken blizzard annihilator'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/__.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, '__.png'))
    elif(arg == 'frantic brute'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/FranticBrute.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'FranticBrute.png'))
    elif(arg == 'frantic flame'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/FranticFlame.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'FranticFlame.png'))
    elif(arg == 'frantic lightning'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/FranticLightning.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'FranticLightning.png'))
    elif(arg == 'reckless beam'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/RecklessBeam.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'RecklessBeam.png'))
    elif(arg == 'savagery'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/Savagery.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Savagery.png'))
    elif(arg == 'hysteria'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/Hysteria.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Hysteria.png'))
    elif(arg == 'distance shredder'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/DistanceShredder.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'DistanceShredder.png'))
    elif(arg == 'space invader'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/SpaceInvader.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'SpaceInvader.png'))
    elif(arg == 'party crasher'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/PartyCrasher.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'PartyCrasher.png'))
    elif(arg == 'mighty cannon'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/MightyCannon.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'MightyCannon.png'))
    elif(arg == 'desert snake'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/DesertSnake.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'DesertSnake.png'))
    elif(arg == 'spinefall'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/SpineFall.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'SpineFall.png'))
    elif(arg == 'cockpit piercer'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/CockpitPiercer.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'CockpitPiercer.png'))
    elif(arg == 'cockpit electrocuter'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/CockpitElectrocuter.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'CockpitElectrocuter'))
    elif(arg == 'cockpit burner'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/CockpitBurner.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'CockpitBurner.png'))
    elif(arg == 'falcon'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/Falcon.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Falcon.png'))
    elif(arg == 'lightning scope'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/LightningScope.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'LightningScope.png'))
    elif(arg == 'flaming scope'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/FlamingScope.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'FlamingScope.png'))
    elif(arg == 'lazy falcon'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/LazyFalcon.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'LazyFalcon.png'))
    elif(arg == 'half brunt scope'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/HalfBurntScope.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'HalfBurntScope.png'))
    elif(arg == 'electrocuted scope'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/ElectrocutedScope.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'ElectrocutedScope.png'))
    elif(arg == 'night eagle'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/NightEagle.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'NightEagle.png'))
    elif(arg == 'spartan carnage'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/SpartanCarnage.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'SpartanCarnage.png'))
    elif(arg == 'desert fury'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/DesertFury.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'DesertFury.png'))
    elif(arg == 'red rain'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/RedRain.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'RedRain.png'))
    elif(arg == 'burning shower'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/BurningShower.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'BurningShower.png'))
    elif(arg == 'supreme cannon'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/SupremeCannon.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'SupremeCannon.png'))
    elif(arg == 'desolation'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/Desolation.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Desolation.png'))
    elif(arg == 'iron frenzy'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/IronFrenzy.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'IronFrenzy.png'))
    elif(arg == 'vandal rage'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/VandalRage.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'VandalRage.png'))
    elif(arg == 'grim cobra'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/GrimCobra.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'GrimCobra.png'))
    elif(arg == 'vailent sniper'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/ValiantSniper.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'ValiantSniper.png'))
    elif(arg == 'delerium'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/Delerium.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Delerium.png'))
    elif(arg == 'overcompressed disintegration'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/OvercompressedDistegration.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'OvercompressedDistegration.png'))
    elif(arg == 'overheated heat bomb'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/OverheatedHeatBomb.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'OverheatedHeatBomb.png'))
    elif(arg == 'overloaded emp'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/OverloadedEMP.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'OverloadedEMP.png'))
    elif(arg == 'test1'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/topResistancePhysical.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'topResistancePhysical.png'))
    elif(arg == 'test2'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/topResistanceHeat.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'topResistanceHeat.png'))
    elif(arg == 'test3'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/topResistanceEnergy.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'topResistanceEnergy.png'))
#used to find the link of a youtuber
@client.command()
async def link(ctx, *, arg):
    if(arg == 'help'):
        link = discord.Embed(title = 'This is the !link help menu.')
        link.add_field(name = 'How to use it?', value = 'use it like this: !link (SmYoutuberName)\nFor example: !link firewater789')
        link.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await ctx.send(embed=link)
    elif(arg == 'firewater789'):
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
