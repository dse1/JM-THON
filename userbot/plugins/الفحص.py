import random
import time
from datetime import datetime
from platform import python_version

from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)

from userbot import JMVERSION, StartTime, jmthon
from userbot.Config import Config

from ..core.managers import edit_or_reply
from ..helpers.functions import check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from ..utils.decorators import sudo_cmd
from . import mention

plugin_category = "bot"

# كتـابة وتعـديل:  @RR9R7


@jmthon.ar_cmd(
    pattern="فحص$",
    command=("فحص", plugin_category),
    info={
        "header": "للـتأكـد مـن حـالة البـوت",
        "options": "لوضـع صـورة مـع الامـر يجـب عليـ ان تضـع رابط الصـورة مـع فـار `ALIVE_PIC` للحصـول علـى رابط الصـورة، بالـرد عليهـا بـ  ( `.تلكراف ميديا` ) ",
        "usage": [
            "{tr}فحص",
        ],
    },
)
@jmthon.on(sudo_cmd(pattern="فحص$", allow_sudo=True))
async def amireallyalive(event):
    "للتـأكد من ان البـوت يعـمـل"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await edit_or_reply(event, "** ⌯︙يتـم التـأكـد انتـظر قليلا رجاءا**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "-"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "**Your bot is working successfully Alone**"
    RR7_IMG = gvarstatus("ALIVE_PIC") or Config.A_PIC
    jmthon_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    caption = jmthon_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        jmver=JMVERSION,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if RR7_IMG:
        RR7 = [x for x in RR7_IMG.split()]
        PIC = random.choice(RR7)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                event,
                f"**الميـديا خـطأ **\nغـير الرابـط بأستـخدام الأمـر  \n `.اضف_فار ALIVE_PIC رابط صورتك`\n\n**لا يمـكن الحـصول عـلى صـورة من الـرابـط :-** `{PIC}`",
            )
    else:
        await edit_or_reply(
            event,
            caption,
        )


temp = """- {ALIVE_TEXT}

**{EMOJI} قاعدۿ البيانات :** تعمل بنـجاح
**{EMOJI} أصـدار التـيليثون :** `{telever}`
**{EMOJI} أصـدار جـمثون :** `{jmver}`
**{EMOJI} أصدار البـايثون :** `{pyver}`
**{EMOJI} الوقـت :** `{uptime}`
**{EMOJI} المسـتخدم:** {mention}"""
