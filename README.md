<p align="center"><img src="https://github-readme-stats.vercel.app/api/pin/?username=Terabaapxd&repo=AvengerBot&theme=dark" /></a></p>

<h4 align="center">
    :exclamation: Please star and fork this project before using it.
</h4>

#

<p align="center">
<a href="https://github.com/TeamAvengerBot/AvengerBot/network/members"><img src="https://img.shields.io/github/forks/Terabaapxd/AvengerBot?style=social" />
<a href="https://github.com/TeamAvengerBot/AvengerBot"><img src="https://img.shields.io/github/stars/Terabaapxd/AvengerBot?style=social" />
<a href="https://github.com/TeamAvengerBot/AvengerBot"><img src="https://img.shields.io/github/watchers/terabaapxd/AvengerBot?style=social" />
<a href="https://github.com/TeamAvengerBot/AvengerBot"><img src="https://img.shields.io/github/repo-size/Terabaapxd/AvengerBot?style=social&logo=github" />
<a href="https://github.com/TeamAvengerBot/AvengerBot/commits/mukesh"><img src="https://img.shields.io/github/last-commit/TeamAvengerBot/AvengerBot?style=social&logo=github" />
<a href="https://github.com/TeamAvengerBot/AvengerBot/issues"><img src="https://img.shields.io/github/issues/Terabaapxd/AvengerBot?style=social&logo=github" />
<a href="https://app.codacy.com/project/badge/Grade/33ac0deeb7b14a028cf6bd574999abeb"><img src="https://img.shields.io/codacy/grade/33ac0deeb7b14a028cf6bd574999abeb?color=gold&logo=github&style=social" />
<a href="https://github.com/Terabaapxd/AvengerBot/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=social&logo=github" />
<a href="https://gitHub.com/TeamAvengerBot/AvengerBot/graphs/commit-activity"><img src="https://img.shields.io/badge/Maintained-yes-green.svg?style=social&logo=github" />
</p>

#

<h2 align="center">
   ⇝ Requirements ⇜
</h2>

<p align="center">
    <a href="https://www.python.org/downloads/release/python-390/"> Python3.9 </a> |
    <a href="https://docs.pyrogram.org/intro/setup#api-keys"> Telegram API Key </a> |
    <a href="https://t.me/botfather"> Telegram Bot Token </a> |
    <a href="https://telegra.ph/How-To-get-Mongodb-URI-04-06"> MongoDB URI </a>
</p>

#

<h2 align="center">
   ⇝ Install Locally Or On A VPS ⇜
</h2>

```console
git clone https://github.com/Terabaapxd/AvengerBot
cd AvengerBot
pip3 install -U -r requirements.txt
cp sample_config.env config.env
```

<h3 align="center">
    Edit <b>config.env</b> with your own values
</h3>

<h2 align="center">
   ⇝ Run Directly ⇜
</h2>

```console
python3 -m Avenger
```
<h1>
    <p align="center">
        <a href="https://heroku.com/deploy?template=https://github.com/Terabaapxd/AvengerBot">
            <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
        </a>
    </p>
</h1>

## Mandatory Vars

- These are the minimum required vars need to setup to make Avenger Bot functional.

1. `API_ID` : Get it from my.telegram.org 
2. `API_HASH`  : Get it from my.telegram.org 
3. `BOT_TOKEN` : Get it from [@Botfather](http://t.me/BotFather) in Telegram
4. `MONGO_URL` : Get it from mongo db website
5. `LOG_GROUP_ID` : You'll need a Private Group ID for this. Supergroup Needed with id starting from -100 
6. `SUDO_USERS_ID` : Sudo User id for making sudoers or you can put your own telegram Id.
7. `OWNER_ID` : Your Owner ID for managing your bot.
8. `GBAN_LOG_GROUP_ID` : You'll need a Private Group ID for this. Supergroup Needed with id starting from -100
9. `MESSAGE_DUMP_CHAT` : You'll need a Private Group ID for this. Supergroup Needed with id starting from -100
10. `WELCOME_DELAY_KICK_SEC` : Fill 300 in this var section
11. `ARQ_API_URL` : Fill http://arq.hamker.dev
13. `ARQ_API_KEY` : Get it from @ARQRobot by typing /get_key
14. `RSS_DELAY` : Fill 300 in this var section
15. `UPSTREAM_REPO` : Fill https://github.com/TeamAvengerBot/AvengerBot.git

<h1 align="center">
   ⇝ Docker ⇜
</h1>

```console
git clone https://github.com/TeamAvengerBot/AvengerBot
cd AvengerBot
cp sample_config.env config.env
```

<h3 align="center">
    Edit <b> config.env </b> with your own values
</h3>

```console
sudo docker build . -t Avenger
sudo docker run Avenger
```

<h2 align="center">
   ⇝ Write new modules ⇜
</h2>

```py
# Add license text here, get it from below

from Avenger import app # This is bot's client
from pyrogram import filters # pyrogram filters
...


# For /help menu
__MODULE__ = "Module Name"
__HELP__ = "Module help message"


@app.on_message(filters.command("start"))
async def some_function(_, message):
    await message.reply_text("I'm already up!!")

# Many useful functions are in, Avenger/utils/, Avenger, and Avenger/core/
```

<h3 align="center">
   And put that file in Avenger/modules/ restart and test your bot.
</h3>

All the credit goes to 
https://github.com/rozari0
https://github.com/TheHamkerCat
