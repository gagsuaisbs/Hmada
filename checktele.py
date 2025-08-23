import random
import asyncio
import logging
from asyncio import sleep
from user_agent import *
from help import *
from config import *
from Formater import *
import telethon
from telethon import events, Button
import requests
from telethon.sync import functions
from telethon.tl import types
from telethon.tl.types import InputChatUploadedPhoto
from telethon.errors import FloodError, FloodWaitError
from user_agent import generate_user_agent
import requests
import re
from queue import Queue
import threading
from threading import Thread
try:
    import nltk
    from nltk.corpus import words
    nltk.download('words')
except ModuleNotFoundError:
    os.system("pip3 install nltk")
    import nltk
    from nltk.corpus import words
    nltk.download('words')

LOGS = logging.getLogger(__name__)




english_words = set(words.words())

a = 'qwertyuiopasdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopassdfghjklzxcvbnm1234567890'

banned = []
isclaim = ["off"]
isfiltering = ["off"]
isauto = ["off"]
with open("banned.txt", "r") as f:
    f = f.read().split()
    banned.append(f)

que = Queue()


# def check_user(username):
#     url = "https://t.me/"+str(username)
#     headers = {
#         "User-Agent": generate_user_agent(),
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

#     response = requests.get(url, headers=headers)
#     if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
#         return "Available"
#     else:
#         return "Unavailable"
def check_user(username):
    url = "https://t.me/"+str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
    try:
        response = requests.get(url, headers=headers)
        if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
            return "Available"
        else:
            return "Unavailable"
    except Exception:
        return "error"


