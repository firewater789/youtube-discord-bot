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

youtubers = ['AEROST',
            'Alex2040 bR',
            'ambroise',
            'Atusiff',
            'bestplayeroftheworld',
            'BossParody SM',
            'Chinaski',
            'CHIPS',
            'CleverNameSM',
            'ClockLiuOG',
            'DOOM BRINGER',
            'Dwightx',
            'epicspeedster',
            'FAIOLA GAMES',
            'firewater789',
            'Fyrestare',
            'Hauer Horatio',
            'iDani RF',
            'JIYOON',
            'L4K3',
            'Laszeski',
            'Lookotza' ,
            'Madao san']

youtubers2 = ['MakeHappyVideos',
            'MAX GAMES',
            'Solitaire',
            'Moretusiff',
            'nullification zealot',
            'Pizza4UAndMe',
            'PRO Sm',
            'Purific',
            'Pyra Pinky-K',
            'Rambo Gaming',
            'S.A.M',
            'simpleon',
            'Smulated ace',
            'Stefan Ludak',
            'SuperMechs Helper',
            'tacocat',
            'Unlucky Joe',
            'WarrMachine',
            'WindForge',
            'WLGang Clan',
            'ZeRo',
            'Zoner']

fortuneBox = ['fortune box', 'fortune box legendary']

premiumBox = ['premium box', 'premium box legendary']

premiumPack = ['premium pack', 'premium pack legendary']

supremeChest = ['supreme chest', 'supreme chest legendary']

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

sideWeaponsPhysical = ['**physical [23]**',
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
                'last resort vulcan']

                
sideWeaponsHeat = ['**heat[28]**',
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
                'overcharged rocket battery']
                

sideWeaponsEnergy =['**Energy[26]**',  
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
            'valiant sniper',
            'delerium',
            'overcompressed disintegration',
            'overheated heat bomb',
            'overloaded emp']

drones = ['tonto'
            'firefly',
            'electrolyte',
            'void',
            'clash',
            'snack',
            'solar torch',
            'flame spear',
            'rail gun',
            'hurlbat',
            'nemo',
            'torment',
            'greedy',
            'swoop',
            'windforge',
            'dustmaker',
            'murmur',
            'anguish',
            'backstabber',
            'flamewave',
            'shockwave',
            'selfish protector',
            'backstabbing protector',
            'unreliable protector',
            'selfish guardian',
            'backstabbing guardian',
            'unreliable guardian',
            'heat point',
            'face shocker']

specials = ['advanced teleporter',
            'double teleporter',
            'charge engine',
            'superb charge engine',
            'platinum grappling hook',
            'flaming grappling hook',
            'shocking grapping hook']

modules = ['heat engine',
            'heat storage unit',
            'cooling mass booster',
            'energy engine',
            'energy storage unit',
            'energy mass booster',
            'quad core booster',
            'combined engine unit',
            'combined storage unit',
            'overload preventor',
            'platinum fortress',
            'mighty protector',
            'plasma fortress',
            'ultrahot protector',
            'electric fortress',
            'supercharge protector',
            'defence matrix',
            'maximum protector',
            'platinum plating']

mechs = ['god mode']

clan = ['wlgang flag', 'wlgang logo', 'wlgang logo with eye', 'trolls fast', 'reign']

other = ['token', 'legendary card', 'rank 1', 'rank 2', 'rank 3', 'rank 4', 'rank 5', 'rank 6', 'rank 7', 'rank 8', 'rank 9']

upgrade = ['rare banner', 'epic banner', 'legendary banner', 'mythical banner', 'divine banner', 
           'common power kit', 'rare power kit', 'epic power kit', 'legendary power kit', 'mass select']

backgrounds = ['background space', 'background snow', 'background cave', 'background junkyard', 'background tower', 
                      'background crane', 'background red desert', 'background unicorn', 'background forest', 'background desert']

buttons = ['arena button',
            'base button',
            'campaign button',
            'clan button',
            'raid button',
            'shop button',
            'upgrade button 1',
            'upgrade button 2',
            'workshop button']

#used to know when the bot goes online
@client.event
async def on_ready():
    main_channel = client.get_channel(803809420282822681)
    await main_channel.send('ready')
    print('Bot is active')

#used to find commands that the bot has
@client.command()
async def help(ctx):
        bot_channel = client.get_channel(810634146727723019)
        help = discord.Embed(title='These are the possible help commands.', 
        color=discord.Colour.dark_blue())
        help.add_field(name = '!png help', value = 'This will help you on how to use the **!png** command please do **!png help** to learn more', inline = False)
        help.add_field(name = '!link help', value = 'This will help you on how to use the **!link** command please do **!link help** to learn more', inline = False)
        help.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=help)

#used to find the ping of the bot
@client.command()
async def ping(ctx):
    bot_channel = client.get_channel(810634146727723019)
    ping=discord.Embed(title="What is my Ping?", description=f"My Ping is {round(client.latency * 1000)}ms", color=0xFF5733)
    ping.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
    await bot_channel.send(embed=ping)

