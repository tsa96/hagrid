import os
import discord
from duckduckgo_search import ddg_images
import requests
import random
import shutil
from PIL import Image
import math
import unicodedata
import re
import asyncio
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
urls: list[str] = []

messages = [
    "Hey there! How's yer day going?",
    "Hey, just thinking about you and hoping all is well.",
    "I miss ya! How about we grab a butterbeer sometime soon?",
    "Hope you're having a magical day!",
    "Sending you some love and good vibes today!",
    "Thanks for being a great friend! You're the best.",
    "Thinking of you and hoping you're doing okay.",
    "Wishing you a wonderful day filled with happiness and joy!",
    "Hope you're ready for some fun and adventure, because I've got something planned!",
    "Sending you a big ol' hug from Hogwarts!",
    "You're a wizard, and don't you forget it!",
    "Hey, let's grab some pumpkin pasties together soon!",
    "You're the Ron to my Harry and the Hermione to my Ron. Thanks for being such a great friend!",
    "Fancy a game of wizard's chess, but with real life-sized pieces?",
    "I think I just saw a dragon sneeze fire and turn a tree into a marshmallow!",
    "I'm convinced that my pet Blast-Ended Skrewt is secretly a world-famous tap dancer.",
    "What if we charmed the pumpkin juice to taste like pumpkin pie, but also make you fly like a broomstick?",
    "I have a theory that Nifflers can talk, but they're just really shy.",
    "Let's take the Hogwarts Express on a joyride and see where it takes us!",
    "I bet I could train a flock of flobberworms to perform a rock concert.",
    "I think I accidentally brewed a potion that turns everything you touch into chocolate frogs.",
    "What if instead of flying on broomsticks, we flew on giant magical butterflies?",
    "I'm pretty sure the Forbidden Forest is secretly a giant ball pit.",
    "I've always wanted to try riding a hippogriff while eating ice cream.",
    "I bet I could knit a sweater for a Hungarian Horntail.",
    "What if we transfigured Hogwarts Castle into a giant trampoline park?",
    "I think I just discovered a new species of magical creature that sings lullabies to you when you're feeling down.",
    "I have a feeling that if we gave a Thestral a guitar, it would be a legendary rockstar.",
    "I heard a rumor that there's a secret room in the Hogwarts kitchen that's filled with unlimited chocolate frogs and butterbeer.",
    "I bet I could teach a giant squid how to paint portraits with its tentacles.",
    "I think I just saw a gnome do a backflip while juggling tomatoes.",
    "What if we played Quidditch, but with inflatable balls and a giant bouncy castle for a field?",
    "I'm pretty sure Fluffy the three-headed dog is secretly a karaoke superstar.",
    "Hey there, Harry! Your hair's looking a bit wild today. Want to try my new hair conditioner?",
    "You know what they say, 'the hairier, the better.' But with my new conditioner, your hair will be shiny and smooth in no time!",
    "I used to think the only thing more tangled than a Blast-Ended Skrewt was my hair, but not anymore!",
    "I've been testing out my new hair conditioner on Fang, and he's never looked better!",
    "I know my hair may not be the best example, but trust me, this stuff really works wonders.",
    "Looking for a hair product that's all-natural and won't hurt the environment? Look no further than Hagrid's Hair Helper!",
    "I can't promise you'll look like a Weasley, but my new hair conditioner will definitely make your hair softer and more manageable.",
    "I'm not just the Care of Magical Creatures professor, I'm also a hair care expert!",
    "You can't tame a Hungarian Horntail, but you can tame your hair with my new conditioner.",
    "Don't let bad hair days get you down. With Hagrid's Hair Helper, every day is a good hair day!",
    "Even dragons need good hair care, and my new conditioner is perfect for them too!",
    "I know my hair may be a bit unruly, but with my new conditioner, yours won't be!",
    "You don't need magic to have great hair. All you need is Hagrid's Hair Helper!",
    "Whether you have hair like a Niffler or a unicorn, my new conditioner can handle it all.",
    "My hair may be wild, but it's also my best advertisement for my new conditioner!",
    "I promise you'll be so impressed with my new hair conditioner, you'll want to name your next pet after it!",
    "My hair may not be perfect, but my new conditioner is.",
    "If you want hair that's soft, shiny, and smells like a field of fresh lavender, you need Hagrid's Hair Helper!",
    "The secret to my luscious locks? My new hair conditioner, of course!",
    "My new hair conditioner is so good, you'll feel like you're getting a magical makeover!",
    "Oh, hello Harry! Don't mind me, just doing a bit of spring cleaning!",
    "Hi there, Harry! Just taking out the trash, you know how it is.",
    "Oops! Looks like I've gotten myself into a bit of a pickle here.",
    "Hey Harry, would you mind giving me a hand? I seem to be a bit stuck.",
    "Don't mind me, Harry. I'm just experimenting with new ways to recycle!",
    "Well, this is a bit embarrassing. Mind not mentioning this to anyone, Harry?",
    "Hiya Harry! Just having a bit of a sit-down in the bin. It's quite cozy, really!",
    "Well, this is quite the predicament. I'll need a bit of help getting out of here, Harry!",
    "Hi Harry, do you know any spells that could help me get out of this bin?",
    "Whoops! Looks like I overestimated the size of this bin.",
    "Hello there, Harry! This is not quite how I intended to spend my afternoon.",
    "Ahem, Harry. I seem to have gotten myself into a bit of a jam here.",
    "Hello Harry, I'm just conducting a bit of an experiment with bin sizes. It's not going quite as planned...",
    "Don't mind me, Harry. I'm just taking a quick break from my usual activities!",
    "Hey there, Harry! Just trying to see if I can fit in this bin. Spoiler alert: I can't!",
    "Hiya Harry! Looks like I've gotten myself into a bit of a sticky situation here.",
    "Oh dear, Harry. I seem to have found myself in a bit of a tight spot.",
    "Hey Harry, you wouldn't happen to have a spare hand to help me out, would you?",
    "Hi Harry, don't worry about me. I'm just, um, doing some field research for the Care of Magical Creatures class.",
    "Hello there, Harry! I'm just taking a little break from my usual routine, as you can see!",
    "Hi there, Harry! Just having a bit of a swim with my new friend here.",
    "What a lovely day for a swim, isn't it? The water's just perfect.",
    "Oh, hello Harry! Just out for a bit of a swim and a splash with my new pal.",
    "This dolphin sure is friendly, Harry! It's been following me around all day.",
    "Don't mind me, Harry. I'm just showing my new friend the sights around Hogwarts.",
    "Isn't this dolphin just amazing, Harry? It's been doing all sorts of tricks for me!",
    "Hi there, Harry! Just trying to keep up with this speedy dolphin friend of mine.",
    "This dolphin seems to have taken a liking to me, Harry! Can you blame it?",
    "Isn't this just the best, Harry? A day spent swimming with my new aquatic friend.",
    "Don't worry about the dolphin, Harry. It's just having a bit of fun!",
    "Hiya Harry! Just out for a bit of a swim with my new aquatic pal.",
    "This dolphin is just the friendliest creature, Harry. It's been keeping me company all day.",
    "Hello Harry! I think I've made a new friend in this dolphin. It's been following me around for ages!",
    "Isn't this just the most fun, Harry? Swimming and playing with my new dolphin buddy.",
    "Don't mind the dolphin, Harry. It's just having a bit of fun in the water.",
    "This dolphin is just the best, Harry. It's been doing all sorts of tricks for me!",
    "Hi there, Harry! Just taking a break from my usual routine to swim with my new dolphin friend.",
    "Isn't this just the most magical thing, Harry? Swimming with a friendly dolphin in the Hogwarts lake!",
    "Don't worry, Harry. The dolphin is just playing a game of chase with me!",
    "Hello Harry! Just having a bit of fun in the water with my new dolphin pal. Want to join in?",
    "Hi there, Harry! Just having a bit of a swim with my new friend here.",
    "What a lovely day for a swim, isn't it? The water's just perfect.",
    "Oh, hello Harry! Just out for a bit of a swim and a splash with my new pal.",
    "This dolphin sure is friendly, Harry! It's been following me around all day.",
    "Don't mind me, Harry. I'm just showing my new friend the sights around Hogwarts.",
    "Isn't this dolphin just amazing, Harry? It's been doing all sorts of tricks for me!",
    "Hi there, Harry! Just trying to keep up with this speedy dolphin friend of mine.",
    "This dolphin seems to have taken a liking to me, Harry! Can you blame it?",
    "Isn't this just the best, Harry? A day spent swimming with my new aquatic friend.",
    "Don't worry about the dolphin, Harry. It's just having a bit of fun!",
    "Hiya Harry! Just out for a bit of a swim with my new aquatic pal.",
    "This dolphin is just the friendliest creature, Harry. It's been keeping me company all day.",
    "Hello Harry! I think I've made a new friend in this dolphin. It's been following me around for ages!",
    "Isn't this just the most fun, Harry? Swimming and playing with my new dolphin buddy.",
    "Don't mind the dolphin, Harry. It's just having a bit of fun in the water.",
    "This dolphin is just the best, Harry. It's been doing all sorts of tricks for me!",
    "Hi there, Harry! Just taking a break from my usual routine to swim with my new dolphin friend.",
    "Isn't this just the most magical thing, Harry? Swimming with a friendly dolphin in the Hogwarts lake!",
    "Don't worry, Harry. The dolphin is just playing a game of chase with me!",
    "Hello Harry! Just having a bit of fun in the water with my new dolphin pal. Want to join in?",
    "Hiya there, Harry! Just stopped by Jamba Juice for a refreshing and healthy treat.",
    "This Jamba Juice smoothie is just what I needed after a long day of teaching.",
    "Jamba Juice has so many tasty and nutritious options. You can't go wrong!",
    "Hello there, Harry! Just trying out some of Jamba Juice's delicious new flavors.",
    "If you're looking for a quick and healthy snack, Jamba Juice has got you covered.",
    "I always feel so energized after enjoying a Jamba Juice smoothie.",
    "Jamba Juice is the perfect pick-me-up on a hot summer day!",
    "Hi there, Harry! Just enjoying my favorite Jamba Juice smoothie before heading back to work.",
    "Jamba Juice has so many yummy options, I can never decide which to choose!",
    "Jamba Juice is my go-to for a quick and healthy snack on-the-go.",
    "I love that Jamba Juice uses all-natural ingredients in their smoothies.",
    "Hello, Harry! Just taking a break with a Jamba Juice smoothie in hand.",
    "Jamba Juice is a great way to treat yourself while still staying healthy.",
    "If you're in need of a refreshing drink, Jamba Juice is the way to go.",
    "I'm loving this new flavor of Jamba Juice smoothie. It's so delicious!",
]


