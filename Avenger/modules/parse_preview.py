from asyncio import sleep

from pyrogram import filters
from pyrogram.types import Message

from Avenger import SUDOERS, app, eor
from Avenger.core.sections import section


@app.on_message(
    filters.command("parse_preview") & filters.user(SUDOERS),
)
async def parse(_, message: Message):
    r = message.reply_to_message
    has_wpp = False

    m_ = await eor(message, text="Parsing...")
    if not r:
        return await m_.edit("Reply to a message with a webpage")

    if not r.web_page:
        text = r.text or r.caption
        if text:
            m = await app.send_message(m_.chat.id, text)
            await sleep(1)
            await m.delete()
            if m.web_page:
                r = m
                has_wpp = True
    else:
        has_wpp = True

    if not has_wpp:
        return await m_.edit(
            "Replied message has no webpage preview.",
        )

    wpp = r.web_page

    body = {
        "Title": [wpp.title or "Null"],
        "Description": [
            (wpp.description[:50] + "...") if wpp.description else "Null"
        ],
        "URL": [wpp.display_url or "Null"],
        "Author": [wpp.author or "Null"],
        "Site Name": [wpp.site_name or "Null"],
        "Type": wpp.type or "Null",
    }

    text = section("Preview", body)

    t = wpp.type

    if t == "photo":
        media = wpp.photo
        func = app.send_photo
    elif t == "audio":
        media = wpp.audio
        func = app.send_audio
    elif t == "video":
        media = wpp.video
        func = app.send_video
    elif t == "document":
        media = wpp.document
        func = app.send_document
    else:
        media = None
        func = None

    if media and func:
        await m_.delete()
        return await func(
            m_.chat.id,
            media.file_id,
            caption=text,
        )

    await m_.edit(text, disable_web_page_preview=True)
