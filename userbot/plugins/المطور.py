import random
import re
import time

from telethon.events import CallbackQuery

from userbot import StartTime, jmthon

from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus

plugin_category = "utils"


@jmthon.ar_cmd(
    pattern="المطور$",
    command=("المطور", plugin_category),
    info={
        "header": "لأظهار مطورين السورس",
        "usage": [
            "{tr}المطور",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    gvarstatus("ALIVE_EMOJI") or "  - "
    gvarstatus("ALIVE_TEXT")
    CAT_IMG = (
        gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/d5279497fcb4ab81c5fe9.jpg "
    )
    if CAT_IMG:
        CAT = [x for x in CAT_IMG.split()]
        A_IMG = list(CAT)
        PIC = random.choice(A_IMG)
        cat_caption = f"- 𝗗𝗼 𝗻𝗼𝘁 𝗰𝗼𝗺𝗽𝗮𝗿𝗲 𝗺𝗲\n"
        cat_caption += f"\n"
        cat_caption += f"➥ Muster   :  [A L O N E](t.me/C1CIC)\n"
        cat_caption += f"➥ Channel  :  [Telethon](t.me/JuuuT)\n"
        cat_caption += f"➥ Chat  :  [CHAT](t.me/jwwwt)\n"
        cat_caption += f"━━━━━━━━━━━━━\n"
        await event.client.send_file(
            event.chat_id, PIC, caption=cat_caption, reply_to=reply_to_id
        )


@jmthon.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await catalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