def preload():
    images = ddg_images('hagrid', region='uk-en', safesearch='On', max_results=400)
    print('Fetched images')
    for image in images:
        url = image['image']
        name: str = url.split('/')[-1]
        urls.append(url)


def slugify(value, allow_unicode=False):
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


def get_hagrid():
    url = random.choice(urls)
    name = url.split('/')[-1]
    if not name.find('.jpg'):
        urls.remove(url)
    try:
        out_name = name.split('.jpg')[0] + '.jpg'
        path = os.getcwd() + '/hagrids/' + slugify(out_name) + '.jpg'
        print("fetching " + url)
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        del r
        image = Image.open(path)
        original_width = image.size[0]
        original_height = image.size[1]
        height = random.randint(20, 200)
        ratio = original_width / original_height
        width = math.floor(height * ratio)
        small_image = image.resize((width, height))
        out_height = math.floor(min(400, original_height) * random.normalvariate(1, 0.33))
        out_width = math.floor((out_height * ratio) * random.normalvariate(1, 0.33))
        image = small_image.resize((out_width, out_height), resample=Image.Resampling.NEAREST)
        print('saving ' + path)
        image.save(path)
        return path
    except Exception as instance:
        print(instance)
        print('failed getting this hagrid. trying again.......')
        urls.remove(url)
        return get_hagrid()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await post_hagrid()


async def post_hagrid():
    name = get_hagrid()
    print('posting ' + name)
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(file=discord.File(name))
    time = random.randint(1 * 60, 30 * 60)
    await asyncio.sleep(time)
    await post_hagrid()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id == 160192445307551744:
        await message.add_reaction("🦐")

    if message.author.id == 83091632596979712:
        await message.add_reaction(random.choice(["💕", "😍", "🥰", "😻", "💝", "💞", "💗", "🤗", "😸", "😄", "☺️"]))

    if message.content.startswith('hi hagrid'):
        await message.channel.send('hi! :)')

    elif message.content == 'hagrid, please fuck off':
        await message.channel.send('ok bye :(')
        exit()

    elif 'hagrid' in message.content.lower() and message.channel.id == 1080010705601843290:
        if message.author.id == 160192445307551744:
            await message.channel.send(random.choice(messages).upper().replace('.', '!') + random.randint(1, 8) * '!')
        else:
            await message.channel.send(random.choice(messages))

load_dotenv()
DISCORD_KEY = os.getenv('HAGRID_KEY')
CHANNEL_ID = os.getenv('HAGRID_CHANNEL_ID')
preload()
client.run(DISCORD_KEY)
