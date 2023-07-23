import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", "23990433"))

API_HASH = os.environ.get("API_HASH", "e6c4b6ee1933711bc4da9d7d17e1eb20")

STRING = os.environ.get("STRING", "AQFJv5gAgM0c5zCc07iCokZWg5r8v5WizWFniJYld19i721FhzN1Y-v2I5KH721rNAewKqldZYCi7XfXv5GOofQOs3DqdYU-jGR-hrm24wkB46wkFBGKjpo4VcNQVbuvkioxc9YaSPP1njLhyRqmMlf9b-6zWUDbz-VQyEVzJEr2NipEkrngdM2V44sE8gbrdftTFZpVbBeZ5m1J2SK086h54UiMVdfdTijbVF1SXTjPCZ86pKY9iwdQRzanyXEu_wt_UNpDaVrcqr3FFvzPhIL1oPp9U6kkEe0IJNdM4teuL8oFQhRuXkHLKj7I3H0Rr788k6ujAZGJ0pKSZykaXi-uHHssDQAAAAF0ma4lAA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
