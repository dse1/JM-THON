# ======================================================================================================================================
# ping -> edited ping with pic by  @RR7PP
# كتابة الملف لسورس جمثون فقط ممنوع نسبه لنفسك
# تخمط دليل فشلك اخمط وكول اني مطور 😂😂

import os
from datetime import datetime

from userbot import jmthon

from . import hmention, reply_id

"""
try:
    from . import PING_PIC, PING_TEXT
except:
    pass
"""
plugin_category = "tools"

PING_PIC = os.environ.get("PING_PIC") or (
    "https://telegra.ph/file/9fae7cafab308cff9f5eb.jpg"
)

JM_TXT = os.environ.get("PING_TEXT") or "𝙳𝚘 𝚗𝚘𝚝 𝚌𝚘𝚖𝚙𝚊𝚛𝚎 𝚖𝚎 ‏ঌ"


@jmthon.ar_cmd(
    pattern="بنق$",
    command=("بنق", plugin_category),
    info={
        "header": "امر تجربه البوت اذا يشتغل ارسل  .بنك فقط",
        "option": "امر بنق المتطور كتابة  @C1CiC",
        "usage": [
            "{tr}بنق",
        ],
    },
)
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    start = datetime.now()
    cat = await edit_or_reply(
        event, "<b><i>  ثواني عيني .... </b></i>", "html"
    )
    end = datetime.now()
    await cat.delete()
    ms = (end - start).microseconds / 1000
    if PING_PIC:
        caption = f"<b><i>{JM_TXT}<i><b>\n<code>\n  ♪ 𝗢𝗪𝗡𝗘𝗥 -  <b>{hmention}</b>\n\n✦⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯✦"
        await event.client.send_file(
            event.chat_id,
            PING_PIC,
            caption=caption,
            parse_mode="html",
            reply_to=reply_to_id,
            link_preview=False,
            allow_cache=True,
        )
    else:
        await event.edit_or_reply(
            event, "<code>يجـب اضـافة متـغير `PING_PIC`  اولا  f<code>", "html"
        )


# ======================================================================================================================================
