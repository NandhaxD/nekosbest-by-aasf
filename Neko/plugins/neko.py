import requests
import time
import random
from Neko import bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

PM_START_TEXT = """
**Welcome** {}~kun ฅ(≈>ܫ<≈)
`I'm A Neko Themed Telegram Bot Using Nekos.best! `
**Make Your Groups Active By Adding Me There! ××**
"""

OWO = (
    "*Neko pats {} on the head.",
    "*gently rubs {}'s head*.",
    "*Neko mofumofus {}'s head*",
    "*Neko messes up {}'s head*",
    "*Neko intensly rubs {}'s head*",
    "*{}'s waifu pats their head*",
    "*{}'s got free headpats*",
    "No pats for {}!",
)

aasf = (
 "(*)^(*) *lazy arrival* zzzZZ(Z){}-kun I'm hungry...",
 "OwO why are calling me *wags tail in excitement* {} Do you have have cookies?",
 "^~^ *peeks by wall* Oh! {} Meowwww",
 "Ara Ara! {} Do you wanna play? *raises cat ears* ^attentive^",
 "($^$) *money face* {} are you rich UwU?",
 "Hello UwU {} I'm here to play, Meow"
)

help_text = """
• **Kiss : **`Neko kiss | /kiss To Kiss A Person`
• **Highfive : **`Neko highfive | /highfive To Highfive A Person`
• **Happy : **`Neko happy | /happy To Makes A Person Happy`
• **Laugh : **`Neko laugh | /laugh To Makes A Person Laugh`
• **Bite : **`Neko bite | /bite To Bite A Person`
• **Poke : **`Neko poke | /poke To Poke A Person`
• **Tickle : **`Neko tickle | /tickle To Tickle A Person`
• **Wave : **`Neko wave | /wave To Wave A Person`
• **Thumbsup : **`Neko thumbsup | /thumbsup To Thumbsup A Person`
• **Stare : **`Neko stare | /stare To Makes A Person Stare`
• **Cuddle : **`Neko cuddle | /cuddle To Cuddle A Person`
• **Smile : **`Neko smile | /smile To Makes A Person Smile`
• **Baka : **`Neko baka | /baka To Say A Person Baka`
• **Blush : **`Neko blush | /blush To Makes A Person Blush`
• **Think : **`Neko think | /think To Makes A Person Think`
• **Pout : **`Neko pout | /pout To Makes A Person Pout`
• **Facepalm : **`Neko facepalm | /facepalm To Makes A Person Facepalm`
• **Wink : **`Neko wink | /wink To Makes A Person Wink`
• **Smug : **`Neko smug | /smug To Makes A Person Smug`
• **Cry : **`Neko cry | /cry To Makes A Person Cry`
• **Dance : **`Neko dance | /dance To Makes A Person Dance`
• **Feed : **`Neko feed | /feed To Feed A Person`
• **Shrug : **`Neko shrug | /shrug To Shrug A Person`
• **Bored : **`Neko bored | /bored To Makes A Person Bored`
• **Pat : **`Neko pat | /pat To Pat A Person`
• **Hug : **`Neko hug | /hug To Hug A Person`
• **Slap : **`Neko slap | /slap To Slap A Person`
• **Cute : **`Neko cute | /cute To Say Me Cute`
• **Waifu : **`Neko waifu | /waifu To Send Random Waifu Image`
• **Kitsune : **`Neko kitsune | /kitsune To Send Random Kitsune Image`
• **Sleep : **`Neko sleep | /sleep To Say I Am Going To Sleep`
• **Neko : **`Neko | /neko To Get Random Neko quotes`
"""

