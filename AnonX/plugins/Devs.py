import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonX import app, Telegram
import random
@app.on_message(
    command(["","",""," ", ""])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/839cbe67ff070e5ff3b72.jpg",
        caption=f"""
 [𝙎𝙊𝙐𝙍𝘾𝙀 𝙎𝙋𝘼𝙍𝙆](https://t.me/ZZZ7iZ)
 —————————————
 [𝙃 𝘼 𝙈 𝘿 ](https://t.me/IIIlIIv)
 
 [𓏺𝐏𝐎𝐓 𖠙 𝙎𝙊𝙐𝙍𝘾𝙀 ‌](https://t.me/IIIlIIv)
  
 [⍟𓏺𝙒𝞝𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝙎𝙊𝙐𝙍𝘾𝙀 𝙎𝙋𝘼𝙍𝙆](https://t.me/ZZZ7iZ)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ السورس ›", url=f"https://t.me/ZZZ7iZ"), 
                ],[
                    InlineKeyboardButton(
                        "‹ مطور السورس ›", url=f"https://t.me/IIIlIIv"),
                ],

            ]

        ),

    )

@app.on_message(command([f"قصيده", "قصائد", "ق", "{BOT_USERNAME} ق"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(8,20)
    url = f"https://t.me/O_O_PI/{rl}"
    await client.send_voice(message.chat.id,url,caption="**[⌁ : تـم اختيـار القصيده لـك](https://t.me/ZZZ7iZ)**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(command(["م","ميمز"]))
async def ihd(client: Client, message: Message):
    rs = random.randint(39,148)
    url = f"https://t.me/iirrrq/{rs}"
    await client.send_photo(message.chat.id,url,caption="**[⌁ : تـم اختيـار الميمز لـك](https://t.me/ZZZ7iZ)**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
            
