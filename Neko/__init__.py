import os

from pyrogram import Client

API_ID = os.environ.get('API_ID', None)
API_HASH = os.environ.get('API_HASH', None)
TOKEN = os.environ.get('TOKEN', None)

# For Local Deploy:
"""
API_ID = ""
API_HASH = ""
TOKEN = ""
"""
bot = Client(
    "NekoBest",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = TOKEN,
    plugins=dict(root=f"{__name__}/plugins/")
)