@bot.on_message(filters.regex("Neko kiss") & filters.command("kiss"))
async def kiss(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/kiss"
       r = requests.get(url)
       e = r.json()
       kissme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(kissme, caption="*{} kisses {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/kiss"
      r = requests.get(url)
      e = r.json()
      kissme = e["results"][0]["url"]
      await message.reply_video(kissme, caption="*Kisses u with all my love*~")
      return

@bot.on_message(filters.regex("Neko highfive") & filters.command("highfive"))
async def highfive(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/highfive"
       r = requests.get(url)
       e = r.json()
       highfiveme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(highfiveme, caption="*{} highfives {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/highfive"
      r = requests.get(url)
      e = r.json()
      highfiveme = e["results"][0]["url"]
      await message.reply_video(highfiveme, caption="*Highfives U With All My Friendship*~")
      return

@bot.on_message(filters.regex("Neko happy") & filters.command("happy"))
async def happy(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/happy"
       r = requests.get(url)
       e = r.json()
       happyme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(happyme, caption="*{} Is So Happy Today Did You Know {} ?*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/happy"
      r = requests.get(url)
      e = r.json()
      happyme = e["results"][0]["url"]
      await message.reply_video(happyme, caption="*U So Happy Today But Why*~")
      return

@bot.on_message(filters.regex("Neko laugh") & filters.command("laugh"))
async def laugh(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/laugh"
       r = requests.get(url)
       e = r.json()
       laughme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(laughme, caption="*{} Is Laughed By {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/laugh"
      r = requests.get(url)
      e = r.json()
      laughme = e["results"][0]["url"]
      await message.reply_video(laughme, caption="*I Can't Control Laughing*~")
      return

@bot.on_message(filters.regex("Neko bite") & filters.command("bite"))
async def bite(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/bite"
       r = requests.get(url)
       e = r.json()
       biteme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(biteme, caption="*{} Bites {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/bite"
      r = requests.get(url)
      e = r.json()
      biteme = e["results"][0]["url"]
      await message.reply_video(biteme, caption="*Bites u with all my strength*~")
      return

@bot.on_message(filters.regex("Neko poke") & filters.command("poke"))
async def poke(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/poke"
       r = requests.get(url)
       e = r.json()
       pokeme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(pokeme, caption="*{} pokes {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/poke"
      r = requests.get(url)
      e = r.json()
      pokeme = e["results"][0]["url"]
      await message.reply_video(pokeme, caption="*Poking You Continuously*~")
      return

@bot.on_message(filters.regex("Neko tickle") & filters.command("tickle"))
async def tickle(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/tickle"
       r = requests.get(url)
       e = r.json()
       tickleme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(tickleme, caption="*{} tickles {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/tickle"
      r = requests.get(url)
      e = r.json()
      tickleme = e["results"][0]["url"]
      await message.reply_video(tickleme, caption="*Tickling You Continuously Don't Laugh*~")
      return

@bot.on_message(filters.regex("Neko wave") & filters.command("wave"))
async def wave(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/wave"
       r = requests.get(url)
       e = r.json()
       waveme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(waveme, caption="*{} waves {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/wave"
      r = requests.get(url)
      e = r.json()
      waveme = e["results"][0]["url"]
      await message.reply_video(waveme, caption="*My Hand Waving To You*~")
      return

@bot.on_message(filters.regex("Neko thumbsup") & filters.command("thumbsup"))
async def thumbsup(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/thumbsup"
       r = requests.get(url)
       e = r.json()
       thumbsupme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(thumbsupme, caption="*{} thumbsups with {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/thumbsup"
      r = requests.get(url)
      e = r.json()
      thumbsupme = e["results"][0]["url"]
      await message.reply_video(thumbsupme, caption="*Hey Come Let's Thumbsup*~")
      return

@bot.on_message(filters.regex("Neko stare") & filters.command("stare"))
async def stare(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/stare"
       r = requests.get(url)
       e = r.json()
       stareme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(stareme, caption="*{} stares {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/stare"
      r = requests.get(url)
      e = r.json()
      stareme = e["results"][0]["url"]
      await message.reply_video(stareme, caption="*What You Said Say It Again*~")
      return

@bot.on_message(filters.regex("Neko cuddle") & filters.command("cuddle"))
async def cuddle(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/cuddle"
       r = requests.get(url)
       e = r.json()
       cuddleme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(cuddleme, caption="*{} cuddles {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/cuddle"
      r = requests.get(url)
      e = r.json()
      cuddleme = e["results"][0]["url"]
      await message.reply_video(cuddleme, caption="*Cuddle u with all my love*~")
      return

@bot.on_message(filters.regex("Neko smile") & filters.command("smile"))
async def smile(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/smile"
       r = requests.get(url)
       e = r.json()
       smileme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(smileme, caption="*{} smiles by seeing {}'s face*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/smile"
      r = requests.get(url)
      e = r.json()
      smileme = e["results"][0]["url"]
      await message.reply_video(smileme, caption="*Is Smiles Looking Beautiful ?*~")
      return

@bot.on_message(filters.regex("Neko baka") & filters.command("baka"))
async def baka(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/baka"
       r = requests.get(url)
       e = r.json()
       bakame = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(bakame, caption="*{} said {} is baka*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/baka"
      r = requests.get(url)
      e = r.json()
      bakame = e["results"][0]["url"]
      await message.reply_video(bakame, caption="*You A Stupid Baka!*~")
      return

@bot.on_message(filters.regex("Neko blush") & filters.command("blush"))
async def blush(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/blush"
       r = requests.get(url)
       e = r.json()
       blushme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(blushme, caption="*{} blushes by seeing {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/blush"
      r = requests.get(url)
      e = r.json()
      blushme = e["results"][0]["url"]
      name1 = message.from_user.first_name
      await message.reply_video(blushme, caption="*Oh {}~kun I Luv You*~".format(name1))
      return

@bot.on_message(filters.regex("Neko think") & filters.command("think"))
async def think(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/think"
       r = requests.get(url)
       e = r.json()
       thinkme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(thinkme, caption="*{} thoughts about {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/think"
      r = requests.get(url)
      e = r.json()
      thinkme = e["results"][0]["url"]
      name = message.from_user.first_name
      await message.reply_video(thinkme, caption="*{}~kun Do You Love Me?*~".format(name))
      return

@bot.on_message(filters.regex("Neko pout") & filters.command("pout"))
async def pout(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/pout"
       r = requests.get(url)
       e = r.json()
       poutme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(poutme, caption="*{} pouts {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/poutme"
      r = requests.get(url)
      e = r.json()
      name = message.from_user.first_name
      poutme = e["results"][0]["url"]
      await message.reply_video(poutme, caption="*Oi {}~kun*~".format(name))
      return

@bot.on_message(filters.regex("Neko facepalm") & filters.command("facepalm"))
async def facepalm(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/facepalm"
       r = requests.get(url)
       e = r.json()
       facepalmme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(facepalmme, caption="*{} Made {} To Facepalm*~".format(name2, name1))
       return
    else:
      url = "https://nekos.best/api/v2/facepalm"
      r = requests.get(url)
      e = r.json()
      name = message.from_user.first_name
      facepalmme = e["results"][0]["url"]
      await message.reply_video(facepalmme, caption="*Oh Shit {}~kun*~".format(name))
      return

@bot.on_message(filters.regex("Neko wink") & filters.command("wink"))
async def wink(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/wink"
       r = requests.get(url)
       e = r.json()
       winkme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(winkme, caption="*{} winks {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/wink"
      r = requests.get(url)
      e = r.json()
      winkme = e["results"][0]["url"]
      await message.reply_video(winkme, caption="*Winks u with all my love*~")
      return

@bot.on_message(filters.regex("Neko smug") & filters.command("smug"))
async def smug(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/smug"
       r = requests.get(url)
       e = r.json()
       smugme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(smugme, caption="*{} sumgs {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/smug"
      r = requests.get(url)
      e = r.json()
      smugme = e["results"][0]["url"]
      await message.reply_video(smugme, caption="*Hehehehehehehehe*~")
      return

@bot.on_message(filters.regex("Neko cry") & filters.command("cry"))
async def cry(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/cry"
       r = requests.get(url)
       e = r.json()
       cryme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(cryme, caption="*{} is cried did you know {}?*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/cry"
      r = requests.get(url)
      e = r.json()
      cryme = e["results"][0]["url"]
      await message.reply_video(cryme, caption="*I Can't Stop Crying*~")
      return

@bot.on_message(filters.regex("Neko dance") & filters.command("dance"))
async def dance(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/dance"
       r = requests.get(url)
       e = r.json()
       danceme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(danceme, caption="*{} danced with {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/dance"
      r = requests.get(url)
      e = r.json()
      name = message.from_user.first_name
      danceme = e["results"][0]["url"]
      await message.reply_video(danceme, caption="*{}~kun. Can You Dance With Me*~".format(name))
      return

@bot.on_message(filters.regex("Neko feed") & filters.command("feed"))
async def feed(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/feed"
       r = requests.get(url)
       e = r.json()
       feedme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(feedme, caption="*{} feeds {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/feed"
      r = requests.get(url)
      e = r.json()
      feedme = e["results"][0]["url"]
      name = message.from_user.first_name
      await message.reply_video(feedme, caption="*Open You Mouth {}~kun*~".format(name))
      return

@bot.on_message(filters.regex("Neko shrug") & filters.command("shrug"))
async def shrug(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/shrug"
       r = requests.get(url)
       e = r.json()
       shrugme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(shrugme, caption="*{} shrugs to {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/shrug"
      r = requests.get(url)
      e = r.json()
      name = message.from_user.first_name
      shrugme = e["results"][0]["url"]
      await message.reply_video(shrugme, caption="*I Don't Know About It {}~kun*~".format(name))
      return

@bot.on_message(filters.regex("Neko bored") & filters.command("bored"))
async def bored(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/bored"
       r = requests.get(url)
       e = r.json()
       boredme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(boredme, caption="*{} bored to see {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/bored"
      r = requests.get(url)
      e = r.json()
      name = message.from_user.first_name
      boredme = e["results"][0]["url"]
      await message.reply_video(boredme, caption="*Today Was So Boring {}~kun Any Idea?*~".format(name))
      return


@bot.on_message(filters.regex("Neko pat") & filters.command("pat"))
def pat(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/pat"
       r = requests.get(url)
       e = r.json()
       patme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       message.reply_to_message.reply_video(patme, caption="*{} pats {}*~".format(name1, name2))
    else:    
      name = (
          message.reply_to_message.from_user.first_name
          if message.reply_to_message
          else message.from_user.first_name
      )
      url = "https://nekos.best/api/v2/pat"
      r = requests.get(url)
      e = r.json()
      patme = e["results"][0]["url"]
      message.reply_video(patme, caption=randomessage.choice(OWO).format(name))

@bot.on_message(filters.regex("Neko hug") & filters.command("hug"))
def hug(_, message):
    
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/hug"
       r = requests.get(url)
       e = r.json()
       hugme = e["results"][0]["url"]
       
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       message.reply_to_message.reply_video(hugme, caption="*{} hugs {}*".format(name1, name2))
    else:
       url = "https://nekos.best/api/v2/hug"
       r = requests.get(url)
       e = r.json()
       hugme = e["results"][0]["url"]
       
       message.reply_video(hugme, caption="*Hugs u with all my love*~")

@bot.on_message(filters.regex("Neko slap") & filters.command("slap"))      
def slap(_, message):
    
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/slap"
       r = requests.get(url)
       e = r.json()
       slapme = e["results"][0]["url"]
       
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       message.reply_to_message.reply_video(slapme, caption="*{} slaps {}*".format(name1, name2))
    else:
       url = "https://nekos.best/api/v2/slap"
       r = requests.get(url)
       e = r.json()
       slapme = e["results"][0]["url"]
       
       message.reply_video(slapme, caption="Here... Take this from me.")

@bot.on_message(filters.regex("Neko cute") & filters.command("cute"))
def cute(_, message):
    name = message.from_user.first_name         
    url = f"https://nekos.best/api/v2/neko"
    r = requests.get(url)
    e = r.json()
    cuteme = e["results"][0]["url"]
    message.reply_photo(
        cuteme, caption="Thank UwU {}-Kun  *smiles and hides ^~^*".format(name)
    )

@bot.on_message(filters.regex("Neko waifu") & filters.command("waifu"))
def waifu(_, message):
    name = message.from_user.first_name         
    url = f"https://nekos.best/api/v2/waifu"
    r = requests.get(url)
    e = r.json()
    waifume = e["results"][0]["url"]
    message.reply_photo(
        waifume, caption="Here I Am {}-Kun's *Waifu*".format(name)
    )

@bot.on_message(filters.regex("Neko kitsune") & filters.command("kitsune"))
def kitsune(_, message):
    name = message.from_user.first_name         
    url = f"https://nekos.best/api/v2/kitsune"
    r = requests.get(url)
    e = r.json()
    kitsuneme = e["results"][0]["url"]
    message.reply_photo(
        kitsuneme, caption="Did You Called Me {}-Kun's *?*".format(name)
    )

@bot.on_message(filters.regex("Neko sleep") | filters.regex("sleep") & filters.command("sleep"))
def sleep(_, message):
    sleep_type = random.choice(("Text", "Gif", "Video"))
    if sleep_type == "Gif":
        try:
            url = "https://nekos.best/api/v2/sleep"
            r = requests.get(url)
            e = r.json()
            sleepme = e["results"][0]["url"]
            message.reply_video(sleepme)
        except BadRequest:
            sleep_type = "Text"

    if sleep_type == "Video":
        try:
            bed = "https://telegra.ph/file/f0fb71c72e059de34b565.mp4"
            message.reply_video(bed)
        except BadRequest:
            sleep_type = "Text"

    if sleep_type == "Text":
        z = ". . . (∪｡∪)｡｡｡zzzZZ"
        message.reply_text(z)

@bot.on_message(filters.regex("Neko") & filters.command("neko"))
def neko(_, message):
    name = message.from_user.first_name
    ke = random.choice(aasf)
    message.reply_text(
        ke.format(name)
    )

@bot.on_message(filters.command(["start"], ["/", ".", "?"]))
async def start(_, message):
      buttons = [[
          InlineKeyboardButton("[► Repo ◄]", url="https://github.com/Team-Aasf/Nekos-Best-Bot"),
          InlineKeyboardButton("[► Deploy ◄]", url="https://heroku.com/deploy?template=https://github.com/Team-Aasf/Nekos-Best-Bot")
      ]]
      url = "https://nekos.best/api/v2/neko"
      r = requests.get(url)
      e = r.json()
      pics = e["results"][0]["url"]
      kk = await message.reply(text="`ねこねこ`")
      time.sleep(2)
      await kk.delete()
      await message.reply_photo(
            photo=pics,
            caption=PM_START_TEXT.format(
                message.from_user.mention
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
        )

@bot.on_message(filters.command(["help"], ['/', ".", "?"]))
def help(_, message):
    url = "https://nekos.best/api/v2/neko"
    r = requests.get(url)
    e = r.json()
    pics = e["results"][0]["url"]
    buttons = [[
        InlineKeyboardButton("[► Repo ◄]", url="https://github.com/Team-Aasf/Nekos-Best-Bot"),
        InlineKeyboardButton("[► Deploy ◄]", url="https://heroku.com/deploy?template=https://github.com/Team-Aasf/Nekos-Best-Bot")
    ]]
    await message.reply_photo(pics, caption=help_text,
                             reply_markup=InlineKeyboardMarkup(buttons))
