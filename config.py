# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "21711546"))
API_HASH = getenv("API_HASH", "f1e60f632bd307ef776a43314e05252b")
BOT_TOKEN = getenv("BOT_TOKEN", "8005510299:AAHk780q5LAz6HBJ6H4VcpZd2AQDS9OIxnA")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7787884100").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://january2024new:KBTzMhl16jyQvuCm@cluster0.ukupd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002446589215")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002285112175"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
