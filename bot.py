import discord
import colorama
import random
from discord.ext import commands, tasks
from itertools import cycle
from colorama import Back, Fore, Style

colorama.init(autoreset = False)

# Client settings

client = commands.Bot(command_prefix = '<')
client.remove_command('help')
status = cycle(['<list', '<help'])

# CMD events

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('wtf men')
	else:
		print(Fore.RED + 'some send a @ or an error is there')

@client.event
async def on_ready():
	change_status.start()
	print(Fore.GREEN + 'megs is awake :)')

@client.event
async def on_member_join(member):
	print(f'{member} has joined a server')

@client.event
async def on_member_remove(member):
	print(f'{member}has left a server')

# Admin commands

@client.command()
@commands.has_permissions(manage_messages=False)
async def clear(ctx, amount=10):
	await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(cfx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send('https://media.giphy.com/media/D8CVAhd6FZpyRTwSRD/giphy.gif')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(cfx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send('https://media.giphy.com/media/D8CVAhd6FZpyRTwSRD/giphy.gif')

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send('https://media1.tenor.com/images/c9b9079df42545425ef53c157a1def8f/tenor.gif?itemid=16626440')
			return

# Text commands

@client.command()
async def help(ctx):
	embed = discord.Embed(title = ':mouse:', description = '''
do [***<list***] for see list of commands

do [***<apps***] for see the apps made by @megs.''', color = discord.Colour.purple())

	embed.set_footer(icon_url = ctx.author.avatar_url, text = "if you've any questions -> megs.#4430")

	await ctx.send(embed = embed)

@client.command()
async def list(ctx):
	embed = discord.Embed(title = ':mouse:', description = '''
-  ***<clear*** (clears the messages memebers've send only works with permissions)

-  ***<kick*** (kick member only works with permissions)

-  ***<ban*** (ban member only works with permissions)

-  ***<unban*** (unban member only works with permissions)

-  ***<help*** (if you need help with the bot)

-  ***<list*** (shows a list of unlisted commands of the bot, [sex_ass], [hentai_ass] etc. are listed commands)

-  ***<apps*** (shows all apps made by @megs.)

-  ***<sex*** (shows a list of all [sex] commands only working in nsfw channel)

-  ***<penis*** (shows a random number from 3 to 30 how long your penis is, take it with humor!)

-  ***<error*** (shows a random gif of issues, trigger warning)

-  ***<ms*** (shows how fast the bot answers you)

-  ***<''', color = discord.Colour.purple())

	embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

	await ctx.send(embed = embed)	

@client.command()
async def apps(ctx):
	embed = discord.Embed(title = '''↓↓↓ all apps made by @megs. ↓↓↓''', description = '''https://github.com/MegzY1/MegsAll''', color = discord.Colour.purple())

	embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

	await ctx.send(embed = embed)

@client.command()
async def sex(ctx):
	embed = discord.Embed(title = ':revolving_hearts:', description = '''
wich type of sex you wanna c? (only works at nsfw channel)

***SEX***

- ***<sex_normal***

-  ***<sex_ass***

-  ***<sex_tits***

***HENTAI***

-  ***<hentai_normal***

-  ***<hentai_ass***

-  ***<hentai_tits***''', color = discord.Colour.purple())

	embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

	await ctx.send(embed = embed)

@client.command()
async def sex_normal(ctx):
	if ctx.channel.nsfw is True:
		answers = ['https://cdn.discordapp.com/attachments/335389582067630080/854754593010221126/image2.gif',
		'https://media.discordapp.net/attachments/831086995597557800/852119063256891432/sensual-and-amp-erotic_700.gif',
		'https://cdn.discordapp.com/attachments/335389582067630080/851884169951707176/25253528.gif',
		'https://cdn.discordapp.com/attachments/335389582067630080/851168733815635968/25248419.gif',
		'https://cdn.discordapp.com/attachments/335389582067630080/846098752187138048/25099626.gif']

		await ctx.send(random.choice(answers))
	else:
		embed = discord.Embed(title = ':no_entry_sign:', description = '''
***this is no nsfw channel***''', color = discord.Colour.purple())

		await ctx.send(embed = embed)

@client.command()
async def sex_ass(ctx):
	if ctx.channel.nsfw is True:
		answers = ['https://imgur.com/eW8Ew94',
		'https://media.discordapp.net/attachments/831086995597557800/852123158298624010/5FD1BF5.gif',
		'https://cdn.discordapp.com/attachments/335389524228046848/854062593576534056/25341621.gif',
		'https://cdn.discordapp.com/attachments/335389524228046848/854062565114118184/25323407.gif',
		'https://cdn.discordapp.com/attachments/335389524228046848/851883934265376808/25250817.gif']

		await ctx.send(random.choice(answers))
	else:
		embed = discord.Embed(title = ':no_entry_sign:', description = '''
***this is no nsfw channel***''', color = discord.Colour.purple())

		await ctx.send(embed = embed)

@client.command()
async def sex_tits(ctx):
	if ctx.channel.nsfw is True:
		answers = ['https://imgur.com/a/hHXkw7r',
		'https://imgur.com/a/N8Fq2H2',
		'https://cdn.discordapp.com/attachments/352894406208126979/852947536376889354/25308197.gif',
		'https://cdn.discordapp.com/attachments/352894406208126979/852947513761857536/25264734.gif',
		'https://cdn.discordapp.com/attachments/352894406208126979/850434187718688878/25238999.gif']

		await ctx.send(random.choice(answers))
	else:
		embed = discord.Embed(title = ':no_entry_sign:', description = '''
***this is no nsfw channel***''', color = discord.Colour.purple())

		await ctx.send(embed = embed)	

@client.command()
async def hentai_normal(ctx):
	if ctx.channel.nsfw is True:
		answers = ['https://cdn.discordapp.com/attachments/839880307779043428/844548636062122014/image4.jpg',
		'https://cdn.discordapp.com/attachments/839880307779043428/844548636062122014/image4.jpg',
		'https://cdn.discordapp.com/attachments/839880307779043428/854756205058588702/image1.jpg',
		'https://cdn.discordapp.com/attachments/839880307779043428/854756209991483412/image1.jpg',
		'https://cdn.discordapp.com/attachments/839880307779043428/854756217457213480/image1.jpg',
		'https://static1.e621.net/data/3c/c7/3cc753b655331deb34d643911835c447.gif',
		'https://cdn.discordapp.com/attachments/515208880272441374/854756471321133078/image2.jpg',
		'https://cdn.discordapp.com/attachments/209643667244318720/849905181024845854/23862559.gif',
		'https://cdn.discordapp.com/attachments/209643667244318720/852638837222277120/176a85c7e52bcffe5ff7bbd6b187e305.gif']

		await ctx.send(random.choice(answers))
	else:
		embed = discord.Embed(title = ':no_entry_sign:', description = '''
***this is no nsfw channel***''', color = discord.Colour.purple())

		await ctx.send(embed = embed)

@client.command()
async def hentai_ass(ctx):
	if ctx.channel.nsfw is True:
		answers = ['https://cdn.discordapp.com/attachments/515208880272441374/847431035229831168/image0.jpg',
		'https://cdn.discordapp.com/attachments/515208880272441374/844570736420192316/image2.jpg',
		'https://cdn.discordapp.com/attachments/515208880272441374/844570735913467924/image0.jpg',
		'https://cdn.discordapp.com/attachments/515208880272441374/844548968557969408/image0.gif',
		'https://cdn.discordapp.com/attachments/515208880272441374/844548960382877697/image0.gif',
		'https://cdn.discordapp.com/attachments/515208880272441374/844548506655260693/image1.jpg',
		'https://cdn.discordapp.com/attachments/515208880272441374/844541853621944339/image0.jpg']

		await ctx.send(random.choice(answers))
	else:
		embed = discord.Embed(title = ':no_entry_sign:', description = '''
***this is no nsfw channel***''', color = discord.Colour.purple())

		await ctx.send(embed = embed)

@client.command()
async def hentai_tits(ctx):
	if ctx.channel.nsfw is True:
		answers = ['https://cdn.discordapp.com/attachments/515208880272441374/840144729861390346/image1.jpg',
		'https://cdn.discordapp.com/attachments/515208880272441374/840144729609601044/image0.jpg',
		'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpUvg7CF97jSWr4Of28146KJm-uMxtSt-jkQ&usqp=CAU',
		'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQi-bRrAVi9K6Nshqi-P8RVJiQVXfPbB8t_RQ&usqp=CAU',
		'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzpbvpS7IO8er7rNsbxUaHySgg3wXFkhcK-A&usqp=CAU',
		'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTluIP3dVsIljqWvBOyNCj1C22-VkMpjNBL0g&usqp=CAU',
		'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUzPwecyz3t_s5diOYYSKv7FwrN85tD3HqcQ&usqp=CAU']

		await ctx.send(random.choice(answers))
	else:
		embed = discord.Embed(title = ':no_entry_sign:', description = '''
***this is no nsfw channel***''', color = discord.Colour.purple())

		await ctx.send(embed = embed)

@client.command()
async def penis(ctx):

	answers	= ['your penis is 3cm long ***3=D***',
	'your penis is ***5cm*** long ***3==D***',
	'your penis is ***6cm*** long ***3===D***',
	'your penis is ***8cm*** long ***3===D***',
	'your penis is ***11cm*** long ***3=====D***',
	'your penis is ***15cm*** long ***3========D***',
	'your penis is ***18cm*** long ***3===========D***',
	'your penis is ***21cm*** long ***3==============D***',
	'your penis is ***25cm*** long ***3================D***',
	'your penis is ***27cm*** long ***3====================D***',
	'your penis is ***30cm*** long ***3=======================D***']

	await ctx.send(random.choice(answers))

@client.command()
async def info(ctx):
	embed = discord.Embed(title = ':heart:***INFO***:heart:', description = '''
▹BoT VerSion : ***beta 1.0***

▹BoT CoDe : 

▹BoT CoDer : megs.#4430''', color = discord.Colour.purple())

		await ctx.send(embed = embed)

@client.command()
async def error(ctx):

	answers	= ['http://gph.is/1LBSZu5',
'https://gph.is/g/ZdL930Z',
'''```diff
- error```''']

	await ctx.send(random.choice(answers))

@client.command()
async def ms(ctx):

	await ctx.send(f'{round(client.latency * 1000)}ms')

# Activity loop

@tasks.loop(seconds=6)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)), status=discord.Status.dnd)

client.run('ODU1MTM3OTM3MjM5MDQ4MTky.YMuHQw.eZAig60cJp5wPcpINDJskMmuu6c')