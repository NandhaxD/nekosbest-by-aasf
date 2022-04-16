import requests
import time
from Neko import bot

from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from pyrogram import filters

buttons = [
    [
        InlineKeyboardButton(
            text=f"[► Repo ◄]", url=f"https://github.com/Team-Aasf/Nekos-Best-Bot"
        )
    ]
]

PM_START_TEXT = """
**Welcome** {}~kun ฅ(≈>ܫ<≈)
`I'm A Neko Themed Telegram Bot Using Nekos.best! `
**Make Your Groups Active By Adding Me There! ××**
"""

@bot.on_message(filters.command(["start"], ["/", ".", "?"]))
async def start(_, m: Message):
      url = "https://nekos.best/api/v2/neko"
      r = requests.get(url)
      e = r.json()
      pics = e["results"][0]["url"]
      kk = await m.reply(text="`ねこねこ`")
      time.sleep(2)
      await kk.delete()
      await m.reply_photo(
            photo=pics,
            caption=PM_START_TEXT.format(
                m.from_user.mention
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
        )
