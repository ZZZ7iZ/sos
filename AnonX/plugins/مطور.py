import asyncio


import random
from AnonX import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import filters, Client
import config



txt = [

            "تعاال @IIIlIIv",


             "هذا حمد @IIIlIIv",
            

             "يردونكك @IIIlIIv ",
            
           
 
            
            

        ]


        


@app.on_message(command(["حمد","حميدددد", "حمددد"]))


async def cutt(client: Client, message: Message):


      a = random.choice(txt)


      await message.reply(


        f"{a}")
