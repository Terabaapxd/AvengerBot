import random
from datetime import datetime

from pyrogram import filters

from Avenger import app
from Avenger.core.decorators.errors import capture_err
from Avenger.utils.dbfunctions import get_couple, save_couple

__MODULE__ = "Couple"
__HELP__ = "/couple - To Choose Couple Of The Day"


# Date and time
def dt():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    return dt_string.split(" ")


def dt_tom():
    return (
        str(int(dt()[0].split("/")[0]) + 1)
        + "/"
        + dt()[0].split("/")[1]
        + "/"
        + dt()[0].split("/")[2]
    )


today = str(dt()[0])
tomorrow = str(dt_tom())


@app.on_message(filters.command(["couple", "couple"]) & ~filters.private)
@capture_err
async def couple(_, message):
    try:
        chat_id = message.chat.id
        is_selected = await get_couple(chat_id, today)
        if not is_selected:
            list_of_users = []
            async for i in app.get_chat_members(message.chat.id):
                if not i.user.is_bot:
                    list_of_users.append(i.user.id)
            if len(list_of_users) < 2:
                return await message.reply_text("Not enough users")
            c1_id = random.choice(list_of_users)
            c2_id = random.choice(list_of_users)
            while c1_id == c2_id:
                c1_id = random.choice(list_of_users)
            c1_mention = (await app.get_users(c1_id)).mention
            c2_mention = (await app.get_users(c2_id)).mention

            couple_selection_message = f"""**Couple of the day:**
{c1_mention} + {c2_mention} = ❤️
__New couple of the day may be chosen at 12AM {tomorrow}__"""
            await app.send_message(
                message.chat.id, text=couple_selection_message
            )
            couple = {"c1_id": c1_id, "c2_id": c2_id}
            await save_couple(chat_id, today, couple)

        else:
            c1_id = int(is_selected["c1_id"])
            c2_id = int(is_selected["c2_id"])
            c1_name = (await app.get_users(c1_id)).first_name
            c2_name = (await app.get_users(c2_id)).first_name
            couple_selection_message = f"""Couple of the day:
[{c1_name}](tg://openmessage?user_id={c1_id}) + [{c2_name}](tg://openmessage?user_id={c2_id}) = ❤️
__New couple of the day may be chosen at 12AM {tomorrow}__"""
            await app.send_message(
                message.chat.id, text=couple_selection_message
            )
    except Exception as e:
        print(e)
        await message.reply_text(e)