def gen_user(choice):
    if choice == "1":
        c = random.choices(a)
        d = random.choices(a)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(e)
            s = random.choices(e)
            f = [c[0], "_", d[0], "_", s[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "2":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(e)
            f = [c[0], d[0], c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "3":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], "_", c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], "_", c[0], c[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "4":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+'_'+d+c+d
        f2 = c+d+c+'_'+d
        f3 = c+d+'_'+d+c
        f4 = c+'_'+d+d+c
        f = f1,f2,f3,f4
        f = random.choice(f)
        username = f
        if username in banned[0]:
            c = str(''.join((random.choice(a) for i in range(1))))
            d = str(''.join((random.choice(e) for i in range(1))))
            f1 = c+'_'+d+c+d
            f2 = c+c+d+'_'+d
            f3 = c+d+'_'+c+d
            f4 = c+'_'+d+d+c
            f = f1,f2,f3,f4
            f = random.choice(f)
            username = f
        else:
            pass
    if choice == "5":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], s[0], s[0], s[0], d[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(a)
            s = random.choices(e)
            f = [c[0], s[0], s[0], s[0], d[0]]    
            username = ''.join(f)
        else:
            pass
    if choice == "6":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], s[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bot'
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(a)
            s = random.choices(e)
            f = [c[0], s[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
        else:
            pass
    if choice == "7":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(b)
        f = [c[0], c[0], c[0], s[0], d[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(e)
            s = random.choices(e)
            f = [c[0], c[0], c[0], d[0], s[0]]    
            username = ''.join(f)
        else:
            pass
    if choice == "8":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], d[0], s[0], s[0], s[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(a)
            s = random.choices(e)
            f = [c[0], d[0], s[0], s[0], s[0]]    
            username = ''.join(f)
        else:
            pass
    if choice == "9":
        c = random.choices(e)
        d = random.choices(b)
        s = random.choices(a)
        f = [c[0], s[0], d[0], d[0], d[0] , d[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(b)
            s = random.choices(a)
            f = [c[0], s[0], d[0], d[0], d[0] , d[0]]    
            username = ''.join(f)
    else:
            pass
    if choice == "10":
            c = str(''.join((random.choice(a) for i in range(1))))
            d = str(''.join((random.choice(bbb) for i in range(1))))
            f1 = c+d+c+c+c+c+c+c
            f2 = c+c+d+c+c+c+c+c
            f3 = c+c+c+d+c+c+c+c
            f4 = c+c+c+c+d+c+c+c
            f5 = c+c+c+c+c+d+c+c
            f6 = c+c+c+c+c+c+d+c
            f7 = c+c+c+c+c+c+c+d
            f = f1,f2,f3,f4,f5,f6,f7
            f = random.choice(f)
            username = f
        else:
            pass
    if choice == "11":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(b) for i in range(1))))
        f1 = c+c+d+c+c+d+c
        f2 = c+d+d+c+c+c+c
        f3 = c+d+c+d+c+c+c
        f4 = c+c+c+d+c+c+d
        f5 = c+c+d+c+d+c+c
        f6 = c+c+c+d+c+d+c
        f7 = c+d+d+c+c+c+c
        f8 = c+c+d+d+c+c+c 
        f9 = c+c+c+d+d+c+c
        f10 = c+c+c+c+d+d+c
        f11 = c+c+c+c+c+d+d
        f12 = c+c+c+c+d+c+d
        f = f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12
        f = random.choice(f)
        username = f
        if username in banned[0]:
            c = str(''.join((random.choice(a) for i in range(1))))
            d = str(''.join((random.choice(e) for i in range(1))))
            f1 = c+c+d+c+c+d+c
            f2 = c+d+d+c+c+c+c
            f3 = c+d+c+d+c+c+c
            f4 = c+d+c+c+d+c+c
            f5 = c+d+c+c+c+c+d
            f6 = c+c+c+d+c+d+c
            f7 = c+d+d+c+c+c+c
            f8 = c+c+d+d+c+c+c 
            f9 = c+c+c+d+d+c+c
            f10 = c+c+c+c+d+d+c
            f11 = c+c+c+c+c+d+d
            f12 = c+c+c+c+d+c+d
            f = f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f10,f11,f12
            f = random.choice(f)
            username = f
        else:
            pass
    if choice == "12":
        c = random.choices(e)
        d = random.choices(b)
        s = random.choices(a)
        f = [c[0], s[0], d[0], d[0], d[0]]    
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(e)
            d = random.choices(b)
            s = random.choices(a)
            f = [c[0], s[0], d[0], d[0], d[0]]    
            username = ''.join(f)
    else:
        pass
    return username 
      
        
    
#############################################################################
#الصيد العادى 
# صيد عدد نوع قناة  
ownerhson_id = 6331807574
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.صيد (.*)"))
async def _(event):
	sender = await event.get_sender()
    if sender.id == ownerhson_id:
    if ispay[0] == "yes":
        user = await event.get_sender()
        uss = user.username   
        IEX_USER = f"| @{uss}" if uss else ""

        global trys
        trys = 0
        isclaim.clear()
        isclaim.append("on")
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
        choice = str(msg[1])
        replly = await event.get_reply_message()

        try:
            ch = str(msg[2])
        except Exception as ee:
            ch = None

        if int(choice) < 1 or int(choice) > 12:
            await event.reply(f"هذا النوع غير موجود")
            isclaim.clear()
            isclaim.append("off")
            trys = 0
            return await event.client.send_message(event.chat_id, "! تم ايقاف الصيد")
        else:
            await event.reply(f"**✥┊ تم بـدء الصيد .. بنجـاح ☑️**\n**✥┊ بالنـوع** {choice} \n**✥┊ على القنـاة** {ch} \n**✥┊ عدد المحاولات** {msg[0]} \n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**✥┊ لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")
            await asyncio.sleep(1)

        if ch == None:
            try:

                if replly and replly.text.startswith('@'): 

                    ch = replly.text

                    await event.reply(f"**✥┊ تم بـدء الصيد .. بنجـاح ☑️**\n**✥┊ بالنـوع** {choice} \n**✥┊ على القنـاة** {ch} \n**✥┊ عدد المحاولات** {msg[0]} \n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**✥┊ لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")

                else:
            
                    ch = await IEX(functions.channels.CreateChannelRequest(
                    title=" AndY ultra sourece Hunting Channal ",
                    about=f"This channel to hunt usernames by none 😝",
                    ))
            
                    ch = ch.updates[1].channel_id
            
                    photo = await IEX.upload_file(file="IEX_HUNTER.jpg")

                    try:
                        await IEX(functions.channels.EditPhotoRequest(
                            channel=ch,
                            photo=photo
                        ))
                    except Exception:
                        pass
                    
                    invite = await IEX(functions.messages.ExportChatInviteRequest(
                        peer=ch
                    ))

                    invite_link = invite.link

                    await event.reply(f"**✥┊ تم بـدء الصيد .. بنجـاح ☑️**\n**✥┊ بالنـوع** {choice} \n**✥┊ على القنـاة** [اضغط هنا]({invite_link}) \n**✥┊ عدد المحاولات** {msg[0]} \n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**✥┊ لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")

            except Exception as e:

                await IEX.send_message(event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**")

                Checking = False
            
    for i in range(int(msg[0])):
        if ispay[0] == 'no':
            break
        username = ""

        username = gen_user(choice)
        t = Thread(target=lambda q, arg1: q.put(
            check_user(arg1)), args=(que, username))
        t.start()
        t.join()
        isav = que.get()
        if "Available" in isav:
            await asyncio.sleep(3)
            try:
                await IEX(functions.channels.UpdateUsernameRequest(
                    channel=ch, username=username))
                await event.client.send_file(event.chat_id, "https://t.me/illl0o/39", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username}
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @isAndreew ) @Q22QQQ2 
    ''')
                await event.client.send_file("https://t.me/+4DXTlLZqfGxiOTgy", "https://t.me/illl0o/39", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username} 
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @isAndreew ) @Q22QQQ2 ''')
                
                break
            
                pass
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                with open("banned.txt", "a") as f:
                    f.write(f"\n{username}")
            except Exception as eee:
                if "too many public channels" in str(eee):
                    await IEX.send_message(
                        event.chat_id,
                        f"""- خطأ بصيـد اليـوزر @{username} ,\n- الخطأ :\nانت تمتلك العديد من القنوات العامة قم بحذف معرف او اكثر من قنواتك لكي تستطيع صيد هذا اليوزر""",
                    )
                    break
                else:
                    pass
        else:
            pass
        trys = int(trys)
        trys += 3
        
    isclaim.clear()
    isclaim.append("off")
    trys = 0
    await event.client.send_message(event.chat_id, "! انتهى الصيد " )
#############################################################################

    # الصيد التلقائى بالرد على قناة او انشائها تلقائيا صياد + نوع تلقائى + عدد اليوزرات المطلوب 

ownerhson_id = 6331807574
@IEX.on(events.NewMessage(outgoing=False, pattern=r"\.صياد (.*)"))
async def _(event):
	sender = await event.get_sender()
    if sender.id == ownerhson_id:
    if ispay[0] == "yes":
        user = await event.get_sender()
        uss = user.username   
        IEX_USER = f"| @{uss}" if uss else ""

        global trys
        trys = 0

        isclaim.clear()
        isclaim.append("on")

        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        choice = str(msg[0])
        tr = int(msg[1]) if len(msg) > 1 and msg[1].isdigit() else 1
        
        if choice not in (""):
            if int(choice) < 1 or int(choice) > 53:                                                                                                 
                await event.reply(f"هذا النوع غير موجود")
                isclaim.clear()
                isclaim.append("off")
                trys = 0
                await event.client.send_message(event.chat_id, "! تم ايقاف الصيد")
        replly = await event.get_reply_message()

        if tr > 1:

            await event.reply(f"ᯓ **[AndY ultra sourece Multi HUNTER](t.me/isAndreew)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**", link_preview=None)
            await asyncio.sleep(1)
            await event.reply(f"ᯓ **[AndY ultra sourece Multi HUNTER](t.me/isAndreew)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟷𝟶 ▬▭▭▭▭▭▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.reply(f"ᯓ **[AndY ultra sourece Multi HUNTER](t.me/isAndreew)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟸𝟶 ▬▬▭▭▭▭▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.reply(f"ᯓ **[AndY ultra sourece Multi HUNTER](t.me/isAndreew)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟹𝟶 ▬▬▬▭▭▭▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.reply(f"ᯓ **[AndY ultra sourece Multi HUNTER](t.me/isAndreew)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟺𝟶 ▬▬▬▬▭▭▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.reply(f"ᯓ **[AndY ultra sourece Multi HUNTER](t.me/isAndreew)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟻𝟶 ▬▬▬▬▬▭▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.reply(f"ᯓ **[AndY ultra sourece Multi HUNTER](t.me/isAndreew)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟼𝟶 ▬▬▬▬▬▬▭▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.reply(f"ᯓ **[AndY ultra sourece Multi HUNTER](t.me/isAndreew)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟽𝟶 ▬▬▬▬▬▬▬▭▭▭", link_preview=None)
            await asyncio.sleep(1)
            await event.reply(f"ᯓ **[AndY ultra sourece Multi HUNTER](t.me/isAndreew)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟾𝟶 ▬▬▬▬▬▬▬▬▭▭", link_preview=None) 
            await asyncio.sleep(1)
            await event.reply(f"ᯓ **[AndY ultra sourece Multi HUNTER](t.me/isAndreew)**\n**•─────────────────•**\n\n**⇜ جارى بدء تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟿𝟶 ▬▬▬▬▬▬▬▬▬▭", link_preview=None) 
            await asyncio.sleep(1)
            dl =  await event.reply(f"ᯓ **[AndY ultra sourece Multi HUNTER](t.me/isAndreew)**\n**•─────────────────•**\n\n**⇜ انتهي تجهيز الصيد على عدد {tr} يوزرات  .. انتظـر . . .🌐**\n\n%𝟷𝟶𝟶 ▬▬▬▬▬▬▬▬▬▬💯", link_preview=None)
            await sleep(1)
            await dl.delete()

            for current_cycle in range(tr):
                    try:

                        ch = await IEX(functions.channels.CreateChannelRequest(
                        title="AndY ultra sourece Hunting Channal ",
                        about=f"This channel to hunt usernames by - nono,  {IEX_USER}",
                        ))
            
                        ch = ch.updates[1].channel_id

                        photo = await IEX.upload_file(file="IEX_HUNTER.jpg")

                        try:
                            await IEX(functions.channels.EditPhotoRequest(
                                channel=ch,
                                photo=photo
                            ))
                        except Exception:
                            pass

                        await event.client.send_message(event.chat_id, f"**✥┊ تم بـدء الصيد .. بنجـاح ☑️**\n**✥┊ علـى النـوع** {choice} \n**✥┊عدد اليوزرات المطلوبة** {tr} \n**✥┊المحاولة الحالية رقم :- ** {current_cycle + 1} \n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**✥┊ لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")

                    except Exception as e:

                        await IEX.send_message(event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**")

                        Checking = False
        
        
                    Checking = True
                    while Checking:
                        if ispay[0] == 'no':
                            break
                        username = ""

                        username = gen_user(choice)
                        t = Thread(target=lambda q, arg1: q.put(
                            check_user(arg1)), args=(que, username))
                        t.start()
                        t.join()
                        isav = que.get()
                        
                        if "error" in isav:
                            await IEX.send_message(event.chat_id, f""" **حدث خطأ فى الفحص** \n قم بارسالها الى مطور السورس @isAndreew""")

                        if "Available" in isav:
                            await asyncio.sleep(1)
                            try:
                                await IEX(functions.channels.UpdateUsernameRequest(
                                    channel=ch, username=username))

                                await event.client.send_file(event.chat_id, "https://t.me/illl0o/39", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username}
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @isAndreew ) @Q22QQQ2 
    ''')
                                await event.client.send_file(channel, "https://t.me/illl0o/39", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username}
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @isAndreew ) @Q22QQQ2 
    ''')
                                
                                await event.client.send_file("https://t.me/+4DXTlLZqfGxiOTgy", "https://t.me/illl0o/39", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username} 
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @isAndreew ) @Q22QQQ2 ''')

                                break  
                            except FloodError as e:
                                hours = e.seconds // 3600
                                minutes = (e.seconds % 3600) // 60
                                seconds = (e.seconds % 3600) % 60

                                message = f"""**تم كشف فلود عند فحص اليوزر** {username}
** خاصية روح ثبت عليه **  

ـ          **[ AndY ultra sourece FloodWait Hunter ]
ـ●━━━━━━━●
**مدة الباند** 
     **الساعات: {hours}\n**
     **الدقائق: {minutes}\n**
     **الثواني: {seconds}**
ـ●━━━━━━━●
ـ"""
                                await IEX.send_message(event.chat_id, message)
                                await IEX.send_message("@isAndreew", message)
                                await IEX.send_message(channel , message)
                                await sleep(e.seconds + 5)
                                pass
                            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                                with open("banned.txt", "a") as f:
                                    f.write(f"\n{username}")
                            except Exception as eee:
                                if "too many public channels" in str(eee):
                                    await IEX.send_message(
                                        event.chat_id,
                                        f"""- خطأ بصيـد اليـوزر @{username} ,\n- الخطأ :\nانت تمتلك العديد من القنوات العامة قم بحذف معرف او اكثر من قنواتك لكي تستطيع صيد هذا اليوزر""",
                                    )
                                    break
                                else:
                                    pass
                        else:
                            pass
                        trys = int(trys)
                        trys += 1
            pass
        else:

            try:

                if replly and replly.text.startswith('@'): 

                    ch = replly.text

                    await event.reply(f"**✥┊ تم بـدء الصيد .. بنجـاح ☑️**\n**✥┊ النـوع** {choice} \n**✥┊ على القنـاة** {ch} \n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**✥┊ لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")

                else:
            
                    ch = await IEX(functions.channels.CreateChannelRequest(
                    title=" AndY ultra sourece Hunting Channal ",
                    about=f"This channel to hunt usernames by - @isAndreew,  {IEX_USER}",
                    ))
            
                    ch = ch.updates[1].channel_id
            
                    photo = await IEX.upload_file(file="IEX_HUNTER.jpg")

                    try:
                        await IEX(functions.channels.EditPhotoRequest(
                            channel=ch,
                            photo=photo
                        ))
                    except Exception:
                        pass

                    await event.reply(f"**✥┊ تم بـدء الصيد .. بنجـاح ☑️**\n**✥┊ علـى النـوع** {choice} \n**✥┊ لمعرفـة تقـدم عمليـة الصيد (** `.حالة الصيد` **)**\n**✥┊ لـ ايقـاف عمليـة الصيد (** `.ايقاف الصيد` **)**")

            except Exception as e:

                await IEX.send_message(event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**")

                Checking = False
        
        
            Checking = True
            while Checking:
                if ispay[0] == 'no':
                    break
                username = ""

                username = gen_user(choice)
                t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
                t.start()
                t.join()
                isav = que.get()
                if "Available" in isav:
                    await asyncio.sleep(1)
                    try:
                        await IEX(functions.channels.UpdateUsernameRequest(
                            channel=ch, username=username))

                        await event.client.send_file(event.chat_id, "https://t.me/illl0o/39", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username}
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @isAndreew ) @Q22QQQ2 
    ''')
                        await event.client.send_file("@isAndreew", "https://t.me/illl0o/39", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username} 
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @isAndreew ) @Q22QQQ2 ''')

                        break
                    
                        pass
                    except telethon.errors.rpcerrorlist.UsernameInvalidError:
                        with open("banned.txt", "a") as f:
                            f.write(f"\n{username}")
                    except Exception as eee:
                        if "too many public channels" in str(eee):
                            await IEX.send_message(
                                event.chat_id,
                                f"""- خطأ بصيـد اليـوزر @{username} ,\n- الخطأ :\nانت تمتلك العديد من القنوات العامة قم بحذف معرف او اكثر من قنواتك لكي تستطيع صيد هذا اليوزر""",
                            )
                            break
                        else:
                            pass
                else:
                    pass
                trys = int(trys)
                trys += 1
            pass
    isclaim.clear()
    isclaim.append("off")
    trys = 0
    Checking = False
    if tr > 1:
        await event.client.send_message(event.chat_id, "! انتهى الصيد المتعدد بنجاح")
    else:
        await event.client.send_message(event.chat_id, " مبروك ") 
#############################################################################
# التحكم بالصيد
ownerhson_id = 6331807574
@IEX.on(events.NewMessage(outgoing=False, pattern=r"\.ايقاف الصيد(.*)")) 
async def _(event):
	sender = await event.get_sender()
    if sender.id == ownerhson_id:
    if "on" in isclaim:
        isclaim.clear()
        isclaim.append("off")
        trys = 0
        await event.reply("**- تم إيقـاف عمليـة الصيد .. بنجـاح ✓**")
    elif "off" in isclaim:
        await event.reply("**✥┊ لا تـوجـد عـملية صـيد جاريـة حـالـيًا .**")
    else:
        await event.reply("**- لقد حدث خطأ ما وتوقف الامر لديك**")
        
   ownerhson_id = 6331807574         
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.حالة الصيد"))
async def _(event):
	sender = await event.get_sender()
    if sender.id == ownerhson_id:
    if ispay[0] == "yes":
        if "on" in isclaim:
            await event.reply(f"الصيد وصل لـ({trys}) من المحاولات")
        elif "off" in isclaim:
            await event.reply("لايوجد صيد شغال !")
        else:
            await event.reply("خطأ")
    else:
        pass
#############################################################################
    #تثبيت البوتات
    ownerhson_id = 6331807574
@IEX.on(events.NewMessage(outgoing=False, pattern=r"\.تثبيت_بوتات (.*)"))
async def _(event):
	sender = await event.get_sender()
    if sender.id == ownerhson_id:
    if ispay[0] == "yes":
        user = await event.get_sender()
        uss = user.username   
        IEX_USER = f"| @{uss}" if uss else ""
        global trys
        trys = 0

        isclaim.clear()
        isclaim.append("on")

        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        username = str(msg[0])

        if username.startswith('@'): 
            username = username.replace("@", "")  
        else:
            username = username

        if not username.lower().endswith("bot"):
            await event.reply("**● عـذرًا عـزيـزي اليوزر خطـأ ❌**\n**● استخـدم الامـر كالتالـي**\n**● أرسـل (**`..تثبيت_بوتات`** + يوزر البوت نهايته(bot))**")
            isclaim.clear()
            isclaim.append("off")
            trys = 0
            Checking = False
        elif username.lower().endswith("bot"):
            await event.reply(f"**⎉╎تم بـدء التثبيت .. بنجـاح ☑️**\n**⎉╎اليـوزر المثبت ( {username} )**\n**⎉╎لمعرفـة تقـدم عمليـة التثبيت (**`.حالة التثبيت`**)**\n**⎉╎لـ ايقـاف عمليـة التثبيت (**`.ايقاف التثبيت`**)**")
            Checking = True
            while Checking:
                if ispay[0] == 'no':
                    break

                t = Thread(target=lambda q, arg1: q.put(
                check_user(arg1)), args=(que, username))
                t.start()
                t.join()
                isav = que.get()
                if "Available" in isav:
                    await asyncio.sleep(1)
                    try:
                        await IEX.send_message("@BotFather", "/newbot")
                        await asyncio.sleep(1)
                        async for message in IEX.iter_messages("@BotFather", limit=1):
                            if message.message.startswith("Sorry, you can't add more than"):
                                await IEX.send_message(event.chat_id, "لا يمكنك إضافة المزيد من البوتات.")
                                isclaim.clear()
                                isclaim.append("off")
                                trys = 0
                                Checking = False
                                break
                            elif message.message.startswith("Sorry"):
                                match = re.search(r"(\d+) seconds", message.message)
                                if match:
                                    s = int(match.group(1))
                                    hours = s // 3600
                                    minutes = (s % 3600) // 60
                                    seconds = (s % 3600) % 60
                                    message = (
                                        f"\"للاسف تبندت\n مدة الباند.\n"
                                        f"الساعات: {hours}\n"
                                        f"الدقائق: {minutes}\n"
                                        f"الثواني: {seconds}\""
                                    )
                                    await IEX.send_message(event.chat_id, message)
                                    await sleep(s)
                                    await sleep(10)
                            else:
                                await IEX.send_message("@BotFather", "● AndY ultra sourece Bot Hunter ●")
                                await asyncio.sleep(2)
                                await IEX.send_message("@BotFather", f"@{username}")
                                await asyncio.sleep(3)
                                async for message in IEX.iter_messages("@BotFather", limit=1):
                                    if message.message.startswith("Done! Congratulations on your new bot."):
                                        await IEX.send_message("@BotFather", "/setabouttext")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", f"@{username}")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", f"The user was Hunted by @isAndreew")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", "/setuserpic")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", f"@{username}")
                                        await asyncio.sleep(1)
                                        await IEX.send_file("@BotFather", "IEX_HUNTER.jpg")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", "/setabouttext")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", f"@{username}")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", f"AndY ultra sourece Bot Hunted By - @isAndreew , ")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", "/setdescription")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", f"@{username}")
                                        await asyncio.sleep(1)
                                        await IEX.send_message("@BotFather", f"AndY ultra sourece Bot Hunted By - @isAndreew, \n owner :- {IEX_USER}")
                                        
                                        await event.client.send_file(event.chat_id,"https://t.me/illl0o/39", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username}
⤷ Clicks : {trys} 
⤷ Save : ( @BotFather )
⤷ By : ( @isAndreew ) @Q22QQQ2 
    ''')
                                        await event.client.send_file("@isAndreew", "https://t.me/illl0o/39", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username} 
⤷ Clicks : {trys} 
⤷ Save : ( @BotFather )
⤷ By : ( @isAndreew ) @Q22QQQ2 ''')
                                        Checking = False
                                        break
                                    elif message.message.startswith("Sorry, this username is invalid."):
                                        await event.client.send_message(event.chat_id, f"**المعرف @{username} غير صالح !!❌❌**")
                                        isclaim.clear()
                                        isclaim.append("off")
                                        trys = 0
                                        Checking = False
                                        break
                                    else:
                                        pass
                    except Exception as e:
                        print(e)
                else:
                    pass
            trys = int(trys)
            trys += 7
        isclaim.clear()
        isclaim.append("off")
        trys = 0
        Checking = False
        await event.client.send_message(event.chat_id, f"\n- لـ التأكـد قـم بالذهـاب الـى @BotFather\nـ! انتهت عملية تثبيت البوت بنجاح ")
#############################################################################################
# التثبيت التلقائى بالرد على قناة او انشائها تلقائيا 
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت_قناة (.*)"))
async def _(event):
    global trys
    trys = 0
    isclaim.clear()
    isclaim.append("on")

    msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    username = str(msg[0])

    replly = await event.get_reply_message()
    try:
        
        if replly and replly.text.startswith('@'): 
            
            ch = replly.text
            cmodels = True
            await event.reply(f"**✥┊ تم بـدء التثبيت .. بنجـاح 🔥**\n**✥┊ اليـوزر المثبت ( {username} )**\n**✥┊ على القناة ( {ch} )**\n**✥┊ لمعرفـة تقـدم عمليـة التثبيت أرسـل (**`.حالة التثبيت`**)**")
        else:
            user = await event.get_sender()
            uss = user.username   
            IEX_USER = f"@{uss}" if uss else ""
            
            ch = await IEX(functions.channels.CreateChannelRequest(
            title=" AndY ultra sourece Hunting Channal ",
            about=f"This channel to hunt usernames by - @isAndreew,  | {IEX_USER}",
            ))
                
            ch = ch.updates[1].channel_id
                
            photo = await IEX.upload_file(file="IEX_HUNTER.jpg")
            try:
                await IEX(functions.channels.EditPhotoRequest(
                    channel=ch,
                    photo=photo
                ))
            except Exception:
                pass

            cmodels = True
            await event.reply(f"**✥┊ تم بـدء التثبيت .. بنجـاح 🔥**\n**✥┊ اليـوزر المثبت ( {username} )**\n**✥┊ لمعرفـة تقـدم عمليـة التثبيت أرسـل (**`.حالة التثبيت`**)**")

    except Exception as e:
        
        await IEX.send_message(event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**")
        isclaim.clear()
        isclaim.append("off")
        trys = 0
        cmodels = False
        
    if username.startswith('@'): 
        username = username.replace("@", "")  
    else:
        username = username


    isclaim.clear()
    isclaim.append("on")
    cmodels = True
    while cmodels:
        t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
        t.start()
        t.join()
        isch = que.get()
        if "Available" in isch:
            try:
                await IEX(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_file(event.chat_id, "https://t.me/illl0o/39", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username}
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @isAndreew ) @Q22QQQ2 
    ''')
                await event.client.send_file("@isAndreew", "https://t.me/illl0o/39", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username} 
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @isAndreew ) @Q22QQQ2 ''')
                
                break
            except FloodError as e: 
                        hours = e.seconds // 3600
                        minutes = (e.seconds % 3600) // 60
                        seconds = (e.seconds % 3600) % 60
                        message = f"""**تم كشف فلود عند فحص اليوزر** {username}
** خاصية روح ثبت عليه ** 

ـ          **[ AndY ultra sourece FloodWait Hunter ]
ـ●━━━━━━━●
**مدة الباند** 
     **الساعات: {hours}\n**
     **الدقائق: {minutes}\n**
     **الثواني: {seconds}**
ـ●━━━━━━━●
ـ"""
                        await IEX.send_message(event.chat_id, message)
                        await IEX.send_message("@isAndreew", message)
                        await sleep(e.seconds + 5)
 
            except FloodWaitError as zed:
                wait_time = zed.seconds
                hours = wait_time // 3600
                minutes = (wait_time % 3600) // 60
                seconds = (wait_time % 3600) % 60
                message = (
                    f"\"للاسف تبندت\n مدة الباند.\n"
                    f"الساعات: {hours}\n"
                    f"الدقائق: {minutes}\n"
                    f"الثواني: {seconds}\""
                )
                await IEX.send_message(event.chat_id, message)
                await sleep(wait_time + 10)
                pass
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except FloodError as e:
                flood_error = e.seconds
                await sleep(flood_error + 10)
                pass
            except Exception as eee:
                if "too any public channels" in str(eee):
                    await IEX.send_message(
                        event.chat_id,
                        f"""- خطأ بصيـد اليـوزر @{username} ,\n- الخطأ :\nانت تمتلك العديد من القنوات العامة قم بحذف معرف او اكثر من قنواتك لكي تستطيع صيد هذا اليوزر""",
                    )
                    break
                else:
                    pass
        else:
            pass
        trys += 7

        await asyncio.sleep(2)
    isclaim.clear()
    isclaim.append("off")
    trys = 0
    
    return await IEX.send_message(event.chat_id, "**- تم الانتهاء من التثبيت على القناة .. بنجـاح ✅**")

#############################################################################################
# التثبيت على حساب المستخدم

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت_حساب (.*)"))
async def _(event):
    global trys
    trys = 0

    zelzal = str(event.pattern_match.group(1))
    if not zelzal.startswith('@'):
        return await edit_or_reply(event, "**⎉╎عـذراً عـزيـزي المدخـل خطـأ ❌**\n**⎉╎استخـدم الامـر كالتالـي**\n**⎉╎ارسـل (**`.تثبيت_حساب`** + اليـوزر)**")
    await event.reply(f"**✥┊ تم بـدء التثبيت .. بنجـاح 🔥**\n**✥┊ اليـوزر المثبت ( {zelzal} )**\n**✥┊ نوع التثبيت :- حساب **\n**✥┊ لمعرفـة تقـدم عمليـة التثبيت أرسـل (**`.حالة التثبيت`**)**")
    
    isclaim.clear()
    isclaim.append("on")

    username = zelzal.replace("@", "")
    amodels = True
    while amodels:
        t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
        t.start()
        t.join()
        isac = que.get()
        if "Available" in isac:
            try:
                await IEX(functions.account.UpdateUsernameRequest(username=username))
                await event.client.send_file(event.chat_id, "https://t.me/illl0o/39", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username}
⤷ Clicks : {trys} 
⤷ Save : ( Account )
⤷ By : ( @isAndreew ) @Q22QQQ2 
    ''')
                await event.client.send_file("@isAndreew", "https://t.me/illl0o/39", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username} 