#used to find png of stuff in the game
@client.command()
async def png(ctx, *, arg):
    bot_channel = client.get_channel(810634146727723019)
    if(arg == 'help'):
        png_help = discord.Embed(title = 'This is the !png help menu.')
        png_help.add_field(name = 'How to use it?', value = 'use it like this: !png (something)\nFor example: !png wlgang flag', inline = False)
        png_help.add_field(name = 'To Find all Possible Png Here are a few Commands.', value = '!png buttons\n!png items\n!png boxes\n!png mechs\n!png clan\n!png other\n!png upgrade\n!png backgrounds and floors', inline = False)
        png_help.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=png_help)
    elif(arg == 'torsos' or arg == 'torso'):
        png_torsos = discord.Embed(title = 'Torsos png', description = 'Here is a list of all torsos png that are in the code as of right now')
        png_torsos.add_field(name = 'Torsos', value = '\n'.join(torsos))
        png_torsos.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=png_torsos)
    elif(arg == 'legs' or arg == 'leg'):
        png_legs = discord.Embed(title = 'Legs png', description = 'Here is a list of all legs png that are in the code as of right now')
        png_legs.add_field(name = 'Legs', value = '\n'.join(legs))
        png_legs.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=png_legs)
    elif(arg == 'side weapons' or arg == 'side weapon'):
        png_sideWeapons = discord.Embed(title = 'side weapons commands', description = 'Here is a list of commands for side weapons')
        png_sideWeapons.add_field(name = 'side weapons', value = '!png side weapons physical\n!png side weapons heat\n!png side weapons energy')
        png_sideWeapons.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=png_sideWeapons)
    elif(arg == 'side weapons physical' or arg == 'side weapon physical'):
        png_sideWeaponsPhysical = discord.Embed(title = 'Physical Side Weapons png', description = 'Here is a list of all physical side weapons png that are in the code as of right now')
        png_sideWeaponsPhysical.add_field(name = 'Physical side weapons', value = '\n'.join(sideWeaponsPhysical))
        png_sideWeaponsPhysical.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=png_sideWeaponsPhysical)
    elif(arg == 'side weapons heat' or arg == 'side weapon heat'):
        png_sideWeaponsHeat = discord.Embed(title = 'Heat Side Weapons png', description = 'Here is a list of all heat side weapons png that are in the code as of right now')
        png_sideWeaponsHeat.add_field(name = 'Heat side weapons', value = '\n'.join(sideWeaponsHeat))
        png_sideWeaponsHeat.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=png_sideWeaponsHeat)
    elif(arg == 'side weapons energy' or arg == 'side weapon energy'):
        png_sideWeaponsEnergy = discord.Embed(title = 'Energy Side Weapons png', description = 'Here is a list of all energy side weapons png that are in the code as of right now')
        png_sideWeaponsEnergy.add_field(name = 'Energy side weapons', value = '\n'.join(sideWeaponsEnergy))
        png_sideWeaponsEnergy.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=png_sideWeaponsEnergy)
    elif(arg == 'top weapons' or arg == 'top weapon'):
        png_topWeapons = discord.Embed(title = 'Top Weapons png', description = 'Here is a list of all top weapons png that are in the code as of right now')
        png_topWeapons.add_field(name = 'top weapons', value = '\n'.join(topWeapons))
        png_topWeapons.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=png_topWeapons)
    elif(arg == 'drones' or arg == 'drone'):
        png_drones = discord.Embed(title = 'Drones png', description = 'Here is a list of all drones png that are in the code as of right now')
        png_drones.add_field(name = 'drones', value = '\n'.join(drones))
        png_drones.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=png_drones)
    elif(arg == 'specials' or arg == 'special'):
        png_specials = discord.Embed(title = 'Specials png', description = 'Here is a list of all specials png that are in the code as of right now')
        png_specials.add_field(name = 'specials', value = '\n'.join(specials))
        png_specials.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=png_specials)
    elif(arg == 'modules' or arg == 'module'):
        png_modules = discord.Embed(title = 'List of all torsos png', description = 'Here is a list of all box png that are in the code as of right now')
        png_modules.add_field(name = 'modules', value = '\n'.join(modules))
        png_modules.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=png_modules)
    elif(arg == 'mechs' or arg == 'mech'):
        png_mechs = discord.Embed(title = 'Modules png', description = 'Here is a list of all modules png that are in the code as of right now')
        png_mechs.add_field(name = 'mechs', value = '\n'.join(mechs))
        png_mechs.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=png_mechs)
    elif(arg == 'clan'):
        png_clan = discord.Embed(title = 'Clan png', description = 'Here is a list of all clan png that are in the code as of right now')
        png_clan.add_field(name = 'clan', value = '\n'.join(clan))
        png_clan.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=png_clan)
    elif(arg == 'upgrade'):
        png_clan = discord.Embed(title = 'upgrade png', description = 'Here is a list of all upgrade png that are in the code as of right now')
        png_clan.add_field(name = 'upgrade stuff', value = '\n'.join(upgrade))
        png_clan.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=png_clan)
    elif(arg == 'backgrounds and floors' or arg == 'backgrounds' or arg == 'floors' or arg == 'background' or arg == 'Background'):
        png_clan = discord.Embed(title = 'backgrounds and floors png', description = 'Here is a list of all backgrounds and floors png that are in the code as of right now')
        png_clan.add_field(name = 'backgrounds', value = '\n'.join(backgrounds))
        png_clan.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=png_clan)                
    elif(arg == 'boxes'):
        png_boxes = discord.Embed(title = 'Box png', description = 'Here is a list of all box png that are in the code as of right now')
        png_boxes.add_field(name = 'Fortune box', value = '\n'.join(fortuneBox), inline = True)
        png_boxes.add_field(name = 'Premium Box', value = '\n'.join(premiumBox), inline = True)
        png_boxes.add_field(name = 'Premium Pack', value = '\n'.join(premiumPack), inline = True)
        png_boxes.add_field(name = 'Supreme chest', value = '\n'.join(supremeChest), inline = True)
        png_boxes.add_field(name = 'Arena Boxes', value = '\n'.join(arenaBoxes), inline = True)
        png_boxes.add_field(name = 'Item and Sliver Boxes', value = '\n'.join(itemBoxes), inline = True)
        png_boxes.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=png_boxes)
    elif(arg == 'other'):
        png_other = discord.Embed(title = 'Other png', description = 'Here is a list of all of the other png that are in the code as of right now')
        png_other.add_field(name = 'Others', value = '\n'.join(other))
        png_other.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=png_other)
    elif(arg == 'button' or arg == 'buttons'):
        png_button = discord.Embed(title = 'Button png', description = 'Here is a list of all button png that are in the code as of right now')
        png_button.add_field(name = 'Buttons', value = '\n'.join(buttons))
        png_button.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=png_button)
    elif(arg == 'item' or arg == 'items'):
        png_items = discord.Embed(title = 'Item png', description = 'Here is a list of all item png that are in the code as of right now')
        png_items.add_field(name = 'Items', value = '!png torsos\n!png legs\n!png side weapon\n!png top weapon\n!png drone\n!png specials\n!png modules')
        png_items.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=png_items)

    elif(arg == 'item box' or arg == 'mix box'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/itemBox.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'itemBox.png'))
    elif(arg == 'item box legendary' or arg == 'mix box legendary'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/itemBoxLegendary.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'itemBoxLegendary.png'))
    #sliver box
    elif(arg == 'sliver box'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/silverBox.PNG") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'silverBox.PNG'))
    elif(arg == 'sliver box legendary'):
        await bot_channel.send('no png yet')
    #premium pack
    elif(arg == 'pack' or arg == 'premium pack'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/premiumPack.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'premiumPack.png'))
    elif(arg == 'premium pack legendary' or arg == 'pack legendary'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/premiumPackLegendary.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'premiumPackLegendary.png'))
    #premium box
    elif(arg == 'premium box'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/premiumBox.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'premiumBox.png'))
    elif(arg == 'premium box legendary'):
         async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/premiumBoxLegendary.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'premiumBoxLegendary.png'))
    #Supreme chest
    elif(arg == 'supreme chest'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/supremeChest.PNG") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'supremeChest.PNG'))
    elif(arg == 'supreme chest legendary'):
         async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/supremeChestLegendary.PNG") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'supremeChestLegendary.PNG'))
    #fortune box
    elif(arg == 'fortune box'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/fortuneBox.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'fortuneBox.png'))
    elif(arg == 'fortune box legendary'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/fortuneBoxLegendary.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'fortuneBoxLegendary.png'))
    #Arena Boxes
    elif(arg == 'rank 1 box'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/rankOneBox.PNG") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'rankOneBox.PNG'))
    elif(arg == 'rank 1 box legendary'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/rankOneBoxLegendary.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'rankOneBoxLegendary.png'))
    elif(arg == 'rank 3 box'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/rankThreeBox.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'rankThreeBox.png'))
    elif(arg == 'rank 3 box legendary'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/Boxes/rankThreeBoxLegendary.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'rankThreeBoxLegendary.png'))
    elif(arg == 'rank 5 box'):
        await bot_channel.send('no png yet')
    elif(arg == 'rank 5 box legendary'):
        await bot_channel.send('no png yet')
    elif(arg == 'rank 7 box'):
        await bot_channel.send('no png yet')
    elif(arg == 'rank 7 box legendary'):
        await bot_channel.send('no png yet')
    elif(arg == 'rank 10 box'):
        await bot_channel.send('no png yet')
    elif(arg == 'rank 10 box legendary'):
        await bot_channel.send('no png yet')
    elif(arg == 'rank 12 box'):
        await bot_channel.send('no png yet')
    elif(arg == 'rank 15 box'):
        await bot_channel.send('no png yet')
    elif(arg == 'rank 20 box'):
        await bot_channel.send('no png yet')
    elif(arg == 'rank 25 box'):
        await bot_channel.send('no png yet')
    #clan war box
    #WLGang stuff
    elif(arg == 'wlgang' or arg == 'wlgang logo' or arg == 'WLGang logo'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/wlgangLogo.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'wlgangLogo.png'))
    elif(arg == 'wlgang with eyes' or arg == 'wlgang logo with eyes' or arg == 'WLGang logo with eyes'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/wlgangLogowithEyes.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'wlgangLogowithEyes.png'))
    elif(arg == 'wlgang flag' or arg == 'WLGang flag'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/wlgangFlag.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'wlgangFlag.png'))
    elif(arg == 'reign'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/RR.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'RR.png'))
    elif(arg == 'trolls fast'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/trollsFast.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'trollsFast.png'))                      
    #mechs
    elif(arg == 'god mode'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/godMode.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'godMode.png'))
    #other
    elif(arg == 'logo' or arg == 'supermechs'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/supermechs.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'supermechs.png'))
    elif(arg == 'legendary card'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/legendaryCard.jpg") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'legendaryCard.jpg'))
    elif(arg == 'token'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/token.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'token.png'))   
    elif(arg == 'rank 1'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/r1.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'r1.png')) 
    elif(arg == 'rank 2'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/r2.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'r2.png')) 
    elif(arg == 'rank 3'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/r3.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'r3.png')) 
    elif(arg == 'rank 4'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/r4.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'r4.png'))   
    elif(arg == 'rank 5'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/r5.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'r5.png')) 
    elif(arg == 'rank 6'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/r6.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'r6.png'))   
    elif(arg == 'rank 7'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/r7.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'r7.png')) 
    elif(arg == 'rank 8'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/r8.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'r8.png'))
    elif(arg == 'rank 9'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/r9.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'r9.png'))  
    #upgrade stuff                   
    elif(arg == 'common power kit'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/commonPowerKit.PNG") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'commonPowerKit.PNG'))
    elif(arg == 'rare power kit'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/rarePowerKit.PNG") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'rarePowerKit.PNG'))
    elif(arg == 'epic power kit'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/epicPowerKit.PNG") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'epicPowerKit.PNG'))
    elif(arg == 'legendary power kit'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/legendaryPowerKit.PNG") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'legendaryPowerKit.PNG'))
    elif(arg == 'mass select'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/massSelect.jpg") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'massSelect.jpg'))  
    elif(arg == 'rare banner'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/RareBanner.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'RareBanner.png'))
    elif(arg == 'epic banner'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/EpicBanner.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'EpicBanner.png'))
    elif(arg == 'legendary banner'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/LegendaryBanner.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'LegendaryBanner.png'))
    elif(arg == 'mythical banner'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/MythicalBanner.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'MythicalBanner.png'))                
    elif(arg == 'divine banner'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/DivineBanner.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'DivineBanner.png'))         
    #Backgrounds
    elif(arg == 'background 1' or arg == 'background space'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/1.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, '1.png')) 
    elif(arg == 'background 2' or arg == 'background snow'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/2.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, '2.png'))   
    elif(arg == 'background 3' or arg == 'background cave'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/3.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, '3.png')) 
    elif(arg == 'background 4' or arg == 'background junkyard'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/4.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, '4.png'))   
    elif(arg == 'background 5' or arg == 'background tower'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/5.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, '5.png')) 
    elif(arg == 'background 6' or arg == 'background crane'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/6.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, '6.png')) 
    elif(arg == 'background 7' or arg == 'background red desert'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/7.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, '7.png')) 
    elif(arg == 'background 8' or arg == 'background unicorn'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/8.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, '8.png'))   
    elif(arg == 'background 9' or arg == 'background forest'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/9.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, '9.png')) 
    elif(arg == 'background 10' or arg == 'background desert'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/10.png") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, '10.png'))
    #Buttons
    elif(arg == 'clan button'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/clan.png.PNG") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'clan.png.PNG'))
    elif(arg == 'arena button'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/arena.png.PNG") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'arena.png.PNG'))
    elif(arg == 'base button'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/base.png.PNG") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'base.png.PNG'))
    elif(arg == 'upgrade button' or arg == 'upgrade button 1'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/upgrade.png.PNG") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'upgrade.png.PNG'))
    elif(arg == 'upgrade button 2'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/upgrade2.png.PNG") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'upgrade2.png.PNG'))
    elif(arg == 'workshop button' or arg == 'work shop button'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/workshop.png.PNG") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'workshop.png.PNG'))
    elif(arg == 'shop button'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/shop.png.PNG") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'shop.png.PNG'))
    elif(arg == 'campaign button'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/campaign.png.PNG") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'campaign.png.PNG'))
    elif(arg == 'raid button'):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/other/raid.png.PNG") as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'raid.png.PNG'))
    #Torsos
    elif(arg == 'interceptor'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/Interceptor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Interceptor.png'))
    elif(arg == 'nightmare'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/Nightmare.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Nightmare.png'))
    elif(arg == 'sith'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/Sith.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Sith.png'))
    elif(arg == 'archimond' or arg == 'arch'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/Archimonde.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Archimonde.png'))
    elif(arg == 'avenger'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/Avenger.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Avenger.png'))
    elif(arg == 'energy free armor' or arg == 'efa' or arg == 'EFA'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/EnergyFreeArmor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'EnergyFreeArmor.png'))
    elif(arg == 'hollow spectral armor' or arg == 'physical monkey' or arg == 'HSA' or arg == 'hsa'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/HollowSpectralArmor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'HollowSpectralArmor.png'))
    elif(arg == 'hollow cyber armor' or arg == 'physical cyber' or arg == 'hca' or arg == 'HCA'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/HollowCyberArmor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'HollowCyberArmor.png'))
    elif(arg == 'rusty energy armor' or arg == 'energy monkey' or arg == 'rea' or arg == 'REA'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/RustyEnergyArmor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'RustyEnergyArmor.png'))
    elif(arg == 'rusty cyber armor' or arg == 'energy cyber' or arg == 'rca' or arg == 'RCA'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/RustyCyberArmor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'RustyCyberArmor.png'))
    elif(arg == 'fractured heat armor' or arg == 'heat monkey' or arg == 'fha' or arg == 'FHA'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/FracturedHeatArmor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'FracturedHeatArmor.png'))
    elif(arg == 'fractured cyber armor' or arg == 'heat cyber' or arg == 'fca' or arg == 'FCA'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/FracturedCyberArmor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'FracturedCyberArmor.png'))
    elif(arg == 'hardened platinum vest' or arg == 'physical vest' or arg == 'hpv' or arg == 'HPV'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/HardenedPlatinumVest.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'HardenedPlatinumVest.png'))
    elif(arg == 'molten platinum vest' or arg == 'heat vest' or arg == 'mpv' or arg == 'MPV'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/MoltenPlatinumVest.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'MoltenPlatinumVest.png'))
    elif(arg == 'lightning platinum vest' or arg == 'energy vest' or arg == 'lpv' or arg == 'LPV'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/LightningPlatinumVest.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'LightningPlatinumVest.png'))
    elif(arg == 'battery armor' or arg == 'ba' or arg == 'BA'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/BatteryArmor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'BatteryArmor.png'))
    elif(arg == 'flame battery armor' or arg == 'fba' or arg == 'FBA'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/FlamingBatteryArmor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'FlamingBatteryArmor.png'))
    elif(arg == 'energy battery armor' or arg == 'eba' or arg == 'EBA'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/EnergyBatteryArmor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'EnergyBatteryArmor.png'))
    elif(arg == 'naga'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/Naga.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Naga.png'))
    elif(arg == 'zarkares' or arg == 'zark'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/Zarkares.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Zarkares.png'))
    elif(arg == 'sabretooth'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/Sabretooth.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Sabretooth.png'))
    elif(arg == 'windigo'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/Windigo.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Windigo.png'))
    elif(arg == 'brutality'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/Brutality.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Brutality.png'))
    elif(arg == 'grim reaper' or arg == 'gr' or arg == 'GR'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/torso/GrimReaper.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'GrimReaper.png'))
    #legs [15]
    elif(arg == 'massive stone feet' or arg == 'msf' or arg == 'MSF'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/MassiveStoneFeet.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'MassiveStoneFeet.png'))
    elif(arg == 'massive lava feet' or arg == 'mlf' or arg == 'MLF'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/MassiveLavaFeet.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'MassiveLavaFeet.png'))
    elif(arg == 'massive shocker feet'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/MassiveShockerFeet.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'MassiveShockerFeet.png'))
    elif(arg == 'iron boots' or arg == 'ib' or arg == 'IB'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/IronBoots.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'IronBoots.png'))
    elif(arg == 'scorching feet' or arg == 'sf' or arg == 'SF'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/ScorchingFeet.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'ScorchingFeet.png'))
    elif(arg == 'charged walkers' or arg == 'cw' or arg == 'CW'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/ChargedWalkers.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'ChargedWalkers.png'))
    elif(arg == 'grave diggers'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/GraveDiggers.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'GraveDiggers.png'))
    elif(arg == 'dynamic stompers'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/DynamicStompers.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'DynamicStompers.png'))
    elif(arg == 'recoil stompers'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/RecoilStompers.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'RecoilStompers.png'))
    elif(arg == 'dynamite boots'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/DynamiteBoots.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'DynamiteBoots.png'))
    elif(arg == 'lightning supporters'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/LightningSupporters.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'LightningSupporters.png'))
    elif(arg == 'devouring paws'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/DevouringPaws.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'DevouringPaws.png'))
    elif(arg == 'the claw' or arg == 'claw'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/TheClaw.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'TheClaw.png'))
    elif(arg == 'rolling beasts'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/RollingBeasts.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'RollingBeasts.png'))
    elif(arg == 'sparked runners'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/legs/SparkedRunners.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'SparkedRunners.png'))                 
    elif(arg == 'perimeter protector'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/PerimeterProtector.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'PerimeterProtector.png'))
    elif(arg == 'back breaker'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BackBreaker.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'BackBreaker.png'))
    elif(arg == 'disintegration'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/Disintegration.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Disintegration.png'))
    elif(arg == 'war hammer'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/WarHammer.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'WarHammer.png'))
    elif(arg == 'seraphblade'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/SeraphBlade.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'SeraphBlade.png'))
    elif(arg == 'rock recoiler'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/RockRecoiler.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'RockRecoiler.png'))
    elif(arg == 'annihilation'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/Annihilation.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Annihilation.png'))
    elif(arg == 'mercy'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/Mercy.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Mercy.png'))
    elif(arg == 'advanced repulser'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/AdvancedRepulser.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'AdvancedRepulser.png'))
    elif(arg == 'armor annihilator'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/ArmorAnnihilator.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'ArmorAnnihilator.png'))
    elif(arg == 'sacrifice cannon'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/SacrificeCannon.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'SacrificeCannon.png'))
    elif(arg == 'purifier'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/Purifier.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Purifier.png'))
    elif(arg == 'unrepaired laser cannon'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/UnrepairedLaserCannon.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'UnrepairedLaserCannon.png'))
    elif(arg == 'nightfall'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/NightFall.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'NightFall.png'))
    elif(arg == 'bloodweep'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BloodWeep.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'BloodWeep.png'))
    elif(arg == 'terror cry'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/TerrorCry.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'TerrorCry.png'))
    elif(arg == 'dark eagle'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/DarkEagle.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'DarkEagle.png'))
    elif(arg == 'malfunctitoning blaster'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/MalfunctioningBlaster.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'MalfunctioningBlaster.png'))
    elif(arg == 'sweetie'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/Sweetie.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Sweetie.png'))
    elif(arg == 'ejection blast'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/EjectionBlast.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'EjectionBlast.png'))
    elif(arg == 'last resort vulcan'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/LastResortVulcan.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'LastResortVulcan.png'))
    elif(arg == 'damaged armor annihilator'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/DamagedArmorAnnihilator.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'DamagedArmorAnnihilator.png'))
    elif(arg == 'rock polisher'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/RockPolisher.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'RockPolisher.png'))
        
    #heat [28]
    elif(arg == 'distance controller'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/DistanceController.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'DistanceController.png'))
    elif(arg == 'heronmark'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/HeronMark.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'HeronMark.png'))
    elif(arg == 'terrorblade'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/TerrorBlade.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'TerrorBlade.png'))
    elif(arg == 'flamimg hammer'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/FlamingHammer.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'FlamingHammer.png'))
    elif(arg == 'overcooking oven'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/OvercookingOven.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'OvercookingOven.png'))
    elif(arg == 'chaos bringer'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/ChaosBringer.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'ChaosBringer.png'))
    elif(arg == 'crimson rapture'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/CrimsonRapture.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'CrimsonRapture.png'))
    elif(arg == 'reckoning'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/Reckoning.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Reckoning.png'))
    elif(arg == 'magma recoiler'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/MagmaRecoiler.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'MagmaRecoiler.png'))
    elif(arg == 'basalt dissolver'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BasaltDissolver.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'BasaltDissolver.png'))
    elif(arg == 'broken devourer'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BrokenDevourer.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'BrokenDevourer.png'))
    elif(arg == 'magma blast'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/MagmaBlast.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'MagmaBlast.png'))
    elif(arg == 'sorrow'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/Sorrow.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Sorrow.png'))
    elif(arg == 'abomination'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/Abomination.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Abomination.png'))
    elif(arg == 'heat bomb'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/HeatBomb.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'HeatBomb.png'))
    elif(arg == 'shadow wolf'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/ShadowWolf.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'ShadowWolf.png'))
    elif(arg == 'explosive retreat'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/ExplosiveRetreat.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'ExplosiveRetreat.png'))
    elif(arg == 'rusty heat blaster'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/RustyHeatBlaster.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'RustyHeatBlaster.png'))
    elif(arg == 'flaminator'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/Flaminator.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Flaminator.png'))
    elif(arg == 'hybrid heat cannon'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/HybridHeatCannon.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'HybridHeatCannon.png'))
    elif(arg == 'corrupt light'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/CorruptLight.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'CorruptLight.png'))
    elif(arg == 'dawnblaze'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/DawnBlaze.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'DawnBlaze.png'))
    elif(arg == 'cracked plasma cannon'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/CrackedPlasmaCannon.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'CrackedPlasmaCannon.png'))
    elif(arg == 'basalt polisher'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BasaltPolisher.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'BasaltPolisher.png'))
    elif(arg == 'misguided rocket battery'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/MisguidedRocketBattery.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'MisguidedRocketBattery.png'))
    elif(arg == 'fractured basalt annihilator'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/_1.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, '_1.png'))
    elif(arg == 'fractured basalt dissolver'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/_%20(12).png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, '_%20(12).png'))
    elif(arg == 'overcharged rocket battery' ):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/OverchargedRocketBattery.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'OverchargedRocketBattery.png'))

    #energy[26]
    elif(arg == 'distance generator'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/DistanceGenerator.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'DistanceGenerator.png'))
    elif(arg == 'unstable power cell' or arg == 'upc'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/UnstablePowerCell.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'UnstablePowerCell.png'))
    elif(arg == 'brightroar' or arg == 'bright roar'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BrightRoar.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'BrightRoar.png'))
    elif(arg == 'bigdaddy'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BigDaddy.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'BigDaddy.png'))
    elif(arg == 'stormweaver'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/StormWeaver.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'StormWeaver.png'))
    elif(arg == 'ash creator'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/AshCreator.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'AshCreator.png'))
    elif(arg == 'viking hammer'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/VikingHammer.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'VikingHammer.png'))
    elif(arg == 'lightning recoiler'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/LightningRecoiler.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'LightningRecoiler.png'))
    elif(arg == 'bulldog'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BullDog.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'BullDog.png'))
    elif(arg == 'blizzard dissolver'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BlizzardDissolver.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'BlizzardDissolver.png'))
    elif(arg == 'drunk lightning'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/DrunkLightning.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'DrunkLightning.png'))
    elif(arg == 'emp'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/EMP.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'EMP.png'))
    elif(arg == 'mortal bullet'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/MortalBullet.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'MortalBullet.png'))
    elif(arg == 'last words'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/LastWords.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'LastWords.png'))
    elif(arg == 'bunker shell'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BunkerShell.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'BunkerShell.png'))
    elif(arg == 'piercing fox'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/PiercingFox.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'PiercingFox.png'))
    elif(arg == 'evac spark'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/EvacSpark.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'EvacSpark.png'))
    elif(arg == 'scrapped energy blaster'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/ScrappedEnergyBlaster.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'ScrappedEnergyBlaster.png'))
    elif(arg == 'malice beam'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/MaliceBeam.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'MaliceBeam.png'))
    elif(arg == 'ultrabright'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/UltraBright.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'UltraBright.png'))
    elif(arg == 'hot flash'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/HotFlash.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'HotFlash.png'))
    elif(arg == 'hybrid energy cannon'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/HybridEnergyCannon.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'HybridEnergyCannon.png'))
    elif(arg == 'lightning cutter'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/LightningCutter.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'LightningCutter.png'))
    elif(arg == 'obsolete energy cannon'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/ObsoleteEnergyCannon.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'ObsoleteEnergyCannon.png'))
    elif(arg == 'broken blizzard dissolver'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/BrokenBlizzardDissolver.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'BrokenBlizzardDissolver.png'))
    elif(arg == 'broken blizzard annihilator'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/side%20weapons/__.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, '__.png'))
    elif(arg == 'frantic brute'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/FranticBrute.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'FranticBrute.png'))
    elif(arg == 'frantic flame'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/FranticFlame.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'FranticFlame.png'))
    elif(arg == 'frantic lightning'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/FranticLightning.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'FranticLightning.png'))
    elif(arg == 'reckless beam'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/RecklessBeam.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'RecklessBeam.png'))
    elif(arg == 'savagery'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/Savagery.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Savagery.png'))
    elif(arg == 'hysteria'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/Hysteria.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Hysteria.png'))
    elif(arg == 'distance shredder'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/DistanceShredder.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'DistanceShredder.png'))
    elif(arg == 'space invader'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/SpaceInvader.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'SpaceInvader.png'))
    elif(arg == 'party crasher'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/PartyCrasher.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'PartyCrasher.png'))
    elif(arg == 'mighty cannon'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/MightyCannon.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'MightyCannon.png'))
    elif(arg == 'desert snake'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/DesertSnake.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'DesertSnake.png'))
    elif(arg == 'spinefall'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/SpineFall.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'SpineFall.png'))
    elif(arg == 'cockpit piercer'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/CockpitPiercer.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'CockpitPiercer.png'))
    elif(arg == 'cockpit electrocuter'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/CockpitElectrocuter.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'CockpitElectrocuter'))
    elif(arg == 'cockpit burner'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/CockpitBurner.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'CockpitBurner.png'))
    elif(arg == 'falcon'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/Falcon.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Falcon.png'))
    elif(arg == 'lightning scope'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/LightningScope.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'LightningScope.png'))
    elif(arg == 'flaming scope'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/FlamingScope.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'FlamingScope.png'))
    elif(arg == 'lazy falcon'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/LazyFalcon.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'LazyFalcon.png'))
    elif(arg == 'half brunt scope'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/HalfBurntScope.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'HalfBurntScope.png'))
    elif(arg == 'electrocuted scope'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/ElectrocutedScope.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'ElectrocutedScope.png'))
    elif(arg == 'night eagle'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/NightEagle.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'NightEagle.png'))
    elif(arg == 'spartan carnage'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/SpartanCarnage.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'SpartanCarnage.png'))
    elif(arg == 'desert fury'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/DesertFury.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'DesertFury.png'))
    elif(arg == 'red rain'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/RedRain.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'RedRain.png'))
    elif(arg == 'burning shower'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/BurningShower.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'BurningShower.png'))
    elif(arg == 'supreme cannon'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/SupremeCannon.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'SupremeCannon.png'))
    elif(arg == 'desolation'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/Desolation.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Desolation.png'))
    elif(arg == 'iron frenzy'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/IronFrenzy.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'IronFrenzy.png'))
    elif(arg == 'vandal rage'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/VandalRage.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'VandalRage.png'))
    elif(arg == 'grim cobra'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/GrimCobra.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'GrimCobra.png'))
    elif(arg == 'valiant sniper'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/ValiantSniper.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'ValiantSniper.png'))
    elif(arg == 'delerium'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/Delerium.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'Delerium.png'))
    elif(arg == 'overcompressed disintegration'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/OvercompressedDistegration.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'OvercompressedDistegration.png'))
    elif(arg == 'overheated heat bomb'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/OverheatedHeatBomb.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'OverheatedHeatBomb.png'))
    elif(arg == 'overloaded emp'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/OverloadedEMP.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'OverloadedEMP.png'))
    elif(arg == 'test1'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/topResistancePhysical.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'topResistancePhysical.png'))
    elif(arg == 'test2'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/topResistanceHeat.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'topResistanceHeat.png'))
    elif(arg == 'test3'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/top%20weapon/topResistanceEnergy.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await bot_channel.send(file=discord.File(data, 'topResistanceEnergy.png'))
            
            #drones

    elif(arg == 'tonto'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/Tonto.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Tonto.png'))
    elif(arg == 'firefly'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/FireFly.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'FireFly.png'))
    elif(arg == 'electrolyte'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/Electrolyte.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Electrolyte.png'))
    elif(arg == 'void'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/Void.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Void.png'))
    elif(arg == 'clash'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/Clash.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Clash.png'))
    elif(arg == 'snack'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/Snack.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Snack.png'))
    elif(arg == 'solar torch'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/SolarTorch.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'SolarTorch.png'))
    elif(arg == 'flamespear'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/FlameSpear.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'FlameSpear.png'))
    elif(arg == 'rail gun'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/RailGun.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'RailGun.png'))
    elif(arg == 'hurlbat'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/HurlBat.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'HurlBat.png'))
    elif(arg == 'nemo'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/Nemo.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Nemo.png'))
    elif(arg == 'torment'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/Torment.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Torment.png'))
    elif(arg == 'greedy'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/Greedy.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Greedy.png'))
    elif(arg == 'swoop'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/Swoop.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Swoop.png'))
    elif(arg == 'windforge'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/WindForge.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'WindForge.png'))
    elif(arg == 'dustmaker'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/DustMaker.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'DustMaker.png'))
    elif(arg == 'murmur'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/Murmur.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Murmur.png'))
    elif(arg == 'anguish'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/Anguish.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Anguish.png'))
    elif(arg == 'backstabber'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/Backstabber.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Backstabber.png'))
    elif(arg == 'flamewave'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/FlameWave.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'FlameWave.png'))
    elif(arg == 'shockwave'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/Shockwave.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'Shockwave.png'))
    elif(arg == 'selfish protector'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/SelfishProtector.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'SelfishProtector.png'))
    elif(arg == 'backstabbing protector'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/BackstabbingProtector.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'BackstabbingProtector.png'))
    elif(arg == 'unreilable protector'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/UnreliableProtector.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'UnreliableProtector.png'))
    elif(arg == 'selfish guardian'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/SelfishGuardian.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'SelfishGuardian.png'))
    elif(arg == 'backstabbing guardian'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/BackstabbingGuardian.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'BackstabbingGuardian.png'))
    elif(arg == 'unreilable guardian'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/UnreliableGuardian.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'UnreliableGuardian.png'))
    elif(arg == 'heat point'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/HeatPoint.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'HeatPoint.png'))
    elif(arg == 'face shocker'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/drone/FaceShocker.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'FaceShocker.png'))
            #speicals 
    elif(arg == 'heat engine'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/HeatEngine.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'HeatEngine.png'))
    elif(arg == 'heat storage unit'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/HeatStorageUnit.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'HeatStorageUnit.png'))
    elif(arg == 'cooling mass booster'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/CoolingMassBooster.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'CoolingMassBooster.png'))
    elif(arg == 'energy engine'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/EnergyEngine.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'EnergyEngine.png'))
    elif(arg == 'energy storage unit'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/EnergyStorageUnit.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'EnergyStorageUnit.png'))
    elif(arg == 'energy mass booster'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/EnergyMassBooster.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'EnergyMassBooster.png'))
    elif(arg == 'quad core booster' or arg == 'qcb'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/QuadCoreBooster.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'QuadCoreBooster.png'))
    elif(arg == 'combined engine unit' or arg == 'ceu'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/CombinedEngineUnit.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'CombinedEngineUnit.png'))
    elif(arg == 'combined storage unit' or arg == 'csu'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/CombinedStorageUnit.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'CombinedStorageUnit.png'))
    elif(arg == 'overload preventor'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/OverloadPreventor.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'OverloadPreventor.png'))
    elif(arg == 'platinum fortress' or arg == 'physical fortress'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/PhysicalFortress.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'PhysicalFortress.png'))
    elif(arg == 'mighty protector'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/MightyProtector.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'MightyProtector.png'))
    elif(arg == 'plasma fortress' or arg == 'heat fortress'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/HeatFortress.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'HeatFortress.png'))
    elif(arg == 'ultrahot protector'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/UltrahotProtector.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'UltrahotProtector.png'))
    elif(arg == 'electric fortress' or arg == 'energy fortress'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/EnergyFortress.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'EnergyFortress.png'))
    elif(arg == 'supercharge protector'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/SuperChargeProtector.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'SuperChargeProtector.png'))
    elif(arg == 'defence matrix' or arg == 'maximum fortress'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/DefenceMatrix.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'DefenceMatrix.png'))
    elif(arg == 'maximum protector'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/MaximumProtector.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'MaximumProtector.png'))
    elif(arg == 'platinum plating'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/PlatinumPlating.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'PlatinumPlating.png'))
    elif(arg == 'platinum grappling hook'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/PlatinumGrapplingHook.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'PlatinumGrapplingHook.png'))
    elif(arg == 'flaming grappling hook'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/FlamingGrapplingHook.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'FlamingGrapplingHook.png'))
    elif(arg == 'shocking grappling hook'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/ShockingGrapplingHook.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'ShockingGrapplingHook.png'))
    elif(arg == 'double teleporter'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/DoubleTeleporter.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'DoubleTeleporter.png'))
    elif(arg == 'advanced teleporter'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/AdvancedTeleporter.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'AdvancedTeleporter.png'))
    elif(arg == 'charge engine' or arg == 'charge'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/ChargeEngine.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'ChargeEngine.png'))
    elif(arg == 'superb charge enginie' or arg == 'superb charge'):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/firewater789/youtube-discord-bot/main/modules/SuperbChargeEngine.png') as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'SuperbChargeEngine.png'))
