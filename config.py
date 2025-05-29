from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from pyro import validate_session

# ضع القيم الخاصة بك هنا مباشرة
APP_ID = 20621590
# ضع هنا الـ APP_ID الخاص بك كرقم صحيح
APP_HASH = "a7e91275d681fefd4b2453b158b254ec"
# ضع هنا الـ APP_HASH كسلسلة نصية
ss = "1BJWap1sAUJ2pnAAo29LhTLj_YZyHzg6ZaVE-58ZG5MOP4gATiH8ymDeui2sazXSpOkSn80P_SECXTpHB0yStC6MpneOogoAnL4R-2-Y92pkpqSnIdPedh1Z_RiefxyuNP-Gc6UEYb7craZCh6aP3tXA6TeVYwzWpJf2FxMBhoHF-_IJnjelzUtVqwSuu6dXLPXFtk4Y1iEND_nPEiRvr4S0N0D_o1mkI0ZoLLgLfhvtTJKkW8Tv90FE79EvTl7bWQQ9Cb2JFth8gkJFqKU_Goh-XuIICf-2N-RiVVwKPDSZbV-Ww_hLdvADmSNuZtLdrWhKdpQKQSW6s40fHJ06xVoBqNnesa7E="
  # ضع هنا الـ String Session كنص

# التحقق من صحة الجلسة
session = validate_session(ss)

# إنشاء العميل
IEX = TelegramClient(StringSession(session), APP_ID, APP_HASH)

ispay = ['yes']

# إذا كنت تستخدم بوت، يمكنك تفعيل الأسطر التالية:
# BOT_USERNAME = "your_bot_username"
# token = "your_bot_token"
# bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
# bot.start()