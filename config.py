from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "8391586"))
API_HASH = getenv("API_HASH", "b1a43ce85cad3c904b795c44c2aac9ef")
BOT_TOKEN = getenv("BOT_TOKEN", "5402913759:AAH2XxS76jDxVCMUA7FOocqQarN8Sbt-MwM")
SESSION_NAME = getenv("SESSION_NAME", "BAAkeGVSjepkSrAoJgkUiSFHJbhrj7OUZZ2LvZcrp7JDIdHu6ZUvLREL2kCj2Wlnu6RffzzYfzZwH6m4W9wRkSnpC6QLYLkuH6c24l81JE8wFdCJBO-gh-PGsn67Vs7iKMSje2EvO7aa19VKevg4vR3UQF3GKS50ubRT2PA_G4SntFz5ogY12fo3CintMPxHy2xHxRkFSNKRzAMYDddp1bDy7rnBk0KVOq98jSrdCQctY7nL2FfoJ1rnUKdlbXv4NGn9YmJ4mx6H9xaeMb4LBQzSwcUSG2rW3xKUswCyuu4_PfqSfKFjAoQj0Un0iCPR6xyh3XBN3I9SSHUJ52t1SHvjeXmNbgA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "U_8_U_2")
ALIVE_NAME = getenv("ALIVE_NAME", "music")
BOT_USERNAME = getenv("BOT_USERNAME", "")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/kingali371/My")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "kingdom12a")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "gg2003a")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "901751747").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "901751747").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