#used to find the link of a youtuber
@client.command() 
async def link(ctx, *, arg):
    bot_channel = client.get_channel(810634146727723019)
    if(arg == 'list'):
        link_list = discord.Embed(title = 'This is the !link list menu.', color=discord.Colour.red())
        link_list.add_field(name = 'List 1', value = '\n'.join(youtubers), inline = True)
        link_list.add_field(name = 'List 2', value = '\n'.join(youtubers2), inline = True)
        link_list.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=link_list)                  
    elif(arg == 'help'):
        link = discord.Embed(title = 'This is the !link help menu.')
        link.add_field(name = 'How to use it?', value = 'use it like this: !link (SmYoutuberName)\nFor example: !link firewater789')
        link.set_footer(icon_url = ctx.author.avatar_url, text =f'Requested by: {ctx.author.name}')
        await bot_channel.send(embed=link)
    elif(arg == 'firewater789'):
        await bot_channel.send('https://www.youtube.com/channel/UCoku4b76Dhs-xZbrkmwidUQ')
    elif(arg == 'Atusiff' or arg == 'atusiff'):
        await bot_channel.send('https://www.youtube.com/channel/UCk4OvXT494YJWpdVaJwvWyQ')
    elif(arg == 'tacocat' or arg == 'naoki ogawa'):
        await bot_channel.send('https://www.youtube.com/channel/UCR86NR06Ur1MxaPYCTVk74Q')
    elif(arg == 'windforge' or arg == 'WindForge'):
        await bot_channel.send('https://www.youtube.com/channel/UCzsrFcyccu1FN3fBvpNDJnA')
    elif(arg == 'Pyra Pinky-K' or arg == 'pyra pinky' or arg == 'pyra pinky k'):
        await bot_channel.send('https://www.youtube.com/channel/UCT66b-SZCXkYm6ahSbiplVA')
    elif(arg == 'Lookotza' or arg == 'lookotza'):
        await bot_channel.send('https://www.youtube.com/channel/UC89sVdPFHtzib90X4vJJGtg')
    elif(arg == 'madao san'):
        await bot_channel.send('https://www.youtube.com/channel/UC1ItNEPxPV0IQJPGpvFez2Q')
    elif(arg == 'dwightx' or arg == 'Dwightx'):
        await bot_channel.send('https://www.youtube.com/channel/UCFGugxNDgF2LzL1ictmxDXQ')
    elif(arg == 'chinaski' or arg == 'Chinaski'):
        await bot_channel.send('https://www.youtube.com/user/DmDnDfD')
    elif(arg == 'Rambo Gaming' or arg == 'rambo gaming' or arg == 'rambo'):
        await bot_channel.send('https://www.youtube.com/channel/UCeOf32uACOWTLTxYAHnaOZA')
    elif(arg == 'L4K3 v' or arg == 'l4k3 v' or arg == 'lake' or arg == 'L4K3' or arg == 'l4k3'):
        await bot_channel.send('https://www.youtube.com/channel/UCgdMVzvwiE1NTBHm_tggGnA')
    elif(arg == 'Stefan Ludak' or arg == 'stefan ludak' or arg == 'stefan'):
        await bot_channel.send('https://www.youtube.com/channel/UCdYzUORe0HyC7UDE5y6TEiA')
    elif(arg == 'simpleon' or arg == 'yeet' or arg == 'yeet' or arg == 'Yeet'):
        await bot_channel.send('https://www.youtube.com/channel/UCsGYt995Qobe46uluJ_cCdg')
    elif(arg == 'Purific' or arg == 'purific'):
        await bot_channel.send('https://www.youtube.com/channel/UCWDulhcB8oJq80PNi5RCy5Q')
    elif(arg == 'CleverNameSM' or arg == 'clevername' or arg == 'clevernamesm'):
        await bot_channel.send('https://www.youtube.com/channel/UCwgZFzMbhNnppqRzIAVwQPA')
    elif(arg == 'ambroise'):
        await bot_channel.send('https://www.youtube.com/channel/UCzJL0bq22-EvX5RY9fUtVzQ')
    elif(arg == 'AEROST' or arg == 'aerost'):
        await bot_channel.send('https://www.youtube.com/channel/UCMicacPcFVmvTI2JfkUD5RA/videos')
    elif(arg == 'Alex2040 bR' or arg == 'alex2040'):
        await bot_channel.send('https://www.youtube.com/channel/UCQXq-AFvt-zDKzMHY5HJkwQ')
    elif(arg == 'bestplayeroftheworld'):
        await bot_channel.send('https://www.youtube.com/channel/UCd8Rd4aMvOEPrYkqSe8_XJg')
    elif(arg == 'BossParody SM' or arg == 'BossParody' or arg == 'bossparody'):
        await bot_channel.send('https://www.youtube.com/channel/UCvrnVpsuQmeHtP845PCXfHA')
    elif(arg == 'CHIPS' or arg == 'chips'):
        await bot_channel.send('https://www.youtube.com/channel/UCyqUTkIXoz2dbfySWg3Vi-g')
    elif(arg == 'ClockLiuOG' or arg == 'clockliuog' or arg == 'clockliu'):
        await bot_channel.send('https://www.youtube.com/channel/UCLWnnIyyZ0ZvvuLLEfikfxQ')
    elif(arg == 'DOOM BRINGER' or arg == 'doom bringer'):
        await bot_channel.send('https://www.youtube.com/channel/UCWTUp7ADNL7fVwRF_JUb0Aw/featured')
    elif(arg == 'epicspeedster'):
        await bot_channel.send('https://www.youtube.com/channel/UCYbL5QSlQuL3mqeQVlU25Dw')
    elif(arg == 'FAIOLA GAMES' or arg == 'faiola games' or arg == 'faiola'):
        await bot_channel.send('https://www.youtube.com/channel/UC0OsraC3NUb1WKvKc2UrWOg')
    elif(arg == 'Fyrestare' or arg == 'fyrestare'):
        await bot_channel.send('https://www.youtube.com/channel/UCa0xXEaj92pNPl3Vnc3hUUQ')
    elif(arg == 'Hauer Horatio' or arg == 'hauer horatio' or arg == 'Hauer' or arg == 'hauer'):
        await bot_channel.send('https://www.youtube.com/channel/UCPjCO3B-SHCoa_CWznChweA')
    elif(arg == 'iDani RF' or arg == 'iDani' or arg == 'idani'):
        await bot_channel.send('https://www.youtube.com/channel/UCrC2PCKk72iI9BJS6c6m3PA')
    elif(arg == 'JIYOON' or arg == 'jiyoon'):
        await bot_channel.send('https://www.youtube.com/channel/UCcl0Zx3wBLyPcQcjLFjqwmA')
    elif(arg == 'Laszeski' or arg == 'laszeski'):
        await bot_channel.send('https://www.youtube.com/channel/UCu8czDKpVyWI34SJrPEUqnQ')
    elif(arg == 'MakeHappyVideos' or arg == 'makehappyvideos'):
        await bot_channel.send('https://www.youtube.com/channel/UCrQWVFMk-RoJvEtMoZgzWOw')
    elif(arg == 'MAX GAMES' or arg == 'max games'):
        await bot_channel.send('https://www.youtube.com/channel/UClCQ-idlW1lcaCcf7Qb8YNQ')
    elif(arg == 'Maxx' or arg == 'warrmachine' or arg == 'WarrMachine'):
        await bot_channel.send('https://www.youtube.com/channel/UCgpqiDLRNMeS2G8rSfhKmfA')
    elif(arg == 'solitaire' or arg == 'Solitaire'):
        await bot_channel.send('https://www.youtube.com/channel/UCz1AL1Q0QlTzYPFCK8qaudw')
    elif(arg == 'Moretusiff' or arg =='moretusiff'):
        await bot_channel.send('https://www.youtube.com/channel/UCMDM8S1Riuf14AOvvC85JHQ')
    elif(arg == 'nullification zealot' or arg == 'nullification'):
        await bot_channel.send('https://www.youtube.com/channel/UCuw9Df6hBt0w729_EGM40tw')
    elif(arg == 'Pizza4UAndMe' or arg == 'pizza4uandme'):
        await bot_channel.send('https://www.youtube.com/channel/UCUDPQaSsYX6bFoPb2sSkKtw')
    elif(arg == 'PRO Sm' or arg == 'pro sm'):
        await bot_channel.send('https://www.youtube.com/channel/UCIDvTNjCT2v0ZKuwZbsXZtA')
    elif(arg == 'S.A.M' or arg == 's.a.m'):
        await bot_channel.send('https://www.youtube.com/channel/UCfr5truubiCZxqugvWfuyRA')
    elif(arg == 'Smulated ace' or arg == 'Smulated' or arg == 'smulated ace' or arg == 'smulated'):
        await bot_channel.send('https://www.youtube.com/channel/UC9eHwO-_ImkvyMy1MncUDQA')
    elif(arg == 'SuperMechs Helper' or arg == 'supermechs helper'):
        await cbot_channeltx.send('https://www.youtube.com/channel/UCwTlAgskjqJ6blYJH5JuSNg')
    elif(arg == 'Unlucky Joe' or arg == 'unlucky joe'):
        await bot_channel.send('https://www.youtube.com/channel/UCtV3vCHHpXUDgqoQdb8KIqA')
    elif(arg == 'WLGang Clan' or arg == 'wlgang clan'):
        await bot_channel.send('https://www.youtube.com/channel/UCo9ZZdvB6tI8-BBjf0349Kw')
    elif(arg == 'ZeRo' or arg == 'zero'):
        await bot_channel.send('https://www.youtube.com/channel/UCFLteDDcJ6Y7UFxulXJpbRA')
    elif(arg == 'Zoner' or arg == 'zoner'):
        await bot_channel.send('https://www.youtube.com/channel/UCNhmVDtEb6sC1lS0tUGZH3A')
    else:
        link=discord.Embed(title='Invailed Name', 
        description='The name you entered is a invailed name or maybe you typed it wrong.\nFor Example:\ninstead of typing Firewater789 try firewater789',
        color=0xFF5733)
        await bot_channel.send(embed=link)

#Rum the client on the server
client.run(token)
