from logging import exception
import re
import requests
import ast
from pyrogram.types.list import List
import json
from config import *

class myMdisk():
    def __init__ (self, message):
        self.msg = message

async def runTextApp (post):
    msg = post.msg
    newText = await get_short_url(msg.text)
    return newText

async def runCaptionApp (post):
    msg = post.msg
    newText = await get_short_url(msg.caption)
    return newText

    # await bot.send_message(chat_id=msg.chat.id, text=newText)

async def fast_short_url (link):
    try:
        if await find_assets_url(url=link) == False:
            return link
        asset_link = await find_assets_url(url=link)
        telegraph_link = await save_on_telegraph(assets_url=asset_link)
        short_url = await converting_gplinks(telegraph_url=telegraph_link)
        short_url = f'`{short_url}`'
        return short_url
    except exception as e:
        print(e)

async def get_short_url (text):
    links = re.findall(r'https?://mdisk.me[^\s]+', text)
    for link in links:
        try:
            asset_link = await find_assets_url(url=link)
            telegraph_link = await save_on_telegraph(assets_url=asset_link)
            short_url = await converting_gplinks(telegraph_url=telegraph_link)
            short_url = f'`{short_url}`'
            text = text.replace(link, short_url)
        except:
            text = text.replace(link, text)
    return text


async def find_assets_url (url):
    try:
        api = 'https://diskuploader.entertainvideo.com/v1/file/cdnurl?param=' + url.split('/')[-1]

        req = requests.get(api)
        data = req.text
        dict_data = json.loads(data)
        print(dict_data['source'])
        return (dict_data['source'])
    except:
        return False

async def save_on_telegraph (assets_url):
    api = 'https://api.telegra.ph/createPage?access_token=8bf3ce97f0eddf0792130955626a9d4813922ba62846f0ce60d0456ee249&title=Join+@PrimeCineplex+On+Telegram&author_name=@PrimeCineplex&content=[{%22tag%22:%22h3%22,%20%22children%22:%20[%22Your+Direct+Link+Generated...%22]},{%22tag%22:%22pre%22,%20%22children%22:%20[%22'+ assets_url+ '%22]},{%22tag%22:%22h4%22,%20%22children%22:%20[%22How+To+Play+In+VLC+Player%22]},{%22tag%22:%22ul%22,%20%22children%22:%20[{%22tag%22:%22li%22,%20%22children%22:%20[%22First+Join+Over+Main+Channel+@PrimeCineplex+On+Telegram.%22]},{%22tag%22:%22li%22,%20%22children%22:%20[%22Download+VLC+Player+For+Windows%22]},{%22tag%22:%22li%22,%20%22children%22:%20[%22Open+VLC+Player%22]},{%22tag%22:%22li%22,%20%22children%22:%20[%22Copy+Above+URL%22]},{%22tag%22:%22li%22,%20%22children%22:%20[%22Copy+Above+URL%22]},{%22tag%22:%22li%22,%20%22children%22:%20[%22Paste+Directly+In+VLC+Player%22]},{%22tag%22:%22li%22,%20%22children%22:%20[%22Click+On+Play,+Enjoy+%F0%9F%98%89%22]}]}]&return_content=true'

    req = requests.get(url=api)
    data = json.loads(req.text)
    telegraph_url = data['result']['url']
    return telegraph_url

async def converting_gplinks(telegraph_url):
    api = 'https://gplinks.in/api?api=448926946a4b49eeaa09521115f725a50113b79b&url=' + telegraph_url

    req = requests.get(api)
    data = json.loads(req.text)
    short_url = data['shortenedUrl']
    return short_url


# --------------------- 

async def get_msg_entities(message_entities, text):
    x = []
    string = str(message_entities)
    res = ast.literal_eval(string)
    try:
        for i in res:
            # print(i)

            if "url" in i and 'mdisk.me' in i['url']:
                print("url")
                
                line = await fast_short_url(i['url'])
                text += f'\n{line}\n'
                print(text)
            else:
                pass
                # print("others")
                # x.append(MessageEntity(type=i["type"], offset=i["offset"], length=i["length"]))
    except:
        entities = message_entities
    
    return text


async def get_reply_markup(msg, text):
    # print(message)
    reply_markup = msg.reply_markup
    buttsons = []
    all_buttons = []
    # for markup in reply_markup["inline_keyboard"]:
    for markup in reply_markup.inline_keyboard:
        # print(markup)
        buttons = []
        for j in markup:
            buttonText = j.text
            buttonURL = j.url
            # Skip Other Link From Buttons
            if 'mdisk.me' not in buttonURL:
                continue
            print(buttonURL)
            try:
                url = await fast_short_url(buttonURL)
                text += f'\n{buttonText} {url}\n'
            except:
                text += f'\n{buttonText} {buttonURL}\n'

    return text