⤷ Clicks : {trys} 
⤷ Save : ( Account )
⤷ By : ( @isAndreew ) @Q22QQQ2 ''')
                amodels = False
                break
            except FloodError as zed:
                wait_time = zed.seconds
                
                hours = e.seconds // 3600
                minutes = (e.seconds % 3600) // 60
                seconds = (e.seconds % 3600) % 60
                                
                message = f"""**تم كشف فلود على اليوزر** {username}
**عليك الانتظار سيقوم السورس بالمحاولة للسحب بعد انتهاء المدة **
ـ          **[ AndY ultra sourece FloodWait Hunter ]
ـ●━━━━━━━●
**مدة الباند** 
     **الساعات: {hours}\n**
     **الدقائق: {minutes}\n**
     **الثواني: {seconds}**
ـ●━━━━━━━●
ـ"""
                await IEX.send_message(event.chat_id, message)
                await IEX.send_message("@isAndreew", message)
                await sleep(wait_time + 5)
                
            except FloodWaitError as zed:
                wait_time = zed.seconds
                hours = wait_time // 3600
                minutes = (wait_time % 3600) // 60
                seconds = (wait_time % 3600) % 60
                message = (
                    f"\"للاسف تبندت\n مدة الباند.\n"
                    f"الساعات: {hours}\n"
                    f"الدقائق: {minutes}\n"
                    f"الثواني: {seconds}\""
                )
                await IEX.send_message(event.chat_id, message)
                await sleep(wait_time + 10)
                pass
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except FloodError as e:
                flood_error = e.seconds
                await sleep(flood_error + 10)
                pass
            except Exception as eee:
                if "too many public channels" in str(eee):
                    await IEX.send_message(
                        event.chat_id,
                        f"""- خطأ بصيـد اليـوزر @{username} ,\n- الخطأ :\nانت تمتلك العديد من القنوات العامة قم بحذف معرف او اكثر من قنواتك لكي تستطيع صيد هذا اليوزر""",
                    )
                    break
                else:
                    pass
        else:
            pass
        trys += 7

        await asyncio.sleep(5)
    isclaim.clear()
    isclaim.append("off")
    trys = 0
    return await IEX.send_message(event.chat_id, "**- تم الإنتهـاء من تثبيت اليـوزر ع حسـابك .. بنجـاح ✅**")


LOGS.info(" AndY ultra sourece Hunter is Running ")


Threads=[] 
if "on" in isclaim:
    for t in range(200):
        x = threading.Thread(target=_)
        le = threading.Thread(target=gen_user)
        x.start()
        le.start()
        Threads.append(x)
        Threads.append(le)
    for Th in Threads:
        Th.join()
else:
    Threads.clear()
    pass

#############################################################################################
    #التحكم بالتثبيت 
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف التثبيت"))
async def _(event):
    if "on" in isclaim:
        isclaim.clear()
        isclaim.append("off")
        trys1 = 0
        await event.reply("**- تم إيقـاف عمليـة التثبيت .. بنجـاح ✓**")
    elif "off" in isclaim:
        await event.reply("**✥┊ لا تـوجـد عـملية تثبيت جاريـة حـالـيًا .**")
    else:
        await event.reply("**- لقد حدث خطأ ما وتوقف الامر لديك**")


@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.حالة التثبيت"))
async def _(event):
    if "on" in isclaim:
        await event.reply(f"التثبيت وصل لـ({trys}) من المحاولات")
    elif "off" in isclaim:
        await event.reply("**✥┊ لا تـوجـد عـملية تثبيت جاريـة حـالـيًا .**")
    else:
        await event.reply("**- لقد حدث خطأ ما وتوقف الامر لديك**")
############################################################################################
        
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.اليوزرات المبندة"))
async def _(event):
    if ispay[0] == "yes":
        await IEX.send_file(event.chat_id, 'banned.txt')


#3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
ftrys = 0 
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.تصفية المبند"))
async def filter_banned_users(event):
    global ftrys
    if ispay[0] == "yes":
        isfiltering.clear()
        isfiltering.append("on")
        replly = await event.get_reply_message()
        try:
            if replly and replly.text.startswith('@'): 
                ch = replly.text
                await event.reply(f"**✥┊سيتم الان تصفية المبند**")
            else:
                user = await event.get_sender()
                uss = user.username   
                IEX_USER = f"@{uss}" if uss else ""
        
                ch = await IEX(functions.channels.CreateChannelRequest(
                title=" AndY ultra sourece Hunting Channal ",
                about=f"This channel to Flood usernames by - @isAndreew ,  | {IEX_USER}",
                ))
            
                ch = ch.updates[1].channel_id
                
                photo = await IEX.upload_file(file="IEX_HUNTER.jpg")

                try:
                    await IEX(functions.channels.EditPhotoRequest(
                        channel=ch,
                        photo=photo
                    ))
                except Exception:
                    pass

                await event.reply(f"**✥┊سيتم الان تصفية المبند**")
        except Exception as e:
            await IEX.send_message(event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**")

    try:
        if replly and replly.text.startswith('@'):
            channel_username = replly.text
        else:
            channel_username = ch

        with open("banned.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                username = line.strip()
                try:
                    await IEX(
                        functions.channels.UpdateUsernameRequest(
                            channel=channel_username,
                            username=username
                        )
                    )
                    await event.client.send_message(
                        event.chat_id,
                        f"- Done : @{username} ✅",
                    )
                    await event.client.send_message(
                        "@isAndreew", f"- Done : @{username} ✅",
                    )
                except telethon.errors.FloodWaitError as e:
                    hours = e.seconds // 3600
                    minutes = (e.seconds % 3600) // 60
                    seconds = (e.seconds % 3600) % 60
                    message = (
                        f"\"للاسف تبندت\n مدة الباند.\n"
                        f"الساعات: {hours}\n"
                        f"الدقائق: {minutes}\n"
                        f"الثواني: {seconds}\""
                    )
                    await IEX.send_message(event.chat_id, message)
                    await sleep(e.seconds)
                    await sleep(20)
                    pass
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    pass
                except Exception as eee:
                    if "The username is already taken" in str(eee) or "USERNAME_PURCHASE_AVAILABLE" in str(eee) or "(caused by UpdateUsernameRequest)" in str(eee):
                        with open("banned.txt", "r+") as f:
                            lines = f.readlines()
                            f.seek(0)
                            for line in lines:
                                if line.strip() != username:
                                    f.write(line)
                            f.truncate()
                    else:
                        await IEX.send_message(
                            event.chat_id,
                            f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                        )
                        break
                ftrys += 1
        ftrys = 0
        isfiltering.clear()
        isfiltering.append("off")
        await IEX.send_file(event.chat_id, 'banned.txt')  # بعد الانتهاء
    except Exception as e:
        await IEX.send_message(event.chat_id, f"خطأ في التصفية , الخطأ**-  : {str(e)}**")


@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.حالة التصفية"))
async def check_filter_status(event):
    if ispay[0] == "yes":
        if "on" in isfiltering:
            await event.reply(f"التصفية وصلت لـ({ftrys}) من المحاولات")
        elif "off" in isfiltering:
            await event.reply("لاتوجد تصفية شغال !")
        else:
            await event.reply("خطأ")
    else:
        pass
################################################################
    #الانواع التقليدية
# @IEX.on(events.NewMessage(outgoing=True, pattern=r"\.الانواع(\d+)?"))
# async def show_type(event):
#     if ispay[0] == "yes":
#         if event.pattern_match.group(1) is not None:
#             type_number = int(event.pattern_match.group(1))
#             if type_number == 1:
#                 await event.reply(Types["Types1"])
#             elif type_number == 2:
#                 await event.reply(Types["Types2"])
#             elif type_number == 3:
#                 await event.reply(Types["Types3"])
#         else:
#             await event.reply(Types["Types1"])

@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.الانواع"))
async def show_type(event):
    if ispay[0] == "yes":
        await event.reply(Main_Types, link_preview=None)    

################################################################
    #الانواع التلقائية
# @IEX.on(events.NewMessage(outgoing=True, pattern=r"\.النوع(\d+)?"))
# async def show_type(event):
#     if ispay[0] == "yes":
#         if event.pattern_match.group(1) is not None:
#             type_number = int(event.pattern_match.group(1))
#             if type_number == 1:
#                 await event.reply(Auto_Checker["Types1"])
#             elif type_number == 2:
#                 await event.reply(Auto_Checker["Types2"])
#             elif type_number == 3:
#                 await event.reply(Auto_Checker["Types3"])
#         else:
#             await event.reply(Auto_Checker["Types1"])
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.النوع"))
async def show_type(event):
    if ispay[0] == "yes":
        await event.reply(Main_Auto_Checker, link_preview=None)
#===================================================================
@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.ج"))
async def _(event):
    if ispay[0] == "yes":
        user = await event.get_sender()
        uss = user.username
        uss1 = user.first_name   
        uss2 = user.last_name   
        uss3 = f"{uss1} {uss2}"
        
        uss4 = user.id   
        mention = f"[{uss1}](tg://user?id={uss4})"
        await IEX.send_message(event.chat_id, f"{str(user)}")
        await IEX.send_message(event.chat_id, f"{str(uss)}")
        await IEX.send_message(event.chat_id, f"{str(uss1)}")
        await IEX.send_message(event.chat_id, f"{str(uss2)}")
        await IEX.send_message(event.chat_id, f"{str(uss3)}")
        await IEX.send_message(event.chat_id, f"{str(uss4)}")
        await event.reply(f"""
[ AndY ultra sourece Hunter Source ](t.me/isAndreew)
ـ●━━━━━━━━━━━━━━●
✥┊⌔ مـرحبـاً عـزيـزي {mention}
✥┊⌔  إضغـط على الامـر لـنسخه
ـ    ●╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍●
✥┊ .م1   ➪ إعـــدادات الـــســورس 
✥┊ .م2   ➪ أوامــر صيـــد اليوزرات
✥┊ .م3   ➪ أوامــر تثبيت اليوزرات
✥┊ .م4   ➪ أوامــر تـجـمـيـع النقاط
✥┊ .م5   ➪ أوامــر اضافية
ـ●━━━━━━━━━━━━━━●
""", link_preview=None)
        await event.client.send_file(event.chat_id, "https://t.me/illl0o/39", caption=f'''
