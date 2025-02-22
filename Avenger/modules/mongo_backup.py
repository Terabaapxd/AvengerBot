from os import remove
from os import system as execute

from pyrogram import filters
from pyrogram.types import Message

from Avenger import MONGO_URL, SUDOERS, app


@app.on_message(
    filters.command("backup") & filters.user(SUDOERS) & filters.private
)
async def backup(_, message: Message):
    m = await message.reply("Backing up data...")

    code = execute(f'mongodump --uri "{MONGO_URL}"')
    if int(code) != 0:
        return await m.edit(
            "Looks like you don't have mongo-database-tools installed "
            + "grab it from mongodb.com/try/download/database-tools"
        )

    code = execute("zip backup.zip -r9 dump/*")
    if int(code) != 0:
        return await m.edit(
            "Looks like you don't have `zip` package installed, BACKUP FAILED!"
        )

    await message.reply_document("backup.zip")
    await m.delete()
    remove("backup.zip")
