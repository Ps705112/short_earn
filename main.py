from pyrogram import filters
from config import *
from utils import *


########### ✅ MAIN BOT ✅ ###########
@bot.on_message()
async def all_message (client, message):
    
    if message.text:
        post = myMdisk(message=message)
        msg = post.msg

        msg_text = await runTextApp(post)
        
        if message.entities:
            msg_text = await get_msg_entities(message_entities=message.entities, text=msg_text)

        if message.reply_markup:
            msg_text = await get_reply_markup(msg, text=msg_text)

        if message.text and message.entities and message.reply_markup:
            await bot.send_message(chat_id=msg.chat.id, text=msg_text)

        elif message.text and message.entities:
            await bot.send_message(chat_id=msg.chat.id, text=msg_text)

        elif message.text and message.reply_markup:
            await bot.send_message(chat_id=msg.chat.id, text=msg_text)

        else:
            await bot.send_message(chat_id=msg.chat.id, text=msg_text)

    elif message.caption:
        post = myMdisk(message=message)
        caption = post.msg
        print(caption)
        msg_caption = await runCaptionApp(post)


        if message.caption_entities:
            msg_caption = await get_msg_entities(message_entities=message.entities, text=msg_caption)
        
        if message.reply_markup:
            msg_caption = await get_reply_markup(caption, text= msg_caption)
        
        if message.photo:
            if message.caption and message.caption_entities and message.reply_markup:
                await bot.send_photo(chat_id=caption.chat.id, photo=message.photo.file_id, caption=msg_caption)

            elif message.caption and message.caption_entities:
                await bot.send_photo(chat_id=caption.chat.id, photo=message.photo.file_id, caption=msg_caption)

            elif message.caption and message.reply_markup:
                await bot.send_photo(chat_id=caption.chat.id, photo=message.photo.file_id, caption=msg_caption)
            else:
                await bot.send_photo(chat_id=caption.chat.id, photo=message.photo.file_id, caption=msg_caption)

        ##### Video #####

        elif message.video:
            if message.caption and message.caption_entities and message.reply_markup:
                await bot.send_video(chat_id=caption.chat.id, video=message.video.file_id, caption=msg_caption)

            elif message.caption and message.caption_entities:
                await bot.send_video(chat_id=caption.chat.id, video=message.video.file_id, caption=msg_caption)

            elif message.caption and message.reply_markup:
                await bot.send_video(chat_id=caption.chat.id, video=message.video.file_id, caption=msg_caption)
            else:
                await bot.send_video(chat_id=caption.chat.id, video=message.video.file_id, caption=msg_caption)


bot.run()