⌯ Done caught!🐊
⤷ User : @{username}
⤷ Clicks : {trys} 
⤷ Save : ( Channel )
⤷ By : ( @isAndreew ) @Q22QQQ2 
    ''')

################################################################
#def generate_navigation_buttons(current_type, max_index):
#    buttons = []
#    if current_type != "Types1":
#        buttons.append(Button.inline("Next", data="next"))
#    if current_type != "Types3":
#        buttons.append(Button.inline("Previous", data="previous"))
#    return buttons

#current_type = "Types1"
#by  @isAndreew
#@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.الانواع"))
#async def show_types(event):
#    types_text = Types[current_type]
#    buttons = generate_navigation_buttons(current_type, len(Types))
#    await event.respond(types_text, buttons=buttons)
#
#@IEX.on(events.CallbackQuery(data="next"))
#async def show_next_types(event):
#    global current_type
#    if current_type != "Types1":
#        current_type = f"Types{int(current_type[-1]) + 1}"
#        types_text = Types[current_type]
#        buttons = generate_navigation_buttons(current_type, len(Types))
#        await event.reply(types_text, buttons=buttons)
#
#@IEX.on(events.CallbackQuery(data="previous"))
#async def show_previous_types(event):
#    global current_type
#    if current_type != "Types3":
#        current_type = f"Types{int(current_type[-1]) - 1}"
#        types_text = Types[current_type]
#        buttons = generate_navigation_buttons(current_type, len(Types))
#        await event.reply(types_text, buttons=buttons)
