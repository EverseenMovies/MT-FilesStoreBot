# (c) @EverseenMovies

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("MT_BOT_TOKEN")
	BOT_USERNAME = os.environ.get("MT_BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("MT_BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("MT_UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("MT_LOG_CHANNEL"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("MO_TECH_YT", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

🧑🏻‍ **Developer:** @EverseenMovies

👨‍💻 **Editing:** @EverseenMovies

🗣️ **Any Doubt:** @Everseen_Movies

📢 **Updates Channel:** [Discovery Projects](https://t.me/EverseenMovies)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍ **Developer:** @EverseenMovies

👨‍💻 **Editing:** @EverseenMovies

🗣️ **Any Doubt:** @Everseen_Movies

📢 **Updates Channel:** [Discovery Projects](https://t.me/Everseen_Movies)

Donate Now (coming soon)
"""
	HOME_TEXT = """
**👋Hi**, [{}](tg://user?id={})\n\n**This is Permanent** **ESM FileShare Bot**.

**Send me any file I will give you a permanent Sharable Link.It was Created by Our Channel @EverseenMovies purpose Only.I Support Channel Also! Check About Bot Button.Don't send any copyright content until the bot is Stopped by @EverseenMovies**.
"""

