# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "35125044"))
API_HASH = getenv("API_HASH", "443933fa1e307654bea9f06c1cf6727e")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "6502857759"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://mohitshaw1496_db_user:0dHZzKuRiiwEoL84@cluster0.jmg8pwu.mongodb.net/?appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1003751654557"))
FORCESUB = getenv("FORCESUB", "https://t.me/Z_Vertex_01")
