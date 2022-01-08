import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = "5013844340:AAH95Z_E8bwChHMlklk5gX4l2r7xedsTBoM"

#Your API ID from my.telegram.org
APP_ID = 735218

#Your API Hash from my.telegram.org
API_HASH = "5a401f985e2f2490685f5c4cefa77722"

#Your db channel Id
CHANNEL_ID = -1001772884676
#OWNER ID
OWNER_ID = 831054990

#Database 
DB_URI = "postgres://eimvpxiansqfsf:176607a160b6edd979dccda7392415361011f4141d78ec8b145c227af812ab7f@ec2-52-44-58-234.compute-1.amazonaws.com:5432/dbijimad8gm9g"

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = 0

TG_BOT_WORKERS = 4

#start message
START_MSG = "Hello {mention}\n\nI can store private files in Specified Channel and other users can access it from special link."
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = "Hello {mention}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>"

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = "{previouscaption}"

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